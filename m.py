import pygame
screen=pygame.display.set_mode((950,530))
wid=50
hig=110
x1=600
y1=350
x2=200
y2=350
vel=5
jump=9.5
up=False
w=False
run=True
creem=(230,230,230)
black=(0,0,0)
red=(255,0,0)
yellow=(255,255,0)
green=(0,255,0)
blue=(0,0,255)
jump1=jump
jump2=jump
radi=17
a_speed=40
life1=5
life2=5
cir1=False
cir2=False
zero1=True
zero2=True
a_pos1=True
a_pos2=True
life1=5
life2=5
bullet1=2
bullet2=2
relodet=130
p1w=False
p2w=False
time=0
while run:
	pygame.display.set_caption(str(time))
	lx1=930
	ly1=20
	lx2=20
	ly2=20
	time+=1
	pygame.time.delay(27)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	keys=pygame.key.get_pressed()
#player 1 movement
	if keys[pygame.K_LEFT] and x1>x2+wid:
		x1=x1-vel
	if keys[pygame.K_RIGHT] and x1<900:
		x1=x1+vel
	if keys[pygame.K_UP]:
		up=True
	if up:
		if(jump1>=-jump):
			if(jump1>0):
				y1=y1-(jump1**2)*0.8
			else:
				y1=y1+(jump1**2)*0.8
			jump1-=1
		else:
			up=False
			jump1=jump
#player two movement
	if keys[pygame.K_w]:
		w=True
	if w:
		if(jump2>=-jump):
			if(jump2>0):
				y2=y2-(jump2**2)*0.8
			else:
				y2=y2+(jump2**2)*0.8
			jump2-=1
		else:
			w=False
			jump2=jump
	if keys[pygame.K_a] and x2>0:
		x2=x2-vel
	if keys[pygame.K_d] and x2+wid<x1:
		x2=x2+vel
#bullet relode
	if (((time%relodet)==0) and (bullet1<5)):
		bullet1+=1
	if (((time%relodet)==0) and (bullet2<5)):
		bullet2+=1
#aura movement
	if zero1:
		cir1_y=0
		cir1_x=0
	if zero2:
		cir2_y=0
		cir2_x=0
#aura two
	if bullet2>0:
		if keys[pygame.K_s]:
			zero2=False
			cir2=True
	if cir2:
		if a_pos2:
			cir2_x=x2+wid+radi
			cir2_y=int(y2)+radi
			a_pos2=False
		pygame.draw.circle(screen,green,[cir2_x,cir2_y],radi)
		cir2_x+=a_speed
		if cir2_x>950:
			cir2=False
			zero2=True
			a_pos2=True
			bullet2-=1
#aura one
	if bullet1>0:
		if keys[pygame.K_DOWN]:
			cir1=True
			zero1=False
	if cir1:
		if a_pos1:
			cir1_x=x1-radi
			cir1_y=int(y1)+radi
			a_pos1=False
		pygame.draw.circle(screen,blue,[cir1_x,cir1_y],radi)
		cir1_x-=a_speed
		if cir1_x<0:
			cir1=False
			a_pos1=True
			zero1=True
			bullet1-=1
	if ((cir1_x-cir2_x)<30) and ((cir1_y-cir2_y)<12) and((cir1_y-cir2_y)>-12):
		cir1=False
		a_pos1=True
		cir2=False
		a_pos2=True
		zero1=True
		zero2=True
	for i in range(life1):
		pygame.draw.rect(screen,creem,[lx1,ly1,15,25])
		lx1-=20
	for i in range(life2):
		pygame.draw.rect(screen,creem,[lx2,ly2,15,25])
		lx2+=20
	for i in range(bullet1):
		pygame.draw.rect(screen,red,[lx1,ly1+30,15,25])
		lx1-=20
	for i in range(bullet2):
		pygame.draw.rect(screen,yellow,[lx2,ly2+30,15,25])
		lx2+=20
	pygame.draw.rect(screen,red,[x1,y1,wid,hig])
	pygame.draw.rect(screen,yellow,[x2,y2,wid,hig])
	pygame.display.update()
#hit player one
	if (((cir2_y>=y1) and (cir2_y<=(y1+hig+5))) and ((cir2_x>x1) and (cir2_x<(x1+wid)))):
		life1-=1
	if (((cir1_y>=y2) and (cir1_y<=(y2+hig+5))) and ((cir1_x>x2) and (cir1_x<(x2+wid)))):
		life2-=1
	if life2==0:
		run=False
	if life1==0:
		run=False
	screen.fill(black)
