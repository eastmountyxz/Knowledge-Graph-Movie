# coding:utf8
import json

#获取所有节点的数据
data = {}

#读取电影数据
fr = open('films.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n')) #转换为字典
    data[tmp['title']] = tmp
    print(tmp['title'], tmp)
fr.close()

#读取人物数据
fr = open('film_characters.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    data[tmp['name']] = tmp
fr.close()

#读取星球数据
fr = open('film_planets.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    data[tmp['name']] = tmp
fr.close()

#读取飞船数据
fr = open('film_starships.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    data[tmp['name']] = tmp
fr.close()

#读取装备数据
fr = open('film_vehicles.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    data[tmp['name']] = tmp
fr.close()

#读取物种数据    
fr = open('film_species.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    data[tmp['name']] = tmp
fr.close()

#写文件
fw = open("all_data.json", "w")
fw.write(json.dumps(data))
fw.close()





