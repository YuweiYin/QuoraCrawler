#!/bin/bash

echo "Start running all quora_crawler... (from 20001 to 30000)"
echo -e "\n\n\n"

LOG_DIR="./log"
mkdir -p ${LOG_DIR}
echo "LOG_DIR: ${LOG_DIR}"

#conda activate qc
#pip install -r requirements.txt

CHROME_FP="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # MacOS
#CHROME_FP="/usr/bin/google-chrome"  # Linux (or "/opt/google/chrome/google-chrome")

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 20001 --split_end 20500 > "${LOG_DIR}/20001_20500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 20501 --split_end 21000 > "${LOG_DIR}/20501_21000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 21001 --split_end 21500 > "${LOG_DIR}/21001_21500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 21501 --split_end 22000 > "${LOG_DIR}/21501_22000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 22001 --split_end 22500 > "${LOG_DIR}/22001_22500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 22501 --split_end 23000 > "${LOG_DIR}/22501_23000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 23001 --split_end 23500 > "${LOG_DIR}/23001_23500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 23501 --split_end 24000 > "${LOG_DIR}/23501_24000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 24001 --split_end 24500 > "${LOG_DIR}/24001_24500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 24501 --split_end 25000 > "${LOG_DIR}/24501_25000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 25001 --split_end 25500 > "${LOG_DIR}/25001_25500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 25501 --split_end 26000 > "${LOG_DIR}/25501_26000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 26001 --split_end 26500 > "${LOG_DIR}/26001_26500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 26501 --split_end 27000 > "${LOG_DIR}/26501_27000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 27001 --split_end 27500 > "${LOG_DIR}/27001_27500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 27501 --split_end 28000 > "${LOG_DIR}/27501_28000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 28001 --split_end 28500 > "${LOG_DIR}/28001_28500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 28501 --split_end 29000 > "${LOG_DIR}/28501_29000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 29001 --split_end 29500 > "${LOG_DIR}/29001_29500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 29501 --split_end 30000 > "${LOG_DIR}/29501_30000.log" 2>&1 &
