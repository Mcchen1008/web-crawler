# 用前准备
首先要安装requests和BeautifulSoup4
可以创建个sh脚本
```sheel
/bin/bash
echo "开始安装 requests 库..."
pip install requests
if [ $? -eq 0 ]; then
    echo "requests 库安装成功"
else
    echo "requests 库安装失败"
fi
echo "开始安装 BeautifulSoup4 库..."
pip install beautifulsoup4
if [ $? -eq 0 ]; then
    echo "BeautifulSoup4 库安装成功"
else
    echo "BeautifulSoup4 库安装失败"
fi
```
