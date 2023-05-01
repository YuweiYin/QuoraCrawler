#!/bin/bash

echo "Set Python environment..."
echo -e "\n\n\n"

# Miniconda 3: https://docs.conda.io/en/latest/miniconda.html
#wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
#bash Miniconda3-latest-Linux-x86_64.sh  # enter "yes"
#source ~/.bashrc

conda create -n qc python=3.9
conda activate qc

#git clone https://github.com/YuweiYin/QuoraCrawler
#cd QuoraCrawler

pip install -r requirements.txt
