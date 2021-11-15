import os
import re
import pygame
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts
def nhanvat(path,l,a):
    for li in l: 
	    zo=pygame.image.load(f'{path}/{li}')
	    zo=pygame.transform.scale(zo,(60,60))
	    a.append(zo)
path = "NhanVat/duoi"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
nvduoi=[]
nhanvat(path,l,nvduoi)

path = "Nhanvat/duoitrai"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
nvduoitrai=[]
nhanvat(path,l,nvduoitrai)

path = "Nhanvat/duoiphai"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
nvduoiphai=[]
nhanvat(path,l,nvduoiphai)

path = "Nhanvat/phai"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
nvphai=[]
nhanvat(path,l,nvphai)

path = "Nhanvat/trai"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
nvtrai=[]
nhanvat(path,l,nvtrai)

path = "Nhanvat/tren"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
nvtren=[]
nhanvat(path,l,nvtren)

path = "Nhanvat/trenphai"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
nvtrenphai=[]
nhanvat(path,l,nvtrenphai)

path = "Nhanvat/trentrai"
l = os.listdir(path)
l=sorted(l,key=numericalSort)
nvtrentrai=[]
nhanvat(path,l,nvtrentrai)

#Toa do nhan vat
x,y=200,400
##kiem tra nhan vat theo huong nao
kt=0
def huong():
    if (kt==0):
        if f[0]<4:
            f[0]+=1
        else :
            f[0]=0
    elif (kt==1):
        if f[1]<4:
            f[1]+=1
        else :
            f[1]=0   
    elif (kt==2):
        if f[2]<4:
            f[2]+=1
        else :
            f[2]=0 
    elif (kt==3):
        if f[3]<4:
            f[3]+=1
        else :
            f[3]=0
    elif (kt==4):
        if f[4]<4:
            f[4]+=1
        else :
            f[4]=0
    elif (kt==5):
        if f[5]<4:
            f[5]+=1
        else :
            f[5]=0   
    elif (kt==6):
        if f[6]<4:
            f[6]+=1
        else :
            f[6]=0  
    elif (kt==7):
        if f[7]<4:
            f[7]+=1
        else :
            f[7]=0  
#Mang kiem tra nhan vat da dung lai chua
kt1=0
## Mang luu vi tri anh cua nhan vat
f=[4]*8
#Dem quang duong di chuyen tren truc toa do:
sx,sy=x,y
