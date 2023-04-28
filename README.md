# QuoraCrawler

QuoraCrawler using selenium, BeautifulSoup, and markdownify

## Environment

### Python

```bash
git clone https://github.com/YuweiYin/QuoraCrawler
cd QuoraCrawler

conda create -n qc python=3.9
conda activate qc

pip install -r requirements.txt
```

OR

```bash
bash set_env_python.sh
```

### Chrome for Linux (Ubuntu)

```bash
bash set_env_chrome.sh
```

---

**Note**: You can skip Step 1-3 by rename the folder `crawler_example` as `crawler`, download `topic_question_links.zip` from [Google Drive](https://drive.google.com/drive/folders/1A5bQdNwSVXlJNHWnC4StDQ9dJF2kCXJu?usp=sharing), put it into the `crawler/` folder, and unzip it. After that, you can run scripts in Step 4 to crawl Quora question/answer pairs.

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
python quora_crawler.py --verbose --task crawl_question_links --split_start 0 --split_end 10000
python quora_crawler.py --verbose --task crawl_qa_data --split_start 1000 --split_end 2000
```

---

# RedditCrawler

```bash
git clone https://github.com/microsoft/DialoGPT
cd DialoGPT

# modify LSP-linux.yml beforehand if some packages are not compatible
conda env create -f LSP-linux.yml -n LSP
conda activate LSP
pip install -r requirements.txt

git clone https://github.com/NVIDIA/apex
cd apex
git reset --hard 3d01e4a0a188cc8df54bc6e44cf5eb40ff6b4cc5
pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" .

cd ..
python demo.py --data full

python reddit_format.py --verbose
```
