#!/usr/bin/env python
# coding: utf-8
# In[2]:
import pandas as pd
import matplotlib.pyplot as plt
# In[3]:
#加载数据
movies_df = pd.read_csv('C:/Users/文/PycharmProjects/pythonProject/项目示例/movie_metadata.csv',encoding="GBK")
# In[4]:
print(movies_df.head())   #输出默认头5行。比原版增加了print()
# In[5]:
print(movies_df.info())    #输出movies_df的信息
print(movies_df.describe())  #输出movies_df的基本统计量和分位数等值
# In[6]:
column_null_number = movies_df.isnull().sum()
# In[7]:
print('每列缺失值个数','\n',column_null_number)
# In[8]:
movies_df_nonull = movies_df.dropna()
# In[9]:
print('每列缺失值个数','\n',movies_df_nonull.isnull().sum())
# In[10]:
movies_df_new = movies_df_nonull.drop_duplicates(keep='first')
# In[11]:
print(movies_df_new.count())
# In[12]:
print(movies_df_new.head())        #输出默认头5行
# In[13]:
print(movies_df_new.describe())
# 下面是自己封装的函数:
def top10area():
    country_group = movies_df_new.groupby('country').size()
    # In[15]:
    print(country_group)
    group_head_10 = country_group.sort_values(ascending=False).head(10)
    print(group_head_10)
    group_head_10.plot(kind='bar')
    plt.xlabel("country/area")
    plt.show()  # 本行是新添加的

def year_count():
    group_year = movies_df_new.groupby('title_year').size()
    print(group_year)
    group_year.plot()
    plt.show()  # 本行是新添加的

'''

movies_df_new['title_year'].value_counts().sort_index().\
                      plot(kind='line',label='total number')
movies_df_new[movies_df_new['color']=='Color']['title_year'].\
                         value_counts().sort_index().plot(kind='line',\
                                     c='red',label='color number')
movies_df_new[movies_df_new['color']!='Color']['title_year'].\
                   value_counts().sort_index().plot(kind='line',c='black',\
                                     label='Black White number')
plt.legend(loc='upper left')
types = []
for tp in movies_df_new['genres']:
              sp = tp.split('|')
              for x in sp:
                  types.append(x)
types_df = pd.DataFrame({'genres':types})
types_df_counts = types_df['genres'].value_counts()
print(types_df_counts)
types_df_counts.plot(kind='bar')
plt.xlabel('genres')
plt.ylabel('number')
plt.title('genres&number')
plt.show()
b1 = types_df_counts/types_df_counts.sum()
explode = (b1>=0.06)/20+0.02
types_df_counts.plot.pie(autopct='%1.1f%%',figsize=(8,8),\
                                   label='',explode=explode)
plt.title('Movie Type Proportional Distribution Map')
plt.show()   #本行是新添加的
year_gross = movies_df_new.groupby('title_year')['gross'].sum()
year_gross.plot(figsize=(10,5))
plt.xticks(range(1915,2018,5))
plt.xlabel('year')
plt.ylabel('gross')
plt.title('year&gross')
plt.show()   #本行是新添加的
movie_grose_20 = movies_df_new.sort_values(['gross'], ascending=False).head(20)
print(movie_grose_20[['movie_title','gross','genres']])
plt.scatter(x= movies_df_new.imdb_score,y= movies_df_new.gross/100000000)
plt.xlabel('imdb_score')
plt.ylabel('gross')
plt.title('imdb_score&gross')
plt.show()   #本行是新添加的

plt.scatter(x= movies_df_new.duration,y= movies_df_new.gross/100000000)
plt.xlabel('duration')
plt.ylabel('gross')
plt.title('duration&gross')
plt.show()   #本行是新添加的

movie_score_20 = movies_df_new.sort_values(['imdb_score'], ascending=False).head(20)
print(movie_score_20[['movie_title','imdb_score']])
plt.scatter(x= movies_df_new.imdb_score, y=movies_df_new.movie_facebook_likes)
plt.xlabel('imdb_score')
plt.ylabel('movie_facebook_likes')
plt.title('imdb_score&likes')
plt.show()   #本行是新添加的
'''
