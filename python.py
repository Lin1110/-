import requests
from bs4 import BeautifulSoup
import re
import code

def code_what(url):
    from urllib import request
    from chardet import detect
    #读取网页内容
    data = request.urlopen(url).read()
    #chardet解析网页
    chardet1 = detect(data)
    return chardet1['encoding']

headers={
        'UserAgent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }

#网站的初始页码
url= ''
#apple = code_what(url)
for u in range(0,100000):  
    res=requests.get(url,headers=headers)
    res.encoding = "gbk"

    soup=BeautifulSoup(res.text,'html.parser')
    
    print('正在下载')
    print(soup.find_all('h1')[0].string)
    #print(soup.find_all("a"))
    #print(soup.find_all("a",text="下一章"))
    apple = soup.find_all("a",text="下一章")[0]["href"]
    #input()
    url='' + apple  
    text_100 = soup.get_text()
    #print(text)
    m = re.search('style3', text_100)
    n = re.search('style4', text_100)
    try:
        text_101 = text[m.span()[1]+3:n.span()[0]]
    except:
        text_101 = text_100
    ls1 = []
    flag = True
    count = 0
    for i in text_101:                
        if i == '\u3000':
            if flag:
                ls1.append('\n')
                flag = False
                continue
            else:
                flag = False
                continue
        ls1.append(i)
        flag = True
    
  
    ls3 = ''.join(ls1)
    #print(ls3)
    #print(text_101)
    ls3.encode('UTF-8')
    filename = 'write_data.txt'
    #print(ls3)
    
    with open(filename,'a',encoding='UTF-8') as f:
        f.write(ls3)
    print('下载完成'+str(u+1))
        


    

