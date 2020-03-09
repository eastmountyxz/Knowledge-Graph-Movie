# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt  
import pandas as pd

#获取数据
df = pd.read_csv('stat_character.csv')  
fig = plt.figure()
axes = fig.add_subplot(111)

#显示数据
print(df["height"])
print(df["mass"])

height = df["height"]
mass = df["mass"]
sex = df["gender"]

for i in range(len(sex)):
    if sex[i] == "male":
        axes.scatter(height[i], mass[i], color = 'red', s=100, marker='o')
    if sex[i] == "female":
        axes.scatter(height[i], mass[i], color = 'green', s=100, marker='s')
    if sex[i] == "hermaphrodite":
        axes.scatter(height[i], mass[i], color = 'black', s=100, marker='*')
    if sex[i] == "none":
        axes.scatter(height[i], mass[i], color = 'blue', s=200, marker='p')
        
plt.xlabel('height')
plt.ylabel('mass')
plt.show()


