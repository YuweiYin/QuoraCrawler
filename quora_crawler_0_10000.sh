#!/bin/bash

echo "Start running all quora_crawler... (from 0 to 10000)"
echo -e "\n\n\n"

LOG_DIR="./log"
mkdir -p ${LOG_DIR}
echo "LOG_DIR: ${LOG_DIR}"

#conda activate qc
#pip install -r requirements.txt

CHROME_FP="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # MacOS
#CHROME_FP="/usr/bin/google-chrome"  # Linux (or "/opt/google/chrome/google-chrome")

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 0 --split_end 500 > "${LOG_DIR}/0_500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 501 --split_end 1000 > "${LOG_DIR}/501_1000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 1001 --split_end 1500 > "${LOG_DIR}/1001_1500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 1501 --split_end 2000 > "${LOG_DIR}/1501_2000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 2001 --split_end 2500 > "${LOG_DIR}/2001_2500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 2501 --split_end 3000 > "${LOG_DIR}/2501_3000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 3001 --split_end 3500 > "${LOG_DIR}/3001_3500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 3501 --split_end 4000 > "${LOG_DIR}/3501_4000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 4001 --split_end 4500 > "${LOG_DIR}/4001_4500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 4501 --split_end 5000 > "${LOG_DIR}/4501_5000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 5001 --split_end 5500 > "${LOG_DIR}/5001_5500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 5501 --split_end 6000 > "${LOG_DIR}/5501_6000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 6001 --split_end 6500 > "${LOG_DIR}/6001_6500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 6501 --split_end 7000 > "${LOG_DIR}/6501_7000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 7001 --split_end 7500 > "${LOG_DIR}/7001_7500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 7501 --split_end 8000 > "${LOG_DIR}/7501_8000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 8001 --split_end 8500 > "${LOG_DIR}/8001_8500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 8501 --split_end 9000 > "${LOG_DIR}/8501_9000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 9001 --split_end 9500 > "${LOG_DIR}/9001_9500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 9501 --split_end 10000 > "${LOG_DIR}/9501_10000.log" 2>&1 &
