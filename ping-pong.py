from sys import *
from pygame import *


font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 2 WIN', True, (90, 50, 50))
lose2 = font1.render('PLAYER 1 WIN', True, (90, 50, 50))




button_easy = Surface((150, 50))
button_normal = Surface((150, 50))
button_hard = Surface((150, 50))
button_impossible = Surface((150, 50))

text_easy = font1.render("Easy", True, (10, 70, 50))
text_easy_rect = text_easy.get_rect(center=(button_easy.get_width() /2, button_easy.get_height()/2))
button_easy_rect = Rect(300, 125, 100, 50)


text_normal = font1.render("Normal", True, (251, 246, 2))
text_normal_rect = text_normal.get_rect(center=(button_normal.get_width() /2, button_normal.get_height()/2))
button_normal_rect = Rect(300, 200, 100, 50)


text_hard = font1.render("Hard", True, (251, 151, 2))
text_hard_rect = text_hard.get_rect(center=(button_hard.get_width() /2, button_hard.get_height()/2))
button_hard_rect = Rect(300, 275, 100, 50)

text_impossible = font1.render("Impossible", True, (251, 2, 2))
text_impossible_rect = text_impossible.get_rect(center=(button_impossible.get_width() /2, button_impossible.get_height()/2))
button_impossible_rect = Rect(300, 350, 100, 50)





win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("Ping-Pong")


background_game = transform.scale(image.load("пинг понг.jpg"), (win_width, win_height+10))
background_menu = transform.scale(image.load("фон-меню.jpg"), (win_width, win_height+10))

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
            

speed_x = 3
speed_y = 3
racket1 = Player('ракетка для тениса.jpg', 100, 250, 40, 150, 5)
racket2 = Player('ракетка для тениса.jpg', 550, 250, 40, 150, 5)
ball = GameSprite('мячик.jpg', 352, 236, 70, 70, 1)

FPS = 60
clock = time.Clock()

menu = True
finish = False
game = True
while game:
    clock.tick(FPS)
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            
            if button_easy_rect.collidepoint(e.pos):
                ball = GameSprite('мячик.jpg', 352, 236, 70, 70, 1)
                speed_x = 2
                speed_y = 2
                menu = False
            
            if button_normal_rect.collidepoint(e.pos):
                ball = GameSprite('мячик.jpg', 352, 236, 50, 50, 3)
                speed_x = 4
                speed_y = 4
                menu = False
            
            if button_hard_rect.collidepoint(e.pos):
                ball = GameSprite('мячик.jpg', 352, 236, 40, 40, 6)
                speed_x = 5
                speed_y = 5
                menu = False

            if button_impossible_rect.collidepoint(e.pos):
                ball = GameSprite('мячик.jpg', 352, 236, 20, 20, 6)
                speed_x = 7
                speed_y = 8
                menu = False
    

    if finish != True:
        
        if menu == True:
            window.blit(background_menu,(0,0))
            
            button_easy.blit(text_easy, text_easy_rect)
            window.blit(button_easy, (button_easy_rect.x, button_easy_rect.y))

            button_normal.blit(text_normal, text_normal_rect)
            window.blit(button_normal, (button_normal_rect.x, button_normal_rect.y))

            button_hard.blit(text_hard, text_hard_rect)
            window.blit(button_hard, (button_hard_rect.x, button_hard_rect.y))

            button_impossible.blit(text_impossible, text_impossible_rect)
            window.blit(button_impossible, (button_impossible_rect.x, button_impossible_rect.y))
        
        else:    
            ball.rect.x += speed_x
            ball.rect.y += speed_y

            if ball.rect.y > win_height - 50 or ball.rect.y < 0:
                speed_y *= -1

            if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
                speed_x *= -1
                speed_y *= 1
            
            
            window.blit(background_game,(0,0))
            racket1.update_1()
            racket2.update_2()
            racket1.reset()
            racket2.reset()
            ball.reset()


            if ball.rect.x < 0:
                finish = True
                window.blit(lose1, (200, 200))

            if ball.rect.x > 650:
                finish = True
                window.blit(lose2, (200, 200))
        
        



        display.update()