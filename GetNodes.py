"""
某人的小脚本
目前支持的网站：
    1、v2raya.com
    2、clashnode.cc
这两个基本上就涵盖了网上能找到的绝大多数节点（非github)
"""

from base64 import b64decode
from bs4 import BeautifulSoup
import requests
import time
import sys
import re


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

input_file = "urls.txt"
output_file = "README.md"
targets = []


# Get time
lt = time.localtime(time.time())
update_time = "## Update Time: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "\n\n```"


# Get share urls
# Supported: clashnode.cc, v2raya.com
print("Get share urls...")
# 1、freeclashnode.com
# https://node.clashnode.cc/uploads/2025/01/0-20250121.txt
for i in range(4):
    tmp = 'https://node.clashnode.cc/uploads/{0}/0{1}/{3}-{0}0{1}{2}.txt'.format(lt.tm_year, lt.tm_mon, lt.tm_mday, i)
    targets.append(tmp)

#2、v2raya.com
web_url = 'https://v2raya.net/free-nodes/free-v2ray-node-subscriptions.html'
response = requests.get(web_url, headers = headers).content
soup = BeautifulSoup(response, 'html.parser')
# soup = BeautifulSoup(open("untitled.html", encoding='utf-8'), 'lxml')
for i in soup.find_all(string=re.compile('https://console.stableproxy.top/api/v1/client/subscribe')):
    targets.append(i)


# Input share urls
'''
with open(input_file, "r", encoding="utf-8") as f:
    oglt = f.read()

oglt = oglt.strip()
flag = False
target = ''
for i in range(len(oglt)-1):
    if oglt[i] == oglt[i+1] == '\n' and not flag:
        target = target + oglt[i]
        flag = True
    elif oglt[i] == '\n' and oglt[i+1] != '\n' and flag:
        flag = False
    elif not flag:
        target += oglt[i]

targets = target.split('\n')
'''


# Get share content
print("Get share content...")
urls = ""
j = 0
for i in targets:
    print(j, j / len(targets) * 100)
    j += 1

    content = requests.get(i, headers=headers).content.decode()
    
    if content.find(':') != -1:
        urls += content
        continue

    # Padding
    pad_num = len(content) % 4
    content = content[:len(content)-pad_num]
    
    # Decoding
    add_ctt = b64decode(content).decode('unicode_escape')

    urls += add_ctt

urls = re.sub('\n+', '\n', urls)

with open(output_file, "w", encoding='utf-8') as f:
    f.write(update_time + urls + "\n```")

input('Enter to exit...')