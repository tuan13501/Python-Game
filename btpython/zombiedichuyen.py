import zombie_map
import nhanvat

#Zombie di chuyen khong gap vat can:
def buoc(a,x,s):
	if abs(a-x+s)>5:
		if a+s>x:
			return 5
		else :
			return -5
	else:
		return 0
#Zombie di chuyen khi gap vat can:
#def vacham_buoc(a,b,x,y,sx,sy):

		


