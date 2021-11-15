import pygame , sys
import map
import nhanvat
import vacham
import zombie
import zombie_map
import zombiedichuyen
import dan
import chiso_nv
import vatpham
import chucnang
import music
import math
from pygame.locals import *
from random import randint
from datetime import datetime
import time
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((1000,600))
font = pygame.font.SysFont('san',35)
pygame.display.set_caption('test')
keys = [False]*8
#Toc do nhan vat:
speed=5
#Thoi gian ban dau zombie:
thoigian_zombie=datetime.now().second
#click chuot:
click=0
#dan nhan vat
anh_dan_nv=[]
dan_nv=[]
# toa do dan
dan_nv_x=[]
dan_nv_y=[]
#Hanh trang
kt_hanhtrang=0
#Kiem tra xem game co dung tam thoi khong:
pause=0
#Kiem tra hien thong tin vat pham hay khong
kt_ht=0
kt_ht_sd=0
music.tieng_nen()
while True:
	clock.tick(10)
	display.fill(0)
	for i in range(len(map.map1_0x)):
		display.blit(map.map1[0],(map.map1_0x[i],map.map1_0y[i]))
	for i in range(len(map.map1_1x)):
		display.blit(map.map1[1],(map.map1_1x[i],map.map1_1y[i]))
	for i in range(len(map.map1_4x)):
		display.blit(map.map1[4],(map.map1_4x[i],map.map1_4y[i]))
	for i in range(len(map.map1_5x)):
		display.blit(map.map1[5],(map.map1_5x[i],map.map1_5y[i]))
	for i in range(len(map.map1_3x)):
		cay=display.blit(map.map1[3],(map.map1_3x[i],map.map1_3y[i]))
		map.map_cay.append(cay)
	for i in range(len(map.map1_2x)):
		cay=display.blit(map.map1[2],(map.map1_2x[i],map.map1_2y[i]))
		map.map_cay.append(cay)
	if pause==0:
	    for i in range(len(map.map1_0x)):
		    display.blit(map.map1[0],(map.map1_0x[i],map.map1_0y[i]))
	    for i in range(len(map.map1_1x)):
		    display.blit(map.map1[1],(map.map1_1x[i],map.map1_1y[i]))
	    for i in range(len(map.map1_4x)):
		    display.blit(map.map1[4],(map.map1_4x[i],map.map1_4y[i]))
	    for i in range(len(map.map1_5x)):
		    display.blit(map.map1[5],(map.map1_5x[i],map.map1_5y[i]))
	    for i in range(len(map.map1_3x)):
		    cay=display.blit(map.map1[3],(map.map1_3x[i],map.map1_3y[i]))
		    map.map_cay.append(cay)
	    for i in range(len(map.map1_2x)):
		    cay=display.blit(map.map1[2],(map.map1_2x[i],map.map1_2y[i]))
		    map.map_cay.append(cay)
	    #Hien thi vat pham tren map:
	    i=0
	    while i<len(vatpham.hanhtrang):
		    VP=display.blit(vatpham.trangbi[vatpham.hanhtrang[i]],(vatpham.VP_x[i],vatpham.VP_y[i]))
		    vatpham.anh_VP.append(VP)
		    vatpham.VP_x[i]+=vatpham.auto(nhanvat.sx,vatpham.VP_x[i],zombie_map.sx)
		    vatpham.VP_y[i]+=vatpham.auto(nhanvat.sy,vatpham.VP_y[i],zombie_map.sy)
		    if nv.colliderect(vatpham.anh_VP[i]):
		    	if vatpham.hanhtrang[i]!=3:
		    		vatpham.VP_ht.append(vatpham.hanhtrang[i])
		    		vatpham.kt_hienthi.append(0)
		    		del vatpham.VP_x[i]
		    		del vatpham.VP_y[i]
		    		del vatpham.hanhtrang[i]
		    		i-=1
		    	else:
		    		chiso_nv.HP+=300
		    		if chiso_nv.HP>chiso_nv.HP_goc:
		    			chiso_nv.HP=chiso_nv.HP_goc
		    		del vatpham.hanhtrang[i]
		    		del vatpham.VP_x[i]
		    		del vatpham.VP_y[i]
		    		i-=1
		    i+=1
	    #NhanVat:

	    if (nhanvat.kt==0):
		    if nhanvat.f[0]<len(nhanvat.nvphai):
			    nv=display.blit(nhanvat.nvphai[nhanvat.f[0]],(nhanvat.x,nhanvat.y))
	    elif (nhanvat.kt==1):
		    if nhanvat.f[1]<len(nhanvat.nvtrai):
			    nv=display.blit(nhanvat.nvtrai[nhanvat.f[1]],(nhanvat.x,nhanvat.y))
	    elif (nhanvat.kt==2):
		    if nhanvat.f[2]<len(nhanvat.nvtren):
			    nv=display.blit(nhanvat.nvtren[nhanvat.f[2]],(nhanvat.x,nhanvat.y))
	    elif (nhanvat.kt==3):
		    if nhanvat.f[3]<len(nhanvat.nvduoi):
			    nv=display.blit(nhanvat.nvduoi[nhanvat.f[3]],(nhanvat.x,nhanvat.y))
	    elif (nhanvat.kt==4):
		    if nhanvat.f[4]<len(nhanvat.nvtrenphai):
			    nv=display.blit(nhanvat.nvtrenphai[nhanvat.f[4]],(nhanvat.x,nhanvat.y))
	    elif (nhanvat.kt==5):
		    if nhanvat.f[5]<len(nhanvat.nvtrentrai):
			    nv=display.blit(nhanvat.nvtrentrai[nhanvat.f[5]],(nhanvat.x,nhanvat.y))
	    elif (nhanvat.kt==6):
		    if nhanvat.f[6]<len(nhanvat.nvduoiphai):
			    nv=display.blit(nhanvat.nvduoiphai[nhanvat.f[6]],(nhanvat.x,nhanvat.y))
	    elif (nhanvat.kt==7):
		    if nhanvat.f[7]<len(nhanvat.nvduoitrai):
			    nv=display.blit(nhanvat.nvduoitrai[nhanvat.f[7]],(nhanvat.x,nhanvat.y))
	    #Cho nhan vat ve vi tri ban dau:

	    if nhanvat.kt1==1:
		    if (nhanvat.f[0]>=0 and nhanvat.f[0]<=3 and nhanvat.kt==0):
			    nhanvat.f[0]+=1
			    nv=display.blit(nhanvat.nvphai[nhanvat.f[0]],(nhanvat.x,nhanvat.y))
		    elif (nhanvat.f[1]>=0 and nhanvat.f[1]<=3 and nhanvat.kt==1):
			    nhanvat.f[1]+=1
			    nv=display.blit(nhanvat.nvtrai[nhanvat.f[1]],(nhanvat.x,nhanvat.y))
		    elif (nhanvat.f[2]>=0 and nhanvat.f[2]<=3 and nhanvat.kt==2):
			    nhanvat.f[2]+=1
			    nv=display.blit(nhanvat.nvtren[nhanvat.f[2]],(nhanvat.x,nhanvat.y))
		    elif (nhanvat.f[3]>=0 and nhanvat.f[3]<=3 and nhanvat.kt==3):
			    nhanvat.f[3]+=1
			    nv=display.blit(nhanvat.nvduoi[nhanvat.f[3]],(nhanvat.x,nhanvat.y))
		    elif (nhanvat.f[4]>=0 and nhanvat.f[4]<=3 and nhanvat.kt==4):
			    nhanvat.f[4]+=1
			    nv=display.blit(nhanvat.nvtrenphai[nhanvat.f[4]],(nhanvat.x,nhanvat.y))
		    elif (nhanvat.f[5]>=0 and nhanvat.f[5]<=3 and nhanvat.kt==5):
			    nhanvat.f[5]+=1
			    nv=display.blit(nhanvat.nvtrentrai[nhanvat.f[5]],(nhanvat.x,nhanvat.y))
		    elif (nhanvat.f[6]>=0 and nhanvat.f[6]<=3 and nhanvat.kt==6):
			    nhanvat.f[6]+=1
			    nv=display.blit(nhanvat.nvduoiphai[nhanvat.f[6]],(nhanvat.x,nhanvat.y))
		    elif (nhanvat.f[7]>=0 and nhanvat.f[7]<=3 and nhanvat.kt==7):
			    nhanvat.f[7]+=1
			    nv=display.blit(nhanvat.nvduoitrai[nhanvat.f[7]],(nhanvat.x,nhanvat.y))
	    #Zombie:
	    thoigian_xhzombie=datetime.now().second
	    if thoigian_zombie>thoigian_xhzombie:
		    thoigian_zombie-=60
	    if thoigian_xhzombie - thoigian_zombie>1:    
		    a=randint(0,2)
		    zombie_map.zombie.append(zombie_map.listZombie[a])
		    zombie_map.zombie_left.append(zombie_map.listZombie_left[a])
		    zombie_map.HP_zombie.append(zombie.HP(a))
		    zombie_map.ATK_zombie.append(zombie.ATK(a))
		    zombie_map.soAnh.append(0)
		    a=randint(0,8)
		    zombie_map.x.append(map.map1_2x[a])
		    zombie_map.y.append(map.map1_2y[a])
		    zombie_map.kt.append(0)
		    thoigian_zombie=thoigian_xhzombie
	    i=0
	    while i<len(zombie_map.zombie):
		    if (zombie_map.soAnh[i]<len(zombie_map.zombie[i])-1):
			    zombie_map.soAnh[i]+=1
		    else : zombie_map.soAnh[i]=0
		    if nhanvat.sx+zombie_map.sx<zombie_map.x[i]:
			    zo=display.blit(zombie_map.zombie[i][zombie_map.soAnh[i]],(zombie_map.x[i],zombie_map.y[i]))
			    zombie_map.anh_zombie.append(zo)
			    zombie_map.x[i]+=zombiedichuyen.buoc(nhanvat.sx,zombie_map.x[i],zombie_map.sx) 
			    zombie_map.y[i]+=zombiedichuyen.buoc(nhanvat.sy,zombie_map.y[i],zombie_map.sy) 
		    else :
			    zo=display.blit(zombie_map.zombie_left[i][zombie_map.soAnh[i]],(zombie_map.x[i],zombie_map.y[i]))
			    zombie_map.anh_zombie.append(zo)
			    zombie_map.x[i]+=zombiedichuyen.buoc(nhanvat.sx,zombie_map.x[i],zombie_map.sx) 
			    zombie_map.y[i]+=zombiedichuyen.buoc(nhanvat.sy,zombie_map.y[i],zombie_map.sy) 
		    if zombie_map.HP_zombie[i]<=0:
			    a=vatpham.roi()
			    if a==9:
			    	vatpham.hanhtrang.append(3)
			    	vatpham.VP_x.append(zombie_map.x[i])
			    	vatpham.VP_y.append(zombie_map.y[i])
			    elif a>=0:
				    vatpham.kt_VP(a,vatpham.hanhtrang,vatpham.HP,vatpham.Giap,vatpham.ATK,vatpham.hut_HP)
				    vatpham.VP_x.append(zombie_map.x[i])
				    vatpham.VP_y.append(zombie_map.y[i])
			    del zombie_map.HP_zombie[i]
			    del zombie_map.ATK_zombie[i]
			    del zombie_map.zombie[i]
			    del zombie_map.zombie_left[i]
			    del zombie_map.x[i]
			    del zombie_map.y[i]
			    i-=1
		    i+=1
	    #Dan nv
	    i=0
	    if click==1:
		    dan_nv.append(dan.dan_nv_img)
		    music.tieng_sung()
		    if nhanvat.kt==0:
			    dan.kt.append(0)
			    dan_nv_x.append(nhanvat.x+50)
			    dan_nv_y.append(nhanvat.y+30)
		    elif nhanvat.kt==1 :
			    dan.kt.append(1)
			    dan_nv_x.append(nhanvat.x-10)
			    dan_nv_y.append(nhanvat.y+10)
		    elif nhanvat.kt==2 :
			    dan.kt.append(2)
			    dan_nv_x.append(nhanvat.x+40)
			    dan_nv_y.append(nhanvat.y-6)
		    elif nhanvat.kt==3 :
			    dan.kt.append(3)
			    dan_nv_x.append(nhanvat.x+8)
			    dan_nv_y.append(nhanvat.y+50)
		    elif nhanvat.kt==4 :
			    dan.kt.append(4)
			    dan_nv_x.append(nhanvat.x+50)
			    dan_nv_y.append(nhanvat.y)
		    elif nhanvat.kt==5 :
			    dan.kt.append(5)
			    dan_nv_x.append(nhanvat.x-3)
			    dan_nv_y.append(nhanvat.y-13)
		    elif nhanvat.kt==6 :
			    dan.kt.append(6)
			    dan_nv_x.append(nhanvat.x+35)
			    dan_nv_y.append(nhanvat.y+45)
		    elif nhanvat.kt==7 :
			    dan.kt.append(7)
			    dan_nv_x.append(nhanvat.x-7)
			    dan_nv_y.append(nhanvat.y+37)
	    while i<len(dan_nv):
		    da=display.blit(dan_nv[i],(dan_nv_x[i],dan_nv_y[i]))
		    anh_dan_nv.append(da)
		    if dan.kt[i]==0:
		    	dan_nv_x[i]+=20
		    elif dan.kt[i]==1:
		    	dan_nv_x[i]-=20
		    elif dan.kt[i]==2:
		    	dan_nv_y[i]-=20
		    elif dan.kt[i]==3:
		    	dan_nv_y[i]+=20
		    elif dan.kt[i]==4:
		    	dan_nv_y[i]-=20
		    	dan_nv_x[i]+=20
		    elif dan.kt[i]==5:
		    	dan_nv_y[i]-=20
		    	dan_nv_x[i]-=20
		    elif dan.kt[i]==6:
		    	dan_nv_y[i]+=20
		    	dan_nv_x[i]+=20
		    elif dan.kt[i]==7:
		    	dan_nv_y[i]+=20
		    	dan_nv_x[i]-=20
		    if dan_nv_y[i]>600 or dan_nv_y[i]<0 or dan_nv_x[i] >1000 or dan_nv_x[i]<0 :
		    	del dan_nv[i]
		    	del dan_nv_x[i]
		    	del dan_nv_y[i]
		    	del dan.kt[i]
		    	i-=1
		    i+=1
	    click=0
	    #va cham dan va zombie
	    d=0
	    while d<len(dan_nv):
		    z=0
		    while z<len(zombie_map.zombie):
		    	if anh_dan_nv[d].colliderect(zombie_map.anh_zombie[z]):
		    		music.tieng_ua()
		    		del anh_dan_nv[d]
		    		del dan_nv[d]
		    		del dan_nv_x[d]
		    		del dan_nv_y[d]
		    		del dan.kt[d]
		    		zombie_map.HP_zombie[z]-=chiso_nv.ATK
		    		chiso_nv.HP+=int((chiso_nv.hut_HP/100)*chiso_nv.ATK)
		    		if chiso_nv.HP>chiso_nv.HP_goc:
		    			chiso_nv.HP=chiso_nv.HP_goc
		    		d-=1
		    		break
		    	z+=1
		    d+=1
	    #va cham dan va cay:
	    d=0
	    while d<len(dan_nv):
		    z=0
		    while z<len(map.map_cay):
		    	if anh_dan_nv[d].colliderect(map.map_cay[z]):
		    		del anh_dan_nv[d]
		    		del dan_nv[d]
		    		del dan_nv_x[d]
		    		del dan_nv_y[d]
		    		del dan.kt[d]
		    		d-=1
		    		break
		    	z+=1
		    d+=1
	    #Nhan vat va zombie va cham:
	    z=0
	    while z<len(zombie_map.zombie):
		    if nv.colliderect(zombie_map.anh_zombie[z]):
			    chiso_nv.HP=chiso_nv.HP-zombie_map.ATK_zombie[z]+chiso_nv.giap
		    z+=1
	    #Cap Nhat chi so nhan vat:
	    chiso_nv.HP_x=int((chiso_nv.HP/chiso_nv.HP_goc)*86)
	    if chiso_nv.HP<=0:
		    chiso_nv.HP=1
	    else:
		    HP_img = pygame.transform.scale(chiso_nv.HP_img,(chiso_nv.HP_x,15))

	    #Thanh mau:
	    HP_SP=display.blit(chiso_nv.HP_MP_img,(0,0))
	    HP = display.blit(HP_img,(107,7))
	    MP=display.blit(chiso_nv.MP_img,(106,28))
	    #Khoi tao lai cac mang luu anh:
	    vatpham.anh_VP=[]
	    map.map_cay=[]	
	    anh_dan_nv=[]
	    zombie_map.anh_zombie=[] 
	#Khi nhan vao hanh trang game se pause:    
	else:
	    anh_VP=[]
	    #Hanh trang:
	    i,j=350,60
	    if (kt_hanhtrang==1):
		    bag=display.blit(chucnang.bag_img,(330,100))
		    thongtin_nv=display.blit(chucnang.thongtin_nv_img,(20,100))
		    for i in range(3):	    	
		    	do=display.blit(chucnang.do_img,(i*90+40,160))
		    	vatpham.do_sd.append(do)
		    	if vatpham.HP_sd[i]>0:
		    		display.blit(vatpham.trangbi_ht[i],(i*90+52,168))
		    		
		    for z in range(len(vatpham.VP_ht)):
			    if (z%8!=0):
				    VP=display.blit(vatpham.trangbi_ht[vatpham.VP_ht[z]],(i,j))
				    vatpham.VP_ht_x.append(i)
				    vatpham.VP_ht_y.append(j)
				    anh_VP.append(VP)
				    i+=80
			    else:
				    j+=90
				    i=350
				    VP=display.blit(vatpham.trangbi_ht[vatpham.VP_ht[z]],(i,j))
				    vatpham.VP_ht_x.append(i)
				    vatpham.VP_ht_y.append(j)
				    anh_VP.append(VP)
				    i+=80
		    z=0
		    #Hien thi thong tin vat pham trong hanh trang
		    while z <len(vatpham.VP_ht):
			    if  anh_VP[z].collidepoint(mouse):
			    	if  click:
			    		if kt_ht==0:			    	
				    		kt_ht=1
				    		vatpham.kt_hienthi[z]=1
				    	else:
				    		kt_ht=0
				    		vatpham.kt_hienthi=[0]*len(vatpham.kt_hienthi)
				    	click=0
			    if kt_ht and vatpham.kt_hienthi[z]:
			    	vatpham.kt_VP_sd=[0]*3
			    	kt_ht_sd=0
			    	if z%8<=3:
			    		a=pygame.draw.rect(display,(210,180,140), (vatpham.VP_ht_x[z], vatpham.VP_ht_y[z], 300, 200))
			    		b=pygame.draw.rect(display,(128,128,128), (vatpham.VP_ht_x[z]+300, vatpham.VP_ht_y[z]+90, 105, 50))
			    		sudung_txt=font.render("Su dung",True,(255,0,255))
			    		sudung=display.blit(sudung_txt,(vatpham.VP_ht_x[z]+305, vatpham.VP_ht_y[z]+100))
			    		c=pygame.draw.rect(display,(128,128,128), (vatpham.VP_ht_x[z]+300, vatpham.VP_ht_y[z]+150, 105, 50))
			    		vutbo_txt=font.render("Vut bo",True,(255,0,255))
			    		vutbo=display.blit(vutbo_txt,(vatpham.VP_ht_x[z]+305, vatpham.VP_ht_y[z]+160))
			    		ten_txt=font.render(vatpham.ten[vatpham.VP_ht[z]],True,(0,0,255))
			    		display.blit(ten_txt,(vatpham.VP_ht_x[z]+10,vatpham.VP_ht_y[z]+10))
			    		HP_txt= font.render(f"+ {vatpham.HP[z]} HP ",True,(255,0,0))
			    		display.blit(HP_txt,(vatpham.VP_ht_x[z]+10,vatpham.VP_ht_y[z]+50))
			    		Giap_txt= font.render(f"+ {vatpham.Giap[z]} Giap",True,(25,25,112))
			    		display.blit(Giap_txt,(vatpham.VP_ht_x[z]+10,vatpham.VP_ht_y[z]+90))
			    		if vatpham.ATK[z]>0:
			    			ATK_txt= font.render(f"+{vatpham.ATK[z]} ATK",True,(0,100,0))
			    			display.blit(ATK_txt,(vatpham.VP_ht_x[z]+10,vatpham.VP_ht_y[z]+130))
			    		if vatpham.hut_HP[z]>0:
			    			Hut_HP_txt= font.render(f"+ {vatpham.hut_HP[z]}% hut mau",True,(128,0,128))
			    			display.blit(Hut_HP_txt,(vatpham.VP_ht_x[z]+10,vatpham.VP_ht_y[z]+170))
			    		if vutbo.collidepoint(mouse):
			    			if click:
			    				chucnang.vutbo(vatpham.VP_ht_x,vatpham.VP_ht_y,vatpham.VP_ht,vatpham.HP,vatpham.Giap,vatpham.ATK,vatpham.hut_HP,vatpham.kt_hienthi,z)
			    				z-=1
			    				click=0
			    				kt_ht=0
			    		if sudung.collidepoint(mouse):
			    			if click:
			    				m=vatpham.VP_ht[z]
			    				chiso_nv.HP_goc=chiso_nv.HP_goc-vatpham.HP_sd[m] + vatpham.HP[z]
			    				chiso_nv.giap=chiso_nv.giap-vatpham.Giap_sd[m] + vatpham.Giap[z]
			    				chiso_nv.ATK=chiso_nv.ATK-vatpham.ATK_sd[m] + vatpham.ATK[z]
			    				chiso_nv.hut_HP=chiso_nv.hut_HP-vatpham.hut_HP_sd[m] + vatpham.hut_HP[z]
			    				chucnang.sudung(vatpham.VP_ht_x,vatpham.VP_ht_y,vatpham.VP_ht,vatpham.HP,vatpham.Giap,vatpham.ATK,vatpham.hut_HP,vatpham.HP_sd,vatpham.Giap_sd,vatpham.ATK_sd,vatpham.hut_HP_sd,z,m)
			    				vatpham.kt_hienthi[z]=0
			    				click=0
			    				kt_ht=0
			    	else :
			    		a=pygame.draw.rect(display,(210,180,140), (vatpham.VP_ht_x[z]-180, vatpham.VP_ht_y[z],300,200))
			    		b=pygame.draw.rect(display,(128,128,128), (vatpham.VP_ht_x[z]-285, vatpham.VP_ht_y[z]+90, 105, 50))
			    		sudung_txt=font.render("Su dung",True,(255,0,255))
			    		sudung=display.blit(sudung_txt,(vatpham.VP_ht_x[z]-280, vatpham.VP_ht_y[z]+100))
			    		c=pygame.draw.rect(display,(128,128,128), (vatpham.VP_ht_x[z]-285, vatpham.VP_ht_y[z]+150, 105, 50))
			    		vutbo_txt=font.render("Vut bo",True,(255,0,255))
			    		vutbo=display.blit(vutbo_txt,(vatpham.VP_ht_x[z]-285, vatpham.VP_ht_y[z]+160))
			    		ten_txt=font.render(vatpham.ten[vatpham.VP_ht[z]],True,(0,0,255))
			    		display.blit(ten_txt,(vatpham.VP_ht_x[z]-170,vatpham.VP_ht_y[z]+10))
			    		HP_txt= font.render(f"+ {vatpham.HP[z]} HP ",True,(255,0,0))
			    		display.blit(HP_txt,(vatpham.VP_ht_x[z]-170,vatpham.VP_ht_y[z]+50))
			    		Giap_txt= font.render(f"+ {vatpham.Giap[z]} Giap",True,(25,25,112))
			    		display.blit(Giap_txt,(vatpham.VP_ht_x[z]-170,vatpham.VP_ht_y[z]+90))
			    		if vatpham.ATK[z]>0:
			    			ATK_txt= font.render(f"+{vatpham.ATK[z]} ATK",True,(0,100,0))
			    			display.blit(ATK_txt,(vatpham.VP_ht_x[z]-170,vatpham.VP_ht_y[z]+130))
			    		if vatpham.hut_HP[z]>0:
			    			Hut_HP_txt= font.render(f"+ {vatpham.hut_HP[z]}% hut mau",True,(128,0,128))
			    			display.blit(Hut_HP_txt,(vatpham.VP_ht_x[z]-170,vatpham.VP_ht_y[z]+170))
			    		if vutbo.collidepoint(mouse):
			    			if click:
			    				chucnang.vutbo(vatpham.VP_ht_x,vatpham.VP_ht_y,vatpham.VP_ht,vatpham.HP,vatpham.Giap,vatpham.ATK,vatpham.hut_HP,vatpham.kt_hienthi,z)
			    				z-=1
			    				click=0
			    				kt_ht=0
			    		if sudung.collidepoint(mouse):
			    			if click:
			    				m=vatpham.VP_ht[z]
			    				chiso_nv.HP_goc=chiso_nv.HP_goc-vatpham.HP_sd[m] + vatpham.HP[z]
			    				chiso_nv.giap=chiso_nv.giap-vatpham.Giap_sd[m] + vatpham.Giap[z]
			    				chiso_nv.ATK=chiso_nv.ATK-vatpham.ATK_sd[m] + vatpham.ATK[z]
			    				chiso_nv.hut_HP=chiso_nv.hut_HP-vatpham.hut_HP_sd[m] + vatpham.hut_HP[z]
			    				chucnang.sudung(vatpham.VP_ht_x,vatpham.VP_ht_y,vatpham.VP_ht,vatpham.HP,vatpham.Giap,vatpham.ATK,vatpham.hut_HP,vatpham.HP_sd,vatpham.Giap_sd,vatpham.ATK_sd,vatpham.hut_HP_sd,z,m)
			    				vatpham.kt_hienthi[z]=0
			    				click=0
			    				kt_ht=0
			    z+=1
		    #In thong tin nhan vat:
		    HP_txt= font.render(f"HP : {chiso_nv.HP}/{chiso_nv.HP_goc}",True,(255,0,0))
		    ATK_txt= font.render(f"ATK : {chiso_nv.ATK}",True,(0,100,0))
		    Hut_HP_txt= font.render(f"Hut HP : {chiso_nv.hut_HP}%",True,(128,0,128))
		    Giap_txt= font.render(f"Giap : {chiso_nv.giap}",True,(25,25,112))
		    display.blit(HP_txt,(30,280))
		    display.blit(Giap_txt,(30,320)) 
		    display.blit(ATK_txt,(30,360))
		    display.blit(Hut_HP_txt,(30,400))
		    z=0
		    #Hien thi thong tin vat pham su dung:
		    while z < 3:
		    	if vatpham.do_sd[z].collidepoint(mouse) and vatpham.HP_sd[z]>0:
		    		if click:
		    			if kt_ht_sd==0:
		    				kt_ht_sd=1
		    				vatpham.kt_VP_sd[z]=1
		    			else:
		    				kt_ht_sd=0
		    				vatpham.kt_VP_sd=[0]*3
		    			click=0
		    	if kt_ht_sd and vatpham.kt_VP_sd[z]:
		    		kt_ht=0
		    		vatpham.kt_hienthi=[0]*len(vatpham.kt_hienthi)
		    		a=pygame.draw.rect(display,(210,180,140), (z*90+52,168, 300, 200))
		    		ten_txt=font.render(vatpham.ten[z],True,(0,0,255))
		    		display.blit(ten_txt,(z*90+62,178))
		    		HP_txt= font.render(f"+ {vatpham.HP_sd[z]} HP ",True,(255,0,0))
		    		display.blit(HP_txt,(z*90+62,218))
		    		Giap_txt= font.render(f"+ {vatpham.Giap_sd[z]} Giap",True,(25,25,112))
		    		display.blit(Giap_txt,(z*90+62,258))
		    		if vatpham.ATK_sd[z]>0:
		    			ATK_txt= font.render(f"+{vatpham.ATK_sd[z]} ATK",True,(0,100,0))
		    			display.blit(ATK_txt,(z*90+62,298))
			    	if vatpham.hut_HP_sd[z]>0:
			    		Hut_HP_txt= font.render(f"+ {vatpham.hut_HP_sd[z]}% hut mau",True,(128,0,128))
			    		display.blit(Hut_HP_txt,(z*90+62,338))
		    	z+=1
		    #Khoi tao lai cac mang
		    vatpham.VP_ht_x=[]
		    vatpham.VP_ht_y=[]
		    click=0
	pygame.display.flip()
	for event in pygame.event.get():
	# di chuyen --start
	    if event.type == pygame.KEYDOWN:
	    	if event.key==K_d:
	    		keys[0]=True
	    		nhanvat.kt1=0
	    	elif event.key==K_a:
	    		keys[1]=True
	    		nhanvat.kt1=0
	    	if event.key==K_w:
	    		keys[2]=True
	    		nhanvat.kt1=0
	    	elif event.key==K_s:
	    		keys[3]=True
	    		nhanvat.kt1=0
	    	if event.key==K_r:
	    		kt_hanhtrang=1
	    		pause=1
	    	elif event.key==K_x:
	    		kt_hanhtrang=0
	    		vatpham.kt_hienthi=[0]*len(vatpham.kt_hienthi)
	    		vatpham.kt_VP_sd=[0]*3
	    		kt_ht=0
	    		kt_ht_sd=0
	    		pause=0
	    if event.type == pygame.KEYUP:
	    	if event.key==K_d:
	    		keys[0]=False
	    		nhanvat.kt1=1
	    	if event.key==K_a:
	    		keys[1]=False
	    		nhanvat.kt1=1
	    	if event.key==K_w:
	    		keys[2]=False
	    		nhanvat.kt1=1
	    	if event.key==K_s:
	    		keys[3]=False
	    		nhanvat.kt1=1
	    #Click chuot:
	    if event.type == pygame.MOUSEBUTTONDOWN:
	    	click=1
	    #Xac dinh huong cua nhan vat:
	    mouse=pygame.mouse.get_pos()
	    goc=180-math.atan2(nhanvat.y-mouse[1],nhanvat.x-mouse[0])*(180/math.pi)
	    if (goc >0 and goc <15 ) or (goc>330 and goc <360):
	    	nhanvat.kt=0
	    elif (goc>150 and goc<195):
	    	nhanvat.kt=1
	    elif (goc>60 and goc<105):
	    	nhanvat.kt=2
	    elif (goc>240 and goc<285):
	    	nhanvat.kt=3
	    elif (goc>15 and goc<60):
	    	nhanvat.kt=4
	    elif (goc>105 and goc<150):
	    	nhanvat.kt=5
	    elif (goc>285 and goc<330):
	    	nhanvat.kt=6
	    elif (goc>195 and goc<240):
	    	nhanvat.kt=7

	    #Thay doi toa do nhan vat
	    if keys[0]:
	    	if nhanvat.sx<=500:
	    		nhanvat.x+=speed
	    		nhanvat.sx+=speed
	    		zombie_map.sx=0
	    	elif nhanvat.sx<1400:
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
	    		for i in range(len(dan_nv_x)):
	    			dan_nv_x[i]-=speed
	    		for i in range(len(vatpham.VP_x)):
	    			vatpham.VP_x[i]-=speed
	    		zombie_map.sx-=speed
	    	elif nhanvat.sx<1695:
	    		nhanvat.sx+=speed
	    		nhanvat.x+=speed
	    	a=pygame.Rect(nhanvat.sx,nhanvat.sy,60,30)
	    	if vacham.vc(a,map.map1_2,18):
	    		vacham.phai()
	    	nhanvat.huong()	
	    if keys[1]:
	    	if nhanvat.sx>=1400:
	    		nhanvat.x-=speed
	    		nhanvat.sx-=speed
	    	elif nhanvat.sx>500:
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
	    		for i in range(len(dan_nv_x)):
	    			dan_nv_x[i]+=speed
	    		for i in range(len(vatpham.VP_x)):
	    			vatpham.VP_x[i]+=speed
	    		zombie_map.sx+=speed
	    	elif nhanvat.sx>150:
	    		nhanvat.sx-=speed
	    		nhanvat.x-=speed
	    		zombie_map.sx=0
	    	a=pygame.Rect(nhanvat.sx,nhanvat.sy,60,30)
	    	if vacham.vc(a,map.map1_2,18):
	    		vacham.trai()
	    	nhanvat.huong()
	    if keys[2]:
	    	if nhanvat.sy>300:
	    		nhanvat.y-=speed
	    		nhanvat.sy-=speed
	    		zombie_map.sy=0
	    	elif nhanvat.sy>-2000:
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
	    		for i in range(len(dan_nv_y)):
	    			dan_nv_y[i]+=speed
	    		for i in range(len(vatpham.VP_y)):
	    			vatpham.VP_y[i]+=speed
	    		zombie_map.sy+=speed
	    	elif nhanvat.sy>-2240:
	    		nhanvat.sy-=speed
	    		nhanvat.y-=speed

	    	a=pygame.Rect(nhanvat.sx,nhanvat.sy,60,30)
	    	if vacham.vc(a,map.map1_2,18):
	    		vacham.tren()
	    	nhanvat.huong()
	    if keys[3]:
	    	if nhanvat.sy<-2000:
	    		nhanvat.y+=speed
	    		nhanvat.sy+=speed

	    	elif nhanvat.sy<300:
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
	    		for i in range(len(dan_nv_y)):
	    			dan_nv_y[i]-=speed
	    		for i in range(len(vatpham.VP_y)):
	    			vatpham.VP_y[i]-=speed
	    		zombie_map.sy-=speed
	    	elif nhanvat.sy<440:
	    		nhanvat.sy+=speed
	    		nhanvat.y+=speed
	    		zombie_map.sy=0
	    	a=pygame.Rect(nhanvat.sx,nhanvat.sy,60,30)
	    	if vacham.vc(a,map.map1_2,18):
	    		vacham.duoi()
	    	nhanvat.huong()
	    if event.type==pygame.QUIT:
	    	pygame.quit()
	    	sys.exit()