from pygame import *


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
        if keys[K_s] and self.rect.y < win_width - 350:
            self.rect.y += self.speed
    
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 580:
            self.rect.y += self.speed

player1 = Player('ракетка для тениса.jpg', 100, 250, 50, 150, 5)
player2 = Player('ракетка для тениса.jpg', 600, 250, 50, 150, 5)

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
        window.blit(background,(0,0))
        player1.update_1()
        player2.update_2()
        player1.reset()
        player2.reset()

        display.update()