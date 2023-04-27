# QuoraCrawler

QuoraCrawler using selenium, BeautifulSoup, and markdownify

## Environment

```bash
git clone https://github.com/YuweiYin/QuoraCrawler
cd QuoraCrawler

conda create -n qc python=3.9
conda activate qc

pip install -r requirements.txt
```

## Step 1

- Set a list of topics, start from https://www.quora.com/topic/xxx
- Seed resource: [Quora Space](https://www.quora.com/spaces), [Quora Statistics](https://www.demandsage.com/quora-statistics/)

```bash
python quora_crawler.py --verbose --task set_seed_topic_list
```

## Step 2: Get as many topic links as possible

```bash
# You can stop and resume running the process at any time.
python quora_crawler.py --verbose --task crawl_topic_links
```

## Step 3: For each topic, get all question links

```bash
# You can stop and resume running the process at any time.
python quora_crawler.py --verbose --task crawl_question_links
```

## Step 4: For each question, get all expanded answers

- postprocessing: unify the data format: `human: question <sep> assistant: answer`

```bash
# You can stop and resume running the process at any time.
python quora_crawler.py --verbose --task crawl_qa_data
```

---

- `--save_all`: Save all types of QA data (raw_html + markdownify + pure_text)

```bash
# You can stop and resume running the process at any time.
python quora_crawler.py --verbose --task crawl_qa_data --save_all
```

---

- `--split_start` / `--split_end`: The start/end index for the current data_split

```bash
# You can stop and resume running the process at any time.
python quora_crawler.py --verbose --task crawl_qa_data --split_start 1000 --split_end 2000
```

---
