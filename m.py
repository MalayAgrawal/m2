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
black=(0,0,0)
red=(255,0,0)
yellow=(255,255,0)
jump1=jump
jump2=jump
while run:
	pygame.time.delay(27)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	keys=pygame.key.get_pressed()
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
	pygame.draw.rect(screen,red,[x1,y1,wid,hig])
	pygame.draw.rect(screen,yellow,[x2,y2,wid,hig])
	pygame.display.update()
	screen.fill(black)













