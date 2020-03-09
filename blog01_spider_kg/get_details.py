# coding: utf-8
import urllib.request as urllib2
import json

#设置headers
headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"

#读取文件-读取json信息并将json格式数据转换为字典
f = open('films.csv', 'r', encoding='utf-8')
films = []
for line in f.readlines():
    #print(line)
    print(line.strip('\n'))
    line = json.loads(line.strip('\n'))
    films.append(line)
f.close()

#遍历每部电影films的实体并获取其他实体
#获取 characters人物, planets星球, starships飞船, vehicles装备, species种族
targets = ['characters', 'planets', 'starships', 'vehicles', 'species']

for target in targets:
    print(target)
    #循环获取五类数据并存储至文件
    fw = open('film_' + target + '.csv', 'w')
    data = []
    #获取7部电影信息的实体名称
    for item in films:  
        tmp = item[target]  #实体对应的链接
        print(tmp)
        for t in tmp:
            if t in data: #如果实体已经存在则跳过 比如某部电影人物另一部也出现了
                continue
            else:
                data.append(t)
            
            #循环请求直到成功 防止网络延迟
            while 1:
                try:
                    print(t)
                    request = urllib2.Request(url=t, headers=headers)
                    response = urllib2.urlopen(request)
                    result = response.read().decode('utf-8')
                except Exception as e:
                    continue #请求失败循环继续
                else:
                    fw.write(result+"\n")
                    break #请求成功跳出循环
                finally:
                    pass
                
    #查看七部电影含这种实体多少个
    print(str(len(data)), target)
    fw.close()

print("success")
