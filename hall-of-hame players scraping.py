#!/usr/bin/env python
# coding: utf-8

# In[273]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# In[274]:


url = 'https://en.hispanosnba.com/players/hall-of-fame/index'


# In[275]:


requ = requests.get(url)
soup = BeautifulSoup(requ.content , 'html.parser')


# In[276]:


table = soup.find('tbody')
url_start = 'https://en.hispanosnba.com'
ths = table.find_all('a')
ths[0]


# In[279]:


#get the url of players
i=0
for th in ths:
    th = str(th)
    th = th.split('"')
    name = th[1]
    ths[i]=url_start+name+'/stats'
    i = i+1
for th in ths:
    print(th)


# In[278]:


#get the players name
player_name = []
for th in ths:
    th = str(th)
    th = th.split('"')
    player_name = player_name + [th[3]]
#player name contain now the names of all the players


# In[283]:


#get tea stats of the players
player_stats=[]
for tr in ths:
    url_a = tr
    requ_a = requests.get(url_a)
    soup_a =  BeautifulSoup(requ_a.content , 'html.parser')
    total_table = soup_a.find('tfoot')
    tr = total_table.find('tr')
    tds = tr.find('td')
    tds = str(tds)
    tds = tds.split('<td>')
    tds[14] = tds[14][8:-9]
    tds[15] = tds[15][:-75]
    player_stats = player_stats + [tds]
#player_stats contain now the stat of all the players


# In[288]:


#generate a empty table
d = {'PLAYER_NAME':[] , 'TEAM':[] , 'GP':[] , 'GS':[] , 'MIN':[] , 'FG':[] , '3P':[] , 'FT':[] ,
     'REB':[] ,'AST':[] , 'STL':[] , 'TO':[] , 'BLK':[] , 'PF':[] , 'PTS':[] , 'EFF':[]}
df = pd.DataFrame(columns = d)
df


# In[289]:


# 1) generate a small table with just one player for every player
# 2) using pd.concat for add the small table to the data frame
i = 0
for stats in player_stats:
    data = {'PLAYER_NAME':[stats[0]], 'TEAM':[stats[1]], 'GP':[stats[2]], 'GS':[stats[3]], 'MIN':[stats[4]], 
            'FG':[stats[5]], '3P':[stats[6]], 'FT':[stats[7]], 'REB':[stats[8]], 'AST':[stats[9]], 'STL':[stats[10]], 
            'TO':[stats[11]], 'BLK':[stats[12]], 'PF':[stats[13]], 'PTS':[stats[14]], 'EFF':[stats[15]]}
    player_row = pd.DataFrame(data , index = [i])
    i = i+1
    df = pd.concat([df , player_row])
df


# In[290]:


#add the players name to the data frame
df['PLAYER_NAME'] = player_name


# In[291]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




