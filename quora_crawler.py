#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: [YuweiYin](https://github.com/YuweiYin)
"""

import os
import sys
import time
import argparse
import collections

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from markdownify import markdownify as md


class QuoraCrawler:

    def __init__(self, args):
        self.args = args
        os.makedirs(args.save_root_dir, exist_ok=True)

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__

    def run_crawl(self):
        assert hasattr(self.args, "task") and isinstance(self.args.task, str)
        if self.args.task == "set_seed_topic_list":
            self.set_seed_topic_list()
        elif self.args.task == "crawl_topic_links":
            self.crawl_topic_links()
        elif self.args.task == "crawl_question_links":
            self.crawl_question_links()
        elif self.args.task == "crawl_qa_data":
            self.crawl_qa_data()
        else:
            raise ValueError(f"Error args.task == {self.args.task}")

    def set_seed_topic_list(self):
        """
        Step 1. set a list of topics, start from https://www.quora.com/topic/xxx
        """
        if self.args.verbose:
            print("FUNCTION: set_seed_topic_list...")

        seed_topic_list = [
            "Mathematics", "Physics", "Calculus", "Philosophy", "Algebra", "Thinking", "Prophecies",
            "Technology", "Movies", "Health", "Food", "Science", "Music", "Books", "Sports",
            "Visiting-and-Travel-1", "Fashion-and-Style-1", "Lifestyle", "Politics", "The-Arts",
            "Life-and-Living-2", "Litigation-and-Lawsuits", "Child-Development", "Writing-Advice",
            "ChatGPT", "Computer-Programming", "Fun", "Cities-and-Metropolitan-Areas", "Nature",
            "Olympic-Games", "American-Football", "Association-Football-1", "National-Basketball-Association-NBA-1",
            "Basketball", "Emotions", "Computers", "Computer-Science", "Chemistry", "Geology", "History",
            "Scientists", "Language", "English-language", "Physical-Education", "Teachers", "Colleges-and-Universities",
            "The-High-School-Experience-1", "Elementary-School-and-Elementary-Schools", "Education", "The-Environment",
            "Climate-Change", "Weather", "Spacetime", "The-Universe", "Astronomy", "Astrophysics", "Cosmology",
            "Gravity", "General-Relativity", "Relativity-physics", "Time-physics",
            "Artificial-Intelligence", "Intelligence", "Machine-Learning", "Deep-Learning", "Data-Science",
            "Algorithms",
            "Statistics-academic-discipline", "Probability-statistics-1", "Linguistics",
            "The-United-States-of-America", "China", "Japan", "Canada",
        ]  # 74 seed topics
        print(f"len(seed_topic_list): {len(seed_topic_list)}")

        with open(self.args.seed_topic_list_filepath, encoding="utf-8", mode="w") as fp_seed_topic_list:
            fp_seed_topic_list.writelines([self.args.url_topic + st + "\n" for st in seed_topic_list])

    def crawl_topic_links(self):
        """
        Step 2. get as many topic links as possible
        """
        if self.args.verbose:
            print("FUNCTION: crawl_topic_links...")

        len_ut = len(self.args.url_topic)
        assert os.path.isfile(self.args.seed_topic_list_filepath), \
            "Please run: `python quora_crawler.py --task set_seed_topic_list`"
        with open(self.args.seed_topic_list_filepath, encoding="utf-8", mode="r") as fp_seed_topic_list:
            seed_topic_list = fp_seed_topic_list.readlines()
            seed_topic_list = [st.strip() for st in seed_topic_list if st[:len_ut] == self.args.url_topic]

        if os.path.isfile(self.args.topic_list_visited_filepath):
            with open(self.args.topic_list_visited_filepath, encoding="utf-8", mode="r") as fp_topic_list_visited:
                topic_list_visited = fp_topic_list_visited.readlines()
                topic_list_visited = [tv.strip() for tv in topic_list_visited if tv[:len_ut] == self.args.url_topic]
        else:
            command = f"touch {self.args.topic_list_visited_filepath}"
            print(f"command: {command}")
            os.system(command)
            topic_list_visited = []

        if os.path.isfile(self.args.topic_list_to_visit_filepath):
            with open(self.args.topic_list_to_visit_filepath, encoding="utf-8", mode="r") as fp_topic_list_to_visit:
                topic_list_to_visit = fp_topic_list_to_visit.readlines()
                topic_list_to_visit = [t.strip() for t in topic_list_to_visit if t[:len_ut] == self.args.url_topic]
        else:
            command = f"touch {self.args.topic_list_to_visit_filepath}"
            print(f"command: {command}")
            os.system(command)
            topic_list_to_visit = []

        if len(topic_list_to_visit) > 0:  # resume crawling
            print(">>> resume crawling")
            url_queue = topic_list_to_visit
            url_queue = collections.deque(url_queue)  # BFS to-be-visited node queue
            url_visited = set(topic_list_visited)  # BFS visited node set
        else:  # start crawling from the hard-coded seed topics
            print(">>> start crawling from the hard-coded seed topics")
            url_queue = seed_topic_list
            url_queue = collections.deque(url_queue)  # BFS to-be-visited node queue
            url_visited = set()  # BFS visited node set

        if os.path.isfile(self.args.topic_list_filepath):
            with open(self.args.topic_list_filepath, encoding="utf-8", mode="r") as fp_topic_list:
                topic_list = fp_topic_list.readlines()
                topic_list = [t.strip() for t in topic_list if t[:len_ut] == self.args.url_topic]
        else:
            command = f"touch {self.args.topic_list_filepath}"
            print(f"command: {command}")
            os.system(command)
            topic_list = []
        topic_saved = set(topic_list)  # saved urls
        topic_saved_cnt = len(topic_saved)
        print(f"init topic_saved_cnt: {topic_saved_cnt}")

        # open the browser
        options = webdriver.ChromeOptions()
        options.binary_location = self.args.chrome_filepath
        options.add_experimental_option("extensionLoadTimeout", 60000)
        browser = webdriver.Chrome(options=options)

        # BFS, visit all seed topics and their related topics
        cur_loop = 0
        write_gap = 100
        while len(url_queue) > 0:
            cur_url = url_queue.popleft()
            if cur_url not in topic_saved:  # add as many as possible into topic_saved
                topic_saved.add(cur_url)

            if cur_url in url_visited:
                continue
            else:
                url_visited.add(cur_url)

            browser.get(cur_url)
            time.sleep(0.5)

            # fetch the content of the whole page and parse it using BeautifulSoup
            html_source = browser.page_source
            soup = BeautifulSoup(html_source, "html.parser")

            q_related_link = soup.find_all(attrs={"class": "puppeteer_test_link"})
            q_related_link = [link.attrs["href"] for link in q_related_link]
            q_related_link = [link for link in q_related_link if link[:len_ut] == self.args.url_topic]

            for link in q_related_link:
                if link not in topic_saved:  # add as many as possible into topic_saved
                    topic_saved.add(link)
                if link not in url_visited:
                    url_queue.append(link)  # add new topic links into the BFS queue

            cur_loop += 1
            if cur_loop % write_gap == 0:
                # rewrite BFS files
                print(f">>> Rewrite BFS files: \t len(url_visited): {len(url_visited)}; "
                      f"\t len(url_queue): {len(url_queue)}; \t len(topic_saved): {len(topic_saved)}")
                with open(self.args.topic_list_visited_filepath, encoding="utf-8", mode="w") as fp_topic_list_visited:
                    url_visited_write = list(url_visited)
                    url_visited_write.sort()
                    fp_topic_list_visited.writelines(([u + "\n" for u in url_visited_write]))

                with open(self.args.topic_list_to_visit_filepath, encoding="utf-8", mode="w") as fp_topic_list_to_visit:
                    url_queue_write = list(set(url_queue))
                    url_queue_write.sort()
                    fp_topic_list_to_visit.writelines(([u + "\n" for u in url_queue_write]))
                    url_queue = collections.deque(url_queue_write)

                with open(self.args.topic_list_filepath, encoding="utf-8", mode="w") as fp_topic_list:
                    topic_saved_write = list(topic_saved)
                    topic_saved_write.sort()
                    fp_topic_list.writelines(([u + "\n" for u in topic_saved_write]))

                # restart the browser to avoid TimeOutError
                browser.quit()
                time.sleep(1.0)
                browser = webdriver.Chrome(options=options)
                time.sleep(1.0)

        print(f">>> *** End ***: \t len(url_visited): {len(url_visited)}; "
              f"\t len(url_queue): {len(url_queue)}; \t len(topic_saved): {len(topic_saved)}")

    def crawl_question_links(self):
        """
        Step 3. for each topic, get all question links

        Time Consumption: about 250-300 min for crawling all question links from 1000 topic links
        """
        if self.args.verbose:
            print("FUNCTION: crawl_question_links...")

        timer_start = time.time()

        tql = "./crawler/topic_question_links/"
        os.makedirs(tql, exist_ok=True)

        len_ut = len(self.args.url_topic)
        assert os.path.isfile(self.args.topic_list_filepath), \
            "Please run: `python quora_crawler.py --task crawl_topic_links`"
        with open(self.args.topic_list_filepath, encoding="utf-8", mode="r") as fp_topic_list:
            topic_list = fp_topic_list.readlines()
            topic_list = [t.strip() for t in topic_list if t[:len_ut] == self.args.url_topic]

        assert hasattr(self.args, "split_start") and isinstance(self.args.split_start, int)
        assert hasattr(self.args, "split_end") and isinstance(self.args.split_end, int)
        ss, se = self.args.split_start, self.args.split_end
        assert 0 <= ss and (se == -1 or se >= ss)

        filepath_done_topic_list = os.path.join("./crawler/", f"done_topic_list_{ss}_{se}.txt")
        if os.path.isfile(filepath_done_topic_list):
            with open(filepath_done_topic_list, encoding="utf-8", mode="r") as fp_done_topic_list:
                done_topic_list = fp_done_topic_list.readlines()
                done_topic_list = [t.strip() for t in done_topic_list if t[:len_ut] == self.args.url_topic]
        else:
            command = f"touch {filepath_done_topic_list}"
            print(f"command: {command}")
            os.system(command)
            done_topic_list = []
        done_topic_set = set(done_topic_list)

        # open the browser
        options = webdriver.ChromeOptions()
        options.binary_location = self.args.chrome_filepath
        options.add_experimental_option("extensionLoadTimeout", 60000)
        browser = webdriver.Chrome(options=options)

        topic_list.sort()
        # set the current data_split
        if se == -1:
            topic_list = topic_list[ss:]
            print(f"The current interval: topic_list[{ss}:]")
        else:
            topic_list = topic_list[ss: (se + 1)]
            print(f"The current interval: topic_list[{ss}: {se + 1}]")

        restart_browser_gap = 100
        total_topics = len(topic_list)
        for idx, cur_topic_url in enumerate(topic_list):
            if cur_topic_url in done_topic_set:
                continue

            topic_name = cur_topic_url.split("/")[-1]

            browser.get(cur_topic_url)
            # time.sleep(1.0)
            time.sleep(0.5)

            # simulate scrolling until nothing changes
            cur_page = browser.page_source
            prev_page = ""
            while prev_page != cur_page:
                time.sleep(2.0)
                prev_page = cur_page
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                cur_page = browser.page_source

            # fetch contents of the whole page
            html_source = browser.page_source

            soup = BeautifulSoup(html_source, "html.parser")
            q_link = soup.find_all(name="a", attrs={"class": "puppeteer_test_link"})
            q_link_str = [link.attrs["href"] for link in q_link]

            profile_list = []  # questioner
            q_link_list = []
            len_up = len(self.args.url_profile)
            cur_index = 0
            max_index = len(q_link_str) - 2
            while cur_index < max_index:  # pattern: (profile, profile, question_link) * N
                cur_link = q_link_str[cur_index]
                if cur_link[:len_up] == self.args.url_profile:
                    profile_list.append(cur_link)
                    q_link_list.append(q_link_str[cur_index + 2])
                    cur_index += 3
                else:
                    cur_index += 1

            if len(q_link_list) > 0:
                save_dir = os.path.join(tql, topic_name)
                os.makedirs(save_dir, exist_ok=True)
                with open(os.path.join(save_dir, "profile_list.txt"), encoding="utf-8", mode="w") as fp_profile_list:
                    fp_profile_list.writelines([profile + "\n" for profile in profile_list])
                with open(os.path.join(save_dir, "q_link_list.txt"), encoding="utf-8", mode="w") as fp_q_link_list:
                    fp_q_link_list.writelines([q_link + "\n" for q_link in q_link_list])

            done_topic_set.add(cur_topic_url)
            done_topic_list = list(done_topic_set)
            done_topic_list.sort()
            timer_run = time.time() - timer_start
            print(f">>> [{idx}/{total_topics}]; \t #Done_Topics: {len(done_topic_list)};"
                  f"\t Cur Topic: {topic_name}; \t #Question of Cur Topic: {len(q_link_list)}; \t " +
                  "Cur Running Time: %.1f sec (%.1f min)" % (timer_run, timer_run / 60))
            with open(filepath_done_topic_list, encoding="utf-8", mode="w") as fp_done_topic_list:
                fp_done_topic_list.writelines([done_topic + "\n" for done_topic in done_topic_list])

            if idx % restart_browser_gap == 1:  # restart the browser to avoid TimeOutError
                browser.quit()
                time.sleep(1.0)
                browser = webdriver.Chrome(options=options)
                time.sleep(1.0)

    def crawl_qa_data(self):
        """
        Step 4. for each question, get all expanded answers
        Step 5. postprocessing: unify the data format: "human: question <sep> assistant: answer"

        Time Consumption: about 500 min for crawling all Q/A content from all questions of 50 topics
        Normally, each topic has roughly 80-90 question links.
        """
        if self.args.verbose:
            print("FUNCTION: crawl_qa_data...")

        timer_start = time.time()

        len_ut = len(self.args.url_topic)
        len_up = len(self.args.url_profile)
        len_uq = len(self.args.url_quora)

        tqa = "./crawler/topic_qa_data/"
        tql = "./crawler/topic_question_links/"
        topic_list = os.listdir(tql)

        assert hasattr(self.args, "split_start") and isinstance(self.args.split_start, int)
        assert hasattr(self.args, "split_end") and isinstance(self.args.split_end, int)
        ss, se = self.args.split_start, self.args.split_end
        assert 0 <= ss and (se == -1 or se >= ss)

        filepath_done_topic_qa_list = os.path.join("./crawler/", f"done_topic_qa_list_{ss}_{se}.txt")
        if os.path.isfile(filepath_done_topic_qa_list):
            with open(filepath_done_topic_qa_list, encoding="utf-8", mode="r") as fp_done_topic_qa_list:
                done_topic_qa_list = fp_done_topic_qa_list.readlines()
                done_topic_qa_list = [t.strip() for t in done_topic_qa_list if t[:len_ut] == self.args.url_topic]
        else:
            command = f"touch {filepath_done_topic_qa_list}"
            print(f"command: {command}")
            os.system(command)
            done_topic_qa_list = []
        done_topic_qa_set = set(done_topic_qa_list)

        skip_topic_list = [
            "1-Motorcycle-Clubs"
        ]
        skip_topic_list = [self.args.url_topic + t for t in skip_topic_list]
        skip_topic_set = set(skip_topic_list)

        # open the browser
        options = webdriver.ChromeOptions()
        options.binary_location = self.args.chrome_filepath
        options.add_experimental_option("extensionLoadTimeout", 60000)
        browser = webdriver.Chrome(options=options)

        url_counter = 0
        restart_browser_gap = 30
        print_done_q_gap = 10
        MAX_Scroll = 30

        topic_list.sort()
        # set the current data_split
        if se == -1:
            topic_list = topic_list[ss:]
            print(f"The current interval: topic_list[{ss}:]")
        else:
            topic_list = topic_list[ss: (se + 1)]
            print(f"The current interval: topic_list[{ss}: {se + 1}]")

        topic_name_list = topic_list[:]
        topic_list = [self.args.url_topic + t for t in topic_list]
        total_topics = len(topic_list)
        for topic_idx, cur_topic_url in enumerate(topic_list):
            if cur_topic_url in done_topic_qa_set:
                continue
            if cur_topic_url in skip_topic_set:
                print(f">>> skip topic: {cur_topic_url}")
                continue

            topic_name = topic_name_list[topic_idx]
            # cur_question_links = []
            print(f">>> *** Start Topic [{topic_idx}/{total_topics}]; \t Cur Topic: {topic_name}")

            cur_dir = os.path.join(tql, topic_name)
            profile_list_filepath = os.path.join(cur_dir, "profile_list.txt")
            q_link_list_filepath = os.path.join(cur_dir, "q_link_list.txt")
            if not os.path.exists(profile_list_filepath) or not os.path.exists(q_link_list_filepath):
                continue

            with open(profile_list_filepath, encoding="utf-8", mode="r") as fp:
                profile_list = fp.readlines()
                profile_list = [p.strip() for p in profile_list if p[:len_up] == self.args.url_profile]
            with open(q_link_list_filepath, encoding="utf-8", mode="r") as fp:
                q_link_list = fp.readlines()
                q_link_list = [q.strip() for q in q_link_list if q[:len_uq] == self.args.url_quora]

            if len(profile_list) != len(q_link_list):
                print(f"List length unequal: {topic_name}; \t profile {len(profile_list)} != q_link {len(q_link_list)}")
                continue

            save_dir = os.path.join(tqa, topic_name)
            os.makedirs(save_dir, exist_ok=True)

            total_questions = len(q_link_list)
            q_idx = 0
            for profile_link, q_link in zip(profile_list, q_link_list):
                browser.get(q_link)
                time.sleep(1.0)
                q_idx += 1
                url_counter += 1

                # simulate scrolling until nothing changes
                cur_page = browser.page_source
                prev_page = ""

                scroll_cnt = 0
                while prev_page != cur_page and scroll_cnt < MAX_Scroll:
                    # time.sleep(0.5)
                    # time.sleep(1.0)
                    time.sleep(2.0)
                    prev_page = cur_page
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    cur_page = browser.page_source
                    if len(cur_page) <= len(prev_page):
                        break
                    scroll_cnt += 1
                time.sleep(2.0)

                # simulate clicking "(more)" to expand all answers
                elements = browser.find_elements(By.CLASS_NAME, "puppeteer_test_read_more_button")
                elements = elements[1:]  # skip the first one of the old-version Quora to avoid AI bot checking
                elements += browser.find_elements(By.CLASS_NAME, "qt_read_more")
                elements = list(set(elements))
                for element in elements:
                    browser.execute_script("arguments[0].click();", element)

                # fetch contents of the whole page
                html_source = browser.page_source

                soup = BeautifulSoup(html_source, "html.parser")
                q_question = soup.find_all(attrs={"class": "puppeteer_test_question_title"})
                q_answer = soup.find_all(attrs={"class": "puppeteer_test_answer_content"})

                q_question_raw_html = [str(question).strip() for question in q_question]
                q_answer_raw_html = [str(answer).strip() for answer in q_answer]

                q_question_markdown = [md(question).strip().replace("\n", "<br>") for question in q_question_raw_html]
                q_answer_markdown = [md(answer).strip().replace("\n", "<br>") for answer in q_answer_raw_html]

                if len(q_question_markdown) > 0 and len(q_answer_markdown) > 0:
                    cur_question = q_question_markdown[0]
                    save_fp_to_train = self.create_file(os.path.join(save_dir, "qa_data_list_to_train.txt"))
                    with open(save_fp_to_train, encoding="utf-8", mode="a+") as fp:
                        # human: question <sep> assistant: answer
                        fp.writelines(["human: " + cur_question + " <sep> assistant: " + ans + "\n"
                                       for ans in q_answer_markdown])

                if self.args.save_all:
                    q_question_text = [question.text.strip() for question in q_question]
                    q_answer_text = [answer.text.strip() for answer in q_answer]

                    if len(q_question_text) > 0 and len(q_answer_text) > 0:
                        cur_question = q_question_text[0]
                        save_fp_pure_text = self.create_file(os.path.join(save_dir, "qa_data_list_pure_text.txt"))
                        with open(save_fp_pure_text, encoding="utf-8", mode="a+") as fp:
                            fp.writelines([topic_name + "\t" + profile_link[len_up:] + "\t" + q_link + "\t" +
                                           cur_question + "\t" + ans + "\n" for ans in q_answer_text])

                    if len(q_question_raw_html) > 0 and len(q_answer_raw_html) > 0:
                        cur_question = q_question_raw_html[0]
                        save_fp_raw_html = self.create_file(os.path.join(save_dir, "qa_data_list_raw_html.txt"))
                        with open(save_fp_raw_html, encoding="utf-8", mode="a+") as fp:
                            fp.writelines([topic_name + "\t" + profile_link[len_up:] + "\t" + q_link + "\t" +
                                           cur_question + "\t" + ans + "\n" for ans in q_answer_raw_html])

                    if len(q_question_markdown) > 0 and len(q_answer_markdown) > 0:
                        cur_question = q_question_markdown[0]
                        save_fp_markdown = self.create_file(os.path.join(save_dir, "qa_data_list_markdown.txt"))
                        with open(save_fp_markdown, encoding="utf-8", mode="a+") as fp:
                            fp.writelines([topic_name + "\t" + profile_link[len_up:] + "\t" + q_link + "\t" +
                                           cur_question + "\t" + ans + "\n" for ans in q_answer_markdown])

                if q_idx % print_done_q_gap == 0:
                    timer_run = time.time() - timer_start
                    print(f">>> Topic [{topic_idx}/{total_topics}] \t >>> Question [{q_idx}/{total_questions}]; "
                          f"\t Cur Topic: {topic_name}; \t " + "Cur Running Time: %.1f sec (%.1f min)" %
                          (timer_run, timer_run / 60))

                # restart the browser to avoid TimeOutError
                if url_counter % restart_browser_gap == 0:
                    browser.quit()
                    time.sleep(1.0)
                    browser = webdriver.Chrome(options=options)
                    time.sleep(1.0)

            done_topic_qa_set.add(cur_topic_url)
            done_topic_qa_list = list(done_topic_qa_set)
            done_topic_qa_list.sort()
            timer_run = time.time() - timer_start
            print(f">>> Topic [{topic_idx}/{total_topics}]; \t #Done_Topics: {len(done_topic_qa_list)};"
                  f"\t Cur Topic: {topic_name}; \t #Question of Cur Topic: {len(q_link_list)}; \t " +
                  "Cur Running Time: %.1f sec (%.1f min)" % (timer_run, timer_run / 60))
            with open(filepath_done_topic_qa_list, encoding="utf-8", mode="w") as fp_done_topic_qa_list:
                fp_done_topic_qa_list.writelines([done_tqa + "\n" for done_tqa in done_topic_qa_list])

    @staticmethod
    def create_file(save_fp: str):
        if os.path.isfile(save_fp):
            os.remove(save_fp)
        os.system(f"touch {save_fp}")
        return save_fp


def run_crawl():
    start = time.time()

    parser = argparse.ArgumentParser(description="Quora Crawler")

    parser.add_argument("--task", type=str, default="crawl_topic_qa_data",
                        help="set_seed_topic_list OR crawl_topic_links OR crawl_question_links OR crawl_qa_data")

    parser.add_argument("--verbose", action="store_true", default=False,
                        help="Turn on the verbose mode")
    parser.add_argument("--save_all", action="store_true", default=False,
                        help="Save all types of QA data (raw_html + markdownify + pure_text)")

    parser.add_argument("--split_start", type=int, default=0,
                        help="The start index for the current data_split")
    parser.add_argument("--split_end", type=int, default=-1,
                        help="The end index for the current data_split")

    parser.add_argument("--url_quora", type=str, default="https://www.quora.com/",
                        help="url_quora")
    parser.add_argument("--url_topic", type=str, default="https://www.quora.com/topic/",
                        help="url_topic")
    parser.add_argument("--url_profile", type=str, default="https://www.quora.com/profile/",
                        help="url_profile")

    parser.add_argument("--chromedriver", type=str, default="chromedriver",
                        help="chromedriver")
    parser.add_argument("--chrome_filepath", type=str,
                        default="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                        help="chrome_filepath of MacOS")

    parser.add_argument("--save_root_dir", type=str, default="./crawler/",
                        help="save_root_dir")
    parser.add_argument("--seed_topic_list_filepath", type=str, default="./crawler/topic_list_seed.txt",
                        help="seed_topic_list_filepath")
    parser.add_argument("--topic_list_visited_filepath", type=str, default="./crawler/topic_list_visited.txt",
                        help="topic_list_visited_filepath")
    parser.add_argument("--topic_list_to_visit_filepath", type=str, default="./crawler/topic_list_to_visit.txt",
                        help="topic_list_to_visit_filepath")
    parser.add_argument("--topic_list_filepath", type=str, default="./crawler/topic_list.txt",
                        help="topic_list_filepath")

    args = parser.parse_args()
    print(args)

    os.environ["webdriver.chrome.driver"] = args.chromedriver

    qc = QuoraCrawler(args=args)
    qc.run_crawl()

    end = time.time()
    print("Total Running Time: %.1f sec (%.1f min)" % (end - start, (end - start) / 60))

    return 0


if __name__ == "__main__":
    sys.exit(run_crawl())
