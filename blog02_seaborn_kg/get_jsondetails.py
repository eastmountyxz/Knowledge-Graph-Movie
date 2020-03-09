#-*- coding: utf-8 -*-
import json

#获取人物的身高和体重的关系
fr = open("film_characters.csv", "r")
fw = open("stat_character.csv", "w")

#姓名 身高 体重 性别 家乡
fw.write('name,height,mass,gender,homeworld'+'\n')

for line in fr:
    print(line.strip('\n'))
    tmp = json.loads(line.strip('\n'))
    #身高体重值unknown设置为-1
    if tmp['height'] == 'unknown':
        tmp['height'] = '-1'
    if tmp['mass'] == 'unknown':
        tmp['mass'] = '-1'
    if tmp['gender'] == 'n/a':
        tmp['gender'] = 'none'
    fw.write(tmp['name'] + ',' + tmp['height'] + ',' + tmp['mass'] + ',' + tmp['gender'].strip() + ',' + tmp['homeworld'] + '\n')
    
fr.close()
fw.close()

