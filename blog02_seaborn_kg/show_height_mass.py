# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt  
import seaborn as sns
import pandas as pd

#读取数据 name height mass gender homeworld
df = pd.read_csv('stat_character.csv')  
fig, ax = plt.subplots(1,1)

#散点图
#sns.jointplot(x="height", y="mass", data=df, color="b", s=50, kind='scatter',
#              space = 0.1, size = 8, ratio = 5)

#回归图
#sns.jointplot(x="height", y="mass", data=df, color="b", kind='reg')

#六角形
#sns.jointplot(x="height", y="mass", data=df, color="b", kind='hex')

#KDE 图
#sns.jointplot(x="height", y="mass", data=df, kind="kde", space=0, color="#6AB27B")

#散点图+KDE 图
#g = (sns.jointplot(x="height", y="mass", data=df, color="k")
#      .plot_joint(sns.kdeplot, zorder=0, n_levels=6))

#sns.pairplot(df)

"""
#矩阵散点图 - pairplot()
sns.pairplot(df, vars = ['height', 'mass'], 
    kind = 'scatter',             #散点图/回归分布图{'scatter', 'reg'})
    diag_kind = 'hist',         #直方图/密度图{'hist'， 'kde'}
    hue = 'gender',              #按照某一字段进行分类
    palette = 'husl',              #设置调色板
    markers = ['o', 's', 'D'],    #设置不同系列的点样式 参考分类个数
    size = 2                         #图标大小
    )
"""

g = sns.pairplot(df,                         #数据
                 vars = ['height', 'mass'], #获取数据列
                 kind = 'reg',                  #散点图/回归分布图{'scatter', 'reg'})
                 diag_kind = 'kde',         #直方图/密度图{'hist'， 'kde'}
                 hue = 'gender',              #按照某一字段进行分类
                 palette = 'husl'              #设置调色板
                 )
          
plt.show()

iris, 




