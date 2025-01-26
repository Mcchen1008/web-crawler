#!/bin/bash

# 尝试安装requests库
echo "开始安装 requests 库..."
pip install requests
if [ $? -eq 0 ]; then
    echo "requests 库安装成功"
else
    echo "requests 库安装失败"
fi

# 尝试安装BeautifulSoup4库
echo "开始安装 BeautifulSoup4 库..."
pip install beautifulsoup4
if [ $? -eq 0 ]; then
    echo "BeautifulSoup4 库安装成功"
else
    echo "BeautifulSoup4 库安装失败"
fi
