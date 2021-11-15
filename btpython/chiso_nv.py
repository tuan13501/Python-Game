import pygame
#Cac chi so:
HP_goc=1000
HP=HP_goc
HP_x=int((HP/HP_goc)*86)
ATK=300
hut_HP=0
giap=0
#Thanh mau
HP_MP_img = pygame.image.load('nhanvat/thanhmau/HP_MP.png')
HP_MP_img = pygame.transform.scale( HP_MP_img,(200,60))
HP_img = pygame.image.load('nhanvat/thanhmau/HP.png')
HP_img = pygame.transform.scale(HP_img,(HP_x,15))
MP_img = pygame.image.load('nhanvat/thanhmau/MP.png')
MP_img = pygame.transform.scale( MP_img,(80,10))

