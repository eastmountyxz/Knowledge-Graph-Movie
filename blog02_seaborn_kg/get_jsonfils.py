import json

#读取数据
fr = open("films.csv", "r")

#写文件
fw = open("stat_basic.csv", "w")
fw.write('title,key,value'+'\n')

#统计每部电影中出现各类实体多少个
for line in fr:
    #tmp['title']获取电影名称
    tmp = json.loads(line.strip('\n'))
    fw.write(tmp['title'] + ',' + 'characters' + ',' + str(len(tmp['characters'])) + '\n')
    fw.write(tmp['title'] + ',' + 'planets' + ',' + str(len(tmp['planets'])) + '\n')
    fw.write(tmp['title'] + ',' + 'starships' + ',' + str(len(tmp['starships'])) + '\n')
    fw.write(tmp['title'] + ',' + 'vehicles' + ',' + str(len(tmp['vehicles'])) + '\n')
    fw.write(tmp['title'] + ',' + 'species' + ',' + str(len(tmp['species'])) + '\n')

fr.close()
fw.close()
