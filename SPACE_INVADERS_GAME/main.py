import pygame as pg
import random
import math

# this class consists of the all type of movements and actions for bullet like 
# -----------show bullets
# -----------shoot bullets
# -----------speed of bullets..
class Bullet:
    def __init__(self,x,y,dim,speed):
        self.x=x
        self.y=y
        self.dim=dim
        self.speed=speed        
    # this function checks collision by math formula for distance 
    # and if it collide than return true else it return false
    def isCollision(self,enemy_x,enemy_y,bullet_x,bullet_y):
        res=math.sqrt((math.pow(enemy_x-bullet_x,2))+(math.pow(enemy_y-bullet_y,2)))
        if res<=64:
            return True
        else:
            return False
    # this method checks collision between player and enemy
    def isCollision_with_player(self,enemy_x,enemy_y,player_x,player_y):
        res=math.sqrt((math.pow(enemy_x-player_x,2))+(math.pow(enemy_y-player_y,2)))
        if res<=32:
            return True
        else:
            return False
    
    # this method just show or displays the image of bullet
    def show_shooting(self,window,x,y,bullet_img):
        window.blit(bullet_img,(x,y))
#this class is for enemy the actions and movements of enemy
class Enemy:
    def __init__(self,x,y,speed,dim):
        self.x=x#array of distance from x
        self.y=y#array of distance from y
        self.speed=speed#array of speed of enemy's movement
        self.dim=dim    
    # this method simply show or display the images of all the 6 or multiple enemy's
    def draw(self,window,enemy_image,i):
        window.blit(enemy_image[i],(self.x[i],self.y[i]))
    # this method stands for the movement automatically done by enemy's
    def move(self):
        # here  we create and random array of speed hope you will see the  game has random speed of enemy's
        newspeed_y=[random.randint(5,15) for i in range(6)]
        # here will adjust the each enemy's movement and check if the hits lower or upper boundry  or not if it hits than will perform appropriate operation according to it
        for  i in range(6):
            if self.x[i]<=0:
                self.speed[i]=abs(self.speed[i])
                self.y[i]+=newspeed_y[i]
            if self.x[i]>=852-64:
                self.speed[i]=self.speed[i] * (-1)
                self.y[i]+=newspeed_y[i]
            self.x[i]+=self.speed[i]
# this class is for player the actions and movements of player
class Player:
    # here we initialise the coordinates of player x,y or speed or dimantions(64*64 or 32*32)
    def __init__(self,x,y,speed,dim):
        self.x=x
        self.y=y
        self.speed=speed
        self.dim=dim
    # this method simply display or show our player
    def draw(self,window,player_img):
        window.blit(player_img,(self.x,self.y))
# this is the main or heart of this game all actions and logic are performed here
class Main:
    # here we initialise the thing which we want in this whole game so not have to initialize again and again
    def __init__(self,window):
        self.window=window
        self.window_width=852
        self.window_height=480
        self.bg=pg.image.load("bg.jpg")
        self.player_img=pg.image.load("player.png")
        self.enemy_img=pg.image.load("enemy.png")
        self.bullet_img=pg.image.load("bullet.png")

    # this method consists of all the movement actions interations and decision based on moves player apply
    def main(self):
        game_loop=True
        fps=120
        score=0
        bullet_x=0
        clock=pg.time.Clock()

        # play the background sound
        pg.mixer.music.load("bg.mp3")
        pg.mixer.music.play(-1)
        
        
        # make player
        player=Player(self.window_width//2-64,self.window_height-74,5,64)

        # make enemy
        enemy_x=[]
        enemy_y=[]
        enemy_images=[]
        speed=[]
        no_of_enemy=6
        for i in range(no_of_enemy):
            enemy_x.append(random.randint(0,self.window_width))
            enemy_y.append(random.randint(0,250))
            enemy_images.append(pg.image.load("enemy.png"))
            speed.append(random.uniform(0,0.5))
        enemy=Enemy(enemy_x,enemy_y,speed,64)

        # make bullet
        bullet=Bullet(self.window_width//2+13,self.window_height-player.dim//2-16,32,10)
        flag=False #if flag==True then shoot bullet

        
        # our forever loop by we show all the frames continously that non-programmer think this is actual object is moving but its not its just images which chanage its coordinates soo quickly that it create illusion that object is moving
        while game_loop:

            # this is fps for better interation the higher the fps the higher the speed 
            clock.tick(fps)

            self.window.blit(self.bg,(0,0))
            
            # all the keys is pressed by keyboard or button of windows is an event
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    game_loop=False
            
            keys=pg.key.get_pressed()
            # move left
            if keys[pg.K_LEFT]:
                # set boundry
                if player.x>player.speed:
                    player.x-=player.speed

            # move  right
            if keys[pg.K_RIGHT]:
                # set boundry
                if player.x<self.window_width-player.dim:
                    player.x+=player.speed

            # shoot bullet
            if keys[pg.K_SPACE]:
                if flag==False:
                    bullet_x=player.x
                    # bullet is ready to shoot
                    flag=True
                    gun_sound=pg.mixer.Sound("gunshoot.mp3")
                    gun_sound.play()

            # bullet is ready not fire it so this fires the bullet
            if flag==True:
                if bullet.y>=0:
                    bullet.y-=bullet.speed
                    bullet.show_shooting(self.window,bullet_x,bullet.y,self.bullet_img)
                else:
                    bullet.y=player.y
                    flag=False
            
        
            for i in range(no_of_enemy):
                # if bullet is collide with enemy than  increase score and put that enemy at initial random position and play sound
                if bullet.isCollision_with_player(enemy_x[i],enemy_y[i],player.x,player.y):
                    for j in range(no_of_enemy):
                        enemy_y[j]=2000
                    font2=pg.font.SysFont("arialblack",64)
                    game_over=font2.render("GAME OVER",True,(255,0,0))
                    self.window.blit(game_over,(250,200))

                if bullet.isCollision(enemy_x[i],enemy_y[i],bullet_x,bullet.y):
                    hit_sound=pg.mixer.Sound("enemy_hit.mp3")
                    hit_sound.play()    
                    score+=1
                    enemy_x[i]=random.randint(0,852-64)
                    enemy_y[i]=random.randint(0,250)
                    bullet.y=player.y
                    flag=False

                # if one of enemy out of all the enemys get out of boundry means touches our player than it's mean game over than remove all enemy rather than delete or unshow images we simply put the enemy's out of screen boundry that no one sees it and game over means close the screen 

                enemy.move()
                # draw enemy
                enemy.draw(self.window,enemy_images,i)

            # display score
            font=pg.font.SysFont("arialblack",32)
            text=font.render(f"Score : {score}",True,(0,0,0))
            self.window.blit(text,(0,0))

            # move our enemy
                
                # draw player
            player.draw(self.window,self.player_img)
            pg.display.update()    

if __name__ == '__main__':
    
    # initialization of pygame module with all of its library
    pg.init()
        
    # set icon for game  
    icon=pg.image.load("icon.png")
    pg.display.set_icon(icon)

    pg.display.set_caption("SPACE INVADERS")

    # create and window of width 852 and height 480
    window=pg.display.set_mode((852,480))

    # Main class consists of the algorithm or the program by which we interact with window so m is an object 
    m=Main(window)

    # method for interation with window
    m.main()
