#import pygame

#map1= pygame.image.load('map/map1.png')
#map1=pygame.transform.scale(map1,(500,300))
import os
import re
import pygame
numbers = re.compile(r'(\d+)')
def numericalSort(value):
	parts = numbers.split(value)
	parts[1::2] = map(int, parts[1::2])
	return parts
def mapgame(path,l,a):
	for li in l: 
		ma=pygame.image.load(f'{path}/{li}')
		a.append(ma)

#Map 1:
path = "map/map1"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
map1=[]
mapgame(path,l,map1)

 # Map1[0]:
map1[0]= pygame.transform.scale(map1[0],(1000,600))
map1_0x=[]
map1_0y=[]
for i in range(-1,3):
	for j in range(-4,2):
		map1_0x.append(i*1000)
		map1_0y.append(j*600)

 # Map1[1]:
map1[1]= pygame.transform.scale(map1[1],(300,100))
map1_1x=[320,500,920,390,470,410,1290,1080,1300]
map1_1y=[290,-80,-570,-840,-1220,-1820,-1110,-1520,-2080]
# Map1[2]:
map1[2]= pygame.transform.scale(map1[2],(150,50))
map1_2x=[600,900,450,1200,1200,600,840,710,1270]
map1_2y=[200,-200,-500,-700,300,-1400,-1100,-1980,-1730]
map1_2=[]
for i in range(len(map1_2x)):
	a=pygame.Rect(map1_2x[i],map1_2y[i]-30,150,50)
	map1_2.append(a)
for i in range(0,13):
	map1_2x.append(i*150)
	map1_2y.append(550)
for i in range(-24,6):
	map1_2x.append(0)
	map1_2y.append(i*100)
for i in range(-24,6):
	map1_2x.append(1740)
	map1_2y.append(i*100)
for i in range(13):
	map1_2x.append(i*150)
	map1_2y.append(-2250)

#Map1[3]:
map1[3]= pygame.transform.scale(map1[3],(150,50))
map1_3x=[]
map1_3y=[]
for i in range(len(map1_2x)):
	a=pygame.Rect(map1_2x[i],map1_2y[i]-70,150,50)
	map1_2.append(a)
for i in range(len(map1_2x)):
	map1_3x.append(map1_2x[i])
	map1_3y.append(map1_2y[i]-50)

# Map1[4]:
map1[4]= pygame.transform.scale(map1[4],(50,50))
map1_4x=[290,260,220,450,290,750,800,330,380,260,300,130,340,370,640,750,560,740,1030,1000,960,1070,1300,1560]
map1_4y=[240,410,-140,-240,-600,-380,-380,-1070,-1100,-2080,-2000,-1870,-1590,-1590,-1340,-1530,-1810,-2070,-2070,-1680,-1220,-40,130,1560]

# Map1[5]:
map1[5]= pygame.transform.scale(map1[5],(100,50))
map1_5x=[950,1410,1520,880,1430,1480,510]
map1_5y=[320,-40,370,-840,-1290,-400,-1680]
#Anh cua cay:
map_cay=[]

 		



