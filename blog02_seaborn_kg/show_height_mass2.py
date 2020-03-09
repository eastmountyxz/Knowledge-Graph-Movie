# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt  
import seaborn as sns
import pandas as pd

#读取数据 name height mass gender homeworld
df = pd.read_csv('stat_character.csv')  
fig, ax = plt.subplots(1,1)

"""
#绘制矩阵散点图 pairplot
g = sns.pairplot(df,                         #数据
                 vars = ['height', 'mass'], #获取数据列
                 kind = 'reg',                  #散点图/回归分布图{'scatter', 'reg'})
                 diag_kind = 'kde',         #直方图/密度图{'hist'， 'kde'}
                 hue = 'gender',              #按照某一字段进行分类
                 palette = 'husl'              #设置调色板
                 )
"""

sns.pairplot(df, kind = 'scatter',diag_kind = 'hist', hue = 'gender',
             palette = 'husl', markers = ['o', 's', 'D', '*'], size = 2)
plt.show()




