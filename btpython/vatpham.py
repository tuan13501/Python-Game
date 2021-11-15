import os
import re
import pygame
from random import randint
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts
def vatpham(path,l,a,s):
    for li in l: 
	    vp=pygame.image.load(f'{path}/{li}')
	    vp=pygame.transform.scale(vp,(s,s))
	    a.append(vp)
path = "vatpham/trangbi"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
trangbi=[]
vatpham(path,l,trangbi,30)
trangbi_ht=[]
vatpham(path,l,trangbi_ht,60)
#Roi vat pham ngau nhien khi giet quai:
hanhtrang=[]
kt_hienthi=[]
VP_ht=[]
VP_x=[]
VP_y=[]
VP_ht_x=[]
VP_ht_y=[]
#Kiem tra xem co roi trang bi khong
def roi():
    a=randint(1,100)
    if a%15==0:
        return randint(0,2)
    elif a%21==0:
        return randint(3,5)
    elif a%33==0:
        return randint(6,8)
    elif a%10==0:
        return 9
    else:
        return -1
#Kiem tra trang bi nhat la trang bi gi
def kt_VP(a,b,c,d,e,f):
    if(a==0):
        b.append(0)
        c.append(randint(200,500))
        d.append(randint(2,6))
        e.append(0)
        f.append(0)
    elif(a==1):
        b.append(1)
        c.append(randint(200,500))
        d.append(randint(2,6))
        e.append(0)
        f.append(0)
    elif(a==2):
        b.append(2)
        c.append(randint(200,500))
        d.append(randint(2,6))
        e.append(0)
        f.append(0)
    elif(a==3):
        b.append(0)
        c.append(randint(200,500))
        d.append(randint(2,6))
        e.append(randint(50,200))
        f.append(0)
    elif(a==4):
        b.append(1)
        c.append(randint(200,500))
        d.append(randint(2,6))
        e.append(randint(50,200))
        f.append(0)
    elif(a==5):
        b.append(2)
        c.append(randint(200,500))
        d.append(randint(2,6))
        e.append(randint(50,200))
        f.append(0)
    elif(a==6):
        b.append(0)
        c.append(randint(200,500))
        d.append(randint(2,6))
        e.append(randint(50,200))
        f.append(randint(4,10))
    elif(a==7):
        b.append(1)
        c.append(randint(200,500))
        d.append(randint(2,6))
        e.append(randint(50,200))
        f.append(randint(4,10))
    elif(a==8):
        b.append(2)
        c.append(randint(200,500))
        d.append(randint(2,6))
        e.append(randint(50,200))
        f.append(randint(4,10))
    elif(a==9):
        b.append(3)
        c.append(0)
        d.append(0)
        e.append(0)
        f.append(0) 

#Auto nhat vat pham
def  auto(a,x,s):
    if abs(a-x+s)>10:
        if a+s>x:
            return 30
        else :
            return -30
    else:
        return 0
anh_VP=[]
#Cac Chi so cua vat pham
HP=[]
ATK=[]
hut_HP=[]
Giap=[]
ten=[ "Giay Kien Cuong ","Ao Choang Bang Gia","Khien That Truyen"]
#Chi so vat pham da su dung
do_sd=[]
HP_sd=[0]*3
ATK_sd=[0]*3
hut_HP_sd=[0]*3
Giap_sd=[0]*3
kt_VP_sd=[0]*3


