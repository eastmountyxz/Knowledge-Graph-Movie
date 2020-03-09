# coding: utf-8
import urllib.request as urllib2

#定义数组存所有电影
films = []

#循环写入七部电影的链接《星球大战》
for x in range(1,8):
    films.append('https://swapi.co/api/films/'+str(x)+'/')
    
#定义headers 防止网站反扒 Window系统
headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"

#写入文件
with open('films.csv','w') as file:
    for item in films:
        print(item)
        #请求访问网站
        request = urllib2.Request(url=item, headers=headers)
        #url打开
        response = urllib2.urlopen(request)
        result = response.read().decode('utf-8')
        print(result)
        file.write(result+"\n")
