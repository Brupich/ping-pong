from pygame import *


font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 2 WIN', True, (180, 0, 0))
lose2 = font1.render('PLAYER 1 WIN', True, (180, 0, 0))


win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("Ping-Pong")

background = transform.scale(image.load("пинг понг.jpg"), (win_width, win_height+10))
 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

#class Ball(GameSprite):
#    
#    def update(self):
#        
#        if self.rect.y <= 5 or self.rect.y >= win_height - 50:
#            speed_y *= -1
#
#        self.rect.x += speed_x
#        self.rect.y += speed_y
        
             

speed_x = 3
speed_y = 3
racket1 = Player('ракетка для тениса.jpg', 100, 250, 50, 150, 5)
racket2 = Player('ракетка для тениса.jpg', 550, 250, 50, 150, 5)
ball = GameSprite('мячик.jpg', 352, 236, 50, 50, 1)

FPS = 60
clock = time.Clock()

finish = False
game = True
while game:
    clock.tick(FPS)
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    

    if finish != True:
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        
        
        window.blit(background,(0,0))
        racket1.update_1()
        racket2.update_2()
        racket1.reset()
        racket2.reset()
#        ball.update()
        ball.reset()


        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > 650:
            finish = True
            window.blit(lose2, (200, 200))


        display.update()