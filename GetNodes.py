from base64 import b64decode
import requests


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

with open('urls.txt', "r", encoding="utf-8") as f:
    targets = f.read().split('\n')

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

with open("result.txt", "w", encoding='utf-8') as f:
    f.write(urls)