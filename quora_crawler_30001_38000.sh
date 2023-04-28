#!/bin/bash

echo "Start running all quora_crawler... (from 30001 to 38000)"
echo -e "\n\n\n"

LOG_DIR="./log"
mkdir -p ${LOG_DIR}
echo "LOG_DIR: ${LOG_DIR}"

#conda activate qc
#pip install -r requirements.txt

CHROME_FP="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # MacOS
#CHROME_FP="/usr/bin/google-chrome"  # Linux (or "/opt/google/chrome/google-chrome")

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 30001 --split_end 30500 > "${LOG_DIR}/30001_30500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 30501 --split_end 31000 > "${LOG_DIR}/30501_31000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 31001 --split_end 31500 > "${LOG_DIR}/31001_31500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 31501 --split_end 32000 > "${LOG_DIR}/31501_32000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 32001 --split_end 32500 > "${LOG_DIR}/32001_32500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 32501 --split_end 33000 > "${LOG_DIR}/32501_33000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 33001 --split_end 33500 > "${LOG_DIR}/33001_33500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 33501 --split_end 34000 > "${LOG_DIR}/33501_34000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 34001 --split_end 34500 > "${LOG_DIR}/34001_34500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 34501 --split_end 35000 > "${LOG_DIR}/34501_35000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 35001 --split_end 35500 > "${LOG_DIR}/35001_35500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 35501 --split_end 36000 > "${LOG_DIR}/35501_36000.log" 2>&1 &

nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 36001 --split_end 36500 > "${LOG_DIR}/36001_36500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 36501 --split_end 37000 > "${LOG_DIR}/36501_37000.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 37001 --split_end 37500 > "${LOG_DIR}/37001_37500.log" 2>&1 &
nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 37501 --split_end 38000 > "${LOG_DIR}/37501_38000.log" 2>&1 &

#nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 38001 --split_end 38500 > "${LOG_DIR}/38001_38500.log" 2>&1 &
#nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 38501 --split_end 39000 > "${LOG_DIR}/38501_39000.log" 2>&1 &
#nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 39001 --split_end 39500 > "${LOG_DIR}/39001_39500.log" 2>&1 &
#nohup python quora_crawler.py --verbose --chrome_filepath "${CHROME_FP}" --task "crawl_qa_data" --split_start 39501 --split_end 40000 > "${LOG_DIR}/39501_40000.log" 2>&1 &
