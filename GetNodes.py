from base64 import b64decode
import requests


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

input_file = "urls.txt"
output_file = "index.html"

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

urls = ""
for i in targets:
    content = requests.get(i, headers=headers).content.decode()

    # print(content)
    
    if content.find(':') != -1:
        urls += content
        continue

    pad_num = len(content) % 4
    print(pad_num)
    content = content[:len(content)-pad_num]
    add_ctt = b64decode(content).decode()
    urls += add_ctt
    print(add_ctt)

with open(output_file, "w", encoding='utf-8') as f:
    f.write(urls)