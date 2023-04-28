#!/bin/bash

echo "Start running all quora_crawler... (from 10001 to 20000)"
echo -e "\n\n\n"

LOG_DIR="./log"
mkdir -p ${LOG_DIR}
echo "LOG_DIR: ${LOG_DIR}"

#conda activate qc
#pip install -r requirements.txt

CHROME_FP="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # MacOS
#CHROME_FP="/usr/bin/google-chrome"  # Linux (or "/opt/google/chrome/google-chrome")

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 10001 --split_end 10500 > "${LOG_DIR}/10001_10500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 10501 --split_end 11000 > "${LOG_DIR}/10501_11000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 11001 --split_end 11500 > "${LOG_DIR}/11001_11500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 11501 --split_end 12000 > "${LOG_DIR}/11501_12000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 12001 --split_end 12500 > "${LOG_DIR}/12001_12500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 12501 --split_end 13000 > "${LOG_DIR}/12501_13000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 13001 --split_end 13500 > "${LOG_DIR}/13001_13500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 13501 --split_end 14000 > "${LOG_DIR}/13501_14000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 14001 --split_end 14500 > "${LOG_DIR}/14001_14500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 14501 --split_end 15000 > "${LOG_DIR}/14501_15000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 15001 --split_end 15500 > "${LOG_DIR}/15001_15500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 15501 --split_end 16000 > "${LOG_DIR}/15501_16000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 16001 --split_end 16500 > "${LOG_DIR}/16001_16500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 16501 --split_end 17000 > "${LOG_DIR}/16501_17000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 17001 --split_end 17500 > "${LOG_DIR}/17001_17500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 17501 --split_end 18000 > "${LOG_DIR}/17501_18000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 18001 --split_end 18500 > "${LOG_DIR}/18001_18500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 18501 --split_end 19000 > "${LOG_DIR}/18501_19000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 19001 --split_end 19500 > "${LOG_DIR}/19001_19500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 19501 --split_end 20000 > "${LOG_DIR}/19501_20000.log" 2>&1 &
