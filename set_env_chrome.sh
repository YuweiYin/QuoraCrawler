#!/bin/bash

echo "Set Chrome environment..."
echo -e "\n\n\n"

# Linux Ubuntu

sudo apt update
sudo apt upgrade

sudo apt install wget
wget --version

wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f

google-chrome --version
google-chrome-stable --version
# Google Chrome 112.0.5615.165

# If you are using Chrome version 113, please download ChromeDriver [113.0.5672.24](https://chromedriver.storage.googleapis.com/index.html?path=113.0.5672.24/)
# If you are using Chrome version 112, please download ChromeDriver [112.0.5615.49](https://chromedriver.storage.googleapis.com/index.html?path=112.0.5615.49/)
# If you are using Chrome version 111, please download ChromeDriver [111.0.5563.64](https://chromedriver.storage.googleapis.com/index.html?path=111.0.5563.64/)

wget https://chromedriver.storage.googleapis.com/112.0.5615.49/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/
sudo chmod +x /usr/bin/chromedriver
chromedriver --version
# ChromeDriver 112.0.5615.49
