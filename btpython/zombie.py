import os
import re
import pygame
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts
def zombie(path,l,a):
    for li in l: 
	    zo=pygame.image.load(f'{path}/{li}')
	    zo=pygame.transform.scale(zo,(80,80))
	    a.append(zo)
#zombie di chuyen right
path = "Zombies/BucketheadZombie/BucketheadZombie"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
BucketheadZombie=[]
zombie(path,l,BucketheadZombie)

path = "Zombies/ConeheadZombie/ConeheadZombie"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
ConeheadZombie=[]
zombie(path,l,ConeheadZombie)

path = "Zombies/FlagZombie/FlagZombie"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
FlagZombie=[]
zombie(path,l,FlagZombie)

#zombie di chuyen left
path = "Zombies/BucketheadZombie/BucketheadZombie_left"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
BucketheadZombie_left=[]
zombie(path,l,BucketheadZombie_left)

path = "Zombies/ConeheadZombie/ConeheadZombie_left"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
ConeheadZombie_left=[]
zombie(path,l,ConeheadZombie_left)

path = "Zombies/FlagZombie/FlagZombie_left"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
FlagZombie_left=[]
zombie(path,l,FlagZombie_left)
def HP(a):
    if (a==0):
         return 1000
    elif (a==1):
        return 1500
    else:
        return 2000
def ATK(a):
    if (a==0):
         return 15
    elif (a==1):
        return 20
    else:
        return 25
