from wxpy import *
from pyecharts import Map
import webbrowser
bot = Bot(cache_path=True) #生成微信机器人
friends = bot.friends()
area = {}
for friend in friends:
    if friend.province not in area:
        area[friend.province]=1
    else:
        area[friend.province]= area[friend.province]+1
print(area)
attr = area.keys()
valuse = area.values()

map = Map('全国地图实例',width=900,height=600)
map.add('',attr,valuse,maptype='china',is_visualmap=True)
map.render('provience.html')
webbrowser.open('provience.html')