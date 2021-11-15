import pygame
import nhanvat
import zombie_map
import map
import vatpham
#Va cham nhan vat 
def vc(a,b,n):
	for i in range(n):
		if a.colliderect(b[i]):
			return 1
	return 0
#Dua nhan vat ve vi tri truoc khi va cham:
speed=5
def phai():
	if nhanvat.sx<=500:
	    nhanvat.x-=speed
	    nhanvat.sx-=speed
	elif nhanvat.sx<1400:
	    nhanvat.sx-=speed
	    for i in range(len(map.map1_0y)):
	    	map.map1_0x[i]+=speed
	    for i in range(len(map.map1_2y)):
	    	map.map1_2x[i]+=speed
	    for i in range(len(map.map1_3y)):
	    	map.map1_3x[i]+=speed
	    for i in range(len(map.map1_1y)):
	    	map.map1_1x[i]+=speed
	    for i in range(len(map.map1_4y)):
	    	map.map1_4x[i]+=speed
	    for i in range(len(map.map1_5y)):
	    	map.map1_5x[i]+=speed
	    for i in range(len(zombie_map.y)):
	    	zombie_map.x[i]+=speed
	    for i in range(len(vatpham.VP_x)):
	    	vatpham.VP_x[i]+=speed
	    zombie_map.sx+=speed	
	elif nhanvat.sx<1695:
	    nhanvat.sx-=speed
	    nhanvat.x-=speed
def trai():
	if nhanvat.sx>=1400:
		nhanvat.x+=speed
		nhanvat.sx+=speed
	elif nhanvat.sx>500:
		nhanvat.sx+=speed
		for i in range(len(map.map1_0y)):
			map.map1_0x[i]-=speed
		for i in range(len(map.map1_2y)):
			map.map1_2x[i]-=speed
		for i in range(len(map.map1_3y)):
			map.map1_3x[i]-=speed
		for i in range(len(map.map1_1y)):
			map.map1_1x[i]-=speed
		for i in range(len(map.map1_4y)):
			map.map1_4x[i]-=speed
		for i in range(len(map.map1_5y)):
			map.map1_5x[i]-=speed
		for i in range(len(zombie_map.y)):
			zombie_map.x[i]-=speed
		for i in range(len(vatpham.VP_x)):
			vatpham.VP_x[i]-=speed
		zombie_map.sx-=speed
	elif nhanvat.sx>150:
		nhanvat.sx+=speed
		nhanvat.x+=speed
def tren():
	if nhanvat.sy>300:
		nhanvat.y+=speed
		nhanvat.sy+=speed
	elif nhanvat.sy>-2000:
		nhanvat.sy+=speed
		for i in range(len(map.map1_0y)):
			map.map1_0y[i]-=speed
		for i in range(len(map.map1_2y)):
			map.map1_2y[i]-=speed
		for i in range(len(map.map1_3y)):
			map.map1_3y[i]-=speed
		for i in range(len(map.map1_1y)):
			map.map1_1y[i]-=speed
		for i in range(len(map.map1_4y)):
			map.map1_4y[i]-=speed
		for i in range(len(map.map1_5y)):
			map.map1_5y[i]-=speed
		for i in range(len(zombie_map.y)):
			zombie_map.y[i]-=speed
		for i in range(len(vatpham.VP_x)):
			vatpham.VP_y[i]-=speed
		zombie_map.sy-=speed
	elif nhanvat.sy>-2240:
		nhanvat.sy+=speed
		nhanvat.y+=speed
def duoi():
	if nhanvat.sy<-2000:
		nhanvat.y-=speed
		nhanvat.sy-=speed
	elif nhanvat.sy<300:
		nhanvat.sy-=speed
		for i in range(len(map.map1_0y)):
			map.map1_0y[i]+=speed
		for i in range(len(map.map1_2y)):
			map.map1_2y[i]+=speed
		for i in range(len(map.map1_3y)):
			map.map1_3y[i]+=speed
		for i in range(len(map.map1_1y)):
			map.map1_1y[i]+=speed
		for i in range(len(map.map1_4y)):
			map.map1_4y[i]+=speed
		for i in range(len(map.map1_5y)):
			map.map1_5y[i]+=speed
		for i in range(len(zombie_map.y)):
			zombie_map.y[i]+=speed
		for i in range(len(vatpham.VP_x)):
			vatpham.VP_y[i]+=speed
		zombie_map.sy+=speed
	elif nhanvat.sy<440:
		nhanvat.sy-=speed
		nhanvat.y-=speed

