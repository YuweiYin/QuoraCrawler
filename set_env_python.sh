#!/bin/bash

echo "Set Python environment..."
echo -e "\n\n\n"

#git clone https://github.com/YuweiYin/QuoraCrawler
#cd QuoraCrawler

conda create -n qc python=3.9
conda activate qc

pip install -r requirements.txt
