import random; import time; import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Screen")
end,clock=True,pygame.time.Clock()
x=y=300
frame=0
color=(255,0,0)
bullets=[]
score=0
movement=2
targets=[]
enemies=[]

spaceship=pygame.image.load('spaceship.png')
spaceship=pygame.transform.scale(spaceship,(50,75))
enemy=pygame.image.load('dodger guy.png')
enemy=pygame.transform.scale(enemy, (22,16))

def draw_targets(enemy):
    global targets
    global enemies
    enemies=[]
    for a in targets:
        enemies.append(screen.blit(enemy,(a[0],a[1])))

def showtext(msg, x, y, color, size):
    fontobj= pygame.font.SysFont('freesans', size, bold=True)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))

while end:
    screen.fill((0,0,0))
    draw_targets(enemy)
    ship=screen.blit(spaceship,(x,y))
    
    for a in bullets:
        bullet=screen.blit(pygame.image.load('bullet.png'),(a[0],a[1]))
        a[1]-=10
        if a[1]<-25: bullets.remove(a)
        for b in enemies:
            if bullet.colliderect(b):
                targets.pop(enemies.index(b))
                enemies.remove(b)
                bullets.remove(a)
                score+=1
    showtext(('Score: '+str(score)),10,550,(255,255,0),50)
    
    pygame.display.update()
    clock.tick(60)
    frame+=1
    if frame%10==0: bullets.append([x+20,y-35])
    if frame%150==0:
        for a in range(12):
            targets.append([a*40+69,-20])
    if frame%3==0: 
        for a in targets:
            a[1]+=1

    for event in pygame.event.get():
        if event.type==4:
            x,y=event.pos[0]-25,event.pos[1]-37
        if event.type==pygame.QUIT:
            end=False
    for a in enemies:
        if ship.collidelistall(enemies) or a[1]>600:
            end=False
            screen.fill((0,0,0))
            showtext('You lose', 250, 275, (200,0,0), 50)
            pygame.display.update()
            time.sleep(3)
            break
pygame.quit()
