import math
import pygame as pg
import math

pg.init()
window=pg.display.set_mode((852,480))

bg=pg.image.load("bg.jpg")
loop_game=True

icon=pg.image.load("icon.png")
pg.display.set_icon(icon)

pg.display.set_caption("HIT MAN")

width=852
height=480

walkleft=[pg.image.load("L1.png"),pg.image.load("L2.png"),pg.image.load("L3.png"),pg.image.load("L4.png"),pg.image.load("L5.png"),pg.image.load("L6.png"),pg.image.load("L7.png"),pg.image.load("L8.png"),pg.image.load("L9.png")]

walkright=[pg.image.load("R1.png"),pg.image.load("R2.png"),pg.image.load("R3.png"),pg.image.load("R4.png"),pg.image.load("R5.png"),pg.image.load("R6.png"),pg.image.load("R7.png"),pg.image.load("R8.png"),pg.image.load("R9.png")]

walkleft_en=[pg.image.load("L1E.png"),pg.image.load("L2E.png"),pg.image.load("L3E.png"),pg.image.load("L4E.png"),pg.image.load("L5E.png"),pg.image.load("L6E.png"),pg.image.load("L7E.png"),pg.image.load("L8E.png"),pg.image.load("L9E.png"),pg.image.load("L10E.png"),pg.image.load("L11E.png")]

walkright_en=[pg.image.load("R1E.png"),pg.image.load("R2E.png"),pg.image.load("R3E.png"),pg.image.load("R4E.png"),pg.image.load("R5E.png"),pg.image.load("R6E.png"),pg.image.load("R7E.png"),pg.image.load("R8E.png"),pg.image.load("R9E.png"),pg.image.load("R10E.png"),pg.image.load("R11E.png")]


stading=pg.image.load("standing.png")

r_bullet=pg.image.load("rbullet.png")
l_bullet=pg.image.load("lbullet.png")

def display_score():
    global game_over_flag
    font=pg.font.Font('freesansbold.ttf', 32)
    nfont=pg.font.Font('freesansbold.ttf', 20)
    if player_score>=enemy_score:
        player_text=font.render(f"YOUR SCORE: {player_score}",True,(32, 106, 93))
        enemy_text=font.render(f"OPPONENT SCORE:{enemy_score}",True,(190, 0, 0))
        window.blit(player_text,(0,0))
        window.blit(enemy_text,(500,0))
    else:
        game_over_flag=True
        game_over=font.render("GAME OVER",True,(255,0,0))
        best_score=font.render(f"Your Best Score : {player_score}",True,(0,255,0))
        for_continue=nfont.render("For Continue Press TAB",True,(0,0,0))
        window.blit(game_over,(300,200))
        window.blit(best_score,(270,250))
        window.blit(for_continue,(300,280))
def draw_window():
    player.draw_player()
    enemy.show()
    global shoot
    if shoot==True:
        iscollision=bullet.isCollision(enemy.x,enemy.y)
        if iscollision:
            bullet.hit()
            bullet.x=round(player.x+player.width//2)
            shoot=False
        bullet.show_bullet(window)
    display_score()
    pg.display.update()

class Player:
    def __init__(self,x,y,speed,dim):
        self.x=x
        self.y=y
        self.speed=speed
        self.walkcount=0
        self.left=False
        self.right=False
        self.isjump=False
        self.width=self.height=dim
        self.jumpcount=10
        self.standing=True
    
    def draw_player(self):
    
        window.blit(bg,(0,0))
        global walkcount  
        # walkcount=(walkcount+1)%27
        if self.walkcount+1>=27:
            self.walkcount=0

        if not self.standing:
            if self.left:
                window.blit(walkleft[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
            elif self.right:
                window.blit(walkright[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
        else:
            if self.right:
                window.blit(walkright[0],(self.x,self.y))
            else:
                window.blit(walkleft[0],(self.x,self.y))
        # pg.display.update()
    def iscollision(self,enemy_x,enemy_y):
        value=math.sqrt(math.pow(self.x-enemy_x,2)+math.pow(self.y-enemy_y,2))
        if value<=27:
            return True
        return False
    
    def hit(self):
        hitSound.play()
        pg.mixer.music.play()
        global enemy_score
        enemy_score+=1
class Bullet:
    def __init__(self,x,y,facing,radius,color):
        self.x=x
        self.y=y
        self.speed=8*facing
        self.radius=radius
        self.color=color
    def show_bullet(self,window):
        if self.speed<0:
            window.blit(l_bullet,(self.x,self.y))
        # pg.draw.circle(window, self.color, (self.x,self.y), self.radius)
        else:
            window.blit(r_bullet,(self.x,self.y))
        # pg.display.update()
    def isCollision(self,enemy_x,enemy_y):
        value=math.sqrt(math.pow(self.x-enemy_x,2)+math.pow(self.y-enemy_y,2))
        if value<=40:
            return True
        else:
            return False
    def hit(self):
        global player_score
        player_score+=5
class Enemy:
    def __init__(self,x,y,dim):
        self.x=x
        self.y=y
        self.dim=dim
        self.speed=3
        self.path=[x,852-self.speed-self.dim]
        self.en_left=False
        self.en_right=False
        self.en_walkstep=0
    def movement(self):
        if self.speed>0:
            if self.x<self.path[1]+self.speed:
                self.x+=self.speed
            else:
                self.speed=self.speed*(-1)
                self.x+=self.speed
                self.en_walkstep=0
        else:
            if self.x>self.path[0]-self.speed:
                self.x+=self.speed
            else:
                self.speed=self.speed*(-1)
                self.x+=self.speed
                self.en_walkstep=0

    def show(self):
        self.movement()
        if self.en_walkstep+1>=33:
            self.en_walkstep=0
        if self.speed>0:
            window.blit(walkright_en[(self.en_walkstep+1)//3],(self.x,self.y))
            self.en_walkstep+=1
        else:
            window.blit(walkleft_en[(self.en_walkstep+1)//3],(self.x,self.y))
            self.en_walkstep+=1


clock=pg.time.Clock()
fps=27


player=Player(width//2,height-64,5,64)

bullet=Bullet(round(player.x+player.width//2),round(player.y + player.height//2),0,5,(0,0,0))
bullet_state=False
shoot=False

enemy=Enemy(0,height-64,64)

hitSound = pg.mixer.Sound('hit.mp3')

bulletSound = pg.mixer.Sound('bullet.mp3')

music = pg.mixer.music.load('music.mp3')
pg.mixer.music.play(-1)

player_score=0
enemy_score=0
game_over_flag=False

while loop_game:

    clock.tick(fps)

    for event in pg.event.get():
        if event.type==pg.QUIT:
            loop_game=False


    if game_over_flag:
        keys=pg.key.get_pressed()
        if keys[pg.K_TAB]:
                enemy.x=1
                game_over_flag=False
                player_score=0
                enemy_score=0
    
    
    if not game_over_flag:
        if shoot==True:
            if bullet.x<852 and bullet.x>0:
                bullet.x+=bullet.speed
            else:
                shoot=False
        keys=pg.key.get_pressed()
        if keys[pg.K_SPACE] and shoot==False:
            bulletSound.play()
            if player.left:
                facing=-1
            else:
                facing=1
            bullet=Bullet(round(player.x+player.width//2),round(player.y + player.height//2),facing,5,(0,0,0))
            shoot=True
        if keys[pg.K_LEFT] and player.x>player.speed:
            player.x-=player.speed
            player.left=True
            player.right=False
            player.standing=False
        elif keys[pg.K_RIGHT] and player.x<width-64:
            player.x+=player.speed
            player.left=False
            player.right=True
            player.standing=False
        else:
            player.standing=True
            player.walkcount=0
        
        if not player.isjump:
            if keys[pg.K_UP]:
                player.isjump=True
                player.left=False
                player.right=False
                player.walkcount=0
        else:
            if player.jumpcount>=-10:
                neg_sign=1
                if player.jumpcount<0:
                    neg_sign=-1
                player.y-=(player.jumpcount**2) * 0.5 * neg_sign
                player.jumpcount-=1
            else:   
                player.jumpcount=10
                player.isjump=False
        
        if player.iscollision(enemy.x,enemy.y):
            player.hit()

        

        draw_window()
        pg.display.update()
        

pg.quit()