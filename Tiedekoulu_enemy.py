import sys

import pygame # sisällytetään pygame

pygame.init() # alustetaan Pygame -kirjasto

GREEN = (0, 255, 0) # määritellään vihreä väri 
BLUE = (0, 0, 128) # määritellään sininen väri
SURFACE_COLOR = (0, 255, 0) # määritellään pinnan väri
SURFACE_FILL = (97, 51, 24) # määritellään pinnan alaosan väri

# tästä voi muuttaa ikkunan kokoa
size = [1100, 500]

win = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.display.set_caption("Vastustaja")

# luodaan listat hahmon liikkeen animointia varten
walk_right = [pygame.image.load('Tiedekoulurobo_juoksee1.png'), \
             pygame.image.load('Tiedekoulurobo_juoksee2.png'), \
             pygame.image.load('Tiedekoulurobo_juoksee3.png'), \
             pygame.image.load('Tiedekoulurobo_juoksee4.png'), \
             pygame.image.load('Tiedekoulurobo_juoksee5.png'), \
             pygame.image.load('Tiedekoulurobo_juoksee6.png'), \
             pygame.image.load('Tiedekoulurobo_juoksee7.png'), \
             pygame.image.load('Tiedekoulurobo_juoksee8.png'), \
             pygame.image.load('Tiedekoulurobo_juoksee9.png'),\
             pygame.image.load('Tiedekoulurobo_juoksee10.png')]
walk_left = [pygame.image.load('Tiedekoulurobo_juoksee_vasen1.png'), \
            pygame.image.load('Tiedekoulurobo_juoksee_vasen2.png'), \
            pygame.image.load('Tiedekoulurobo_juoksee_vasen3.png'), \
            pygame.image.load('Tiedekoulurobo_juoksee_vasen4.png'), \
            pygame.image.load('Tiedekoulurobo_juoksee_vasen5.png'), \
            pygame.image.load('Tiedekoulurobo_juoksee_vasen6.png'), \
            pygame.image.load('Tiedekoulurobo_juoksee_vasen7.png'), \
            pygame.image.load('Tiedekoulurobo_juoksee_vasen8.png'), \
            pygame.image.load('Tiedekoulurobo_juoksee_vasen9.png'), \
            pygame.image.load('Tiedekoulurobo_juoksee_vasen10.png')]
char = pygame.image.load('Tiedekoulurobo1.png')

# piirrettävän pinnan koordinaatit
a = [0, 283]
b = [150,283]
c = [150,450]
d = [500,450]
e = [500,283]
f = [1100,283]

# luodaan Sprite luokka, jonka avulla pystytään määrittelemään hahmoja peliin
class Sprite(pygame.sprite.Sprite):
    # luontimetodi
    def __init__(self, x, y, width, height, velocity, gravity, jump_velocity, time, walk_count, is_gravity, left, right, is_jump, surface):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.gravity = gravity
        self.jump_velocity = jump_velocity
        self.time = time
        self.walk_count = walk_count
        self.is_gravity = is_gravity
        self.left = left
        self.right = right
        self.is_jump = is_jump
        self.surface = surface

    # funktio, jolla hahmo liikkuu oikealle
    def move_right(self):
        self.x += self.velocity
        self.left = False
        self.right = True
        
    # funktio, jolla hahmo liikkuu vasemmalle
    def move_left(self):
        self.x -= self.velocity
        self.left = True
        self.right = False

    # funktio, jolla hahmo liikkuu ylös
    def move_up(self):
        self.y -= self.velocity

    # funktio, jolla hahmo liikkuu alas
    def move_down(self):
        self.y += self.velocity

    # funktio, jolla hahmo seisoo
    def stand(self):
        self.left = False
        self.right = False
        self.walk_count = 0

    # funktio, jolla hahmo hyppää
    def jump(self):
        self.is_jump = True
        self.y -= 1
        self.right = False
        self.left = False
        self.walk_count = 0

    # funktio, jolla hahmo laskeutuu
    def landing(self):
        if self.is_gravity and self.y < size[0] - self.height :
            self.y -= (self.jump_velocity - self.gravity*self.time)
            if self.y > self.surface:
                self.y = self.surface
            self.time += 1
        else:
            self.is_jump = False
            self.time = 0

    # funktio, joka määrittää painovoiman
    def use_gravity(self):
        self.is_gravity = True
        if not(self.is_jump):
            self.y += self.gravity*self.time
            if self.y > self.surface:
                self.y = self.surface
            self.time += 1

# annetaan muuttujat Sprite luokalle

# pelaajan x ja y sijanti, sekä nopeus pelin alussa
player_x = 50
player_y = 50
player_velocity = 5 # pelaajan nopeus

# vastustajan x ja y sijainti, sekä nopeus pelin alussa
enemy_x = 1000
enemy_y = 100
enemy_velocity = 3 # vastustajan nopeus

width = 40 # hahmon leveys
height = 60 # hahmon korkeus
gravity = 0.3 # painovoiman vaikutuksen luomiseen käytettävä putoamiskiihtyvvyys
jump_velocity = 10 # hypyn lähtönopeus
time = 0 # aika
walk_count = 0 # Walk count animaatiota varten
is_gravity = False # Tarkastus, että onko painovoima päällä?
left = False # vasen
right = False # oikea
is_jump = False # Tarkastus, että on hyppy päällä?
surface = 250 # Pinta

# luodaan player olio Sprite-luokan avulla
player = Sprite(player_x, player_y, width, height, player_velocity, gravity, jump_velocity, time, walk_count, is_gravity, left, right, is_jump, surface)

# luodaan enemy olio Sprite-luokan avulla
enemy = Sprite(enemy_x, enemy_y, width, height, enemy_velocity, gravity, jump_velocity, time, walk_count, is_gravity, left, right, is_jump, surface)

# luodaan redraw_game_window() -funktio jolla piirretään ruudulle
def redraw_game_window():
    
    win.fill((135,206,235))

    # piirretään pinta
    pygame.draw.lines(win, SURFACE_COLOR, False, [a, b, c, d, e, f], 5)

    # värjätään pinnan alaosa piirtämällä sinne ruskea saman muotoinen kulmio
    pygame.draw.polygon(win, SURFACE_FILL, \
                        [(0, size[1]), a, b, c, d, e, f, size])

    # pelaajan animaatio
    if player.walk_count + 1 >= 29:
        player.walk_count = 0
        
    if player.left:
        win.blit(walk_left[player.walk_count//3], (player.x,player.y))
        player.walk_count += 1
    elif player.right:
        win.blit(walk_right[player.walk_count//3], (player.x,player.y))
        player.walk_count += 1
    else:
        win.blit(char, [player.x,player.y])

    # vastustajan animaatio
    if enemy.walk_count + 1 >= 29:
        enemy.walk_count = 0
        
    if enemy.left:
        win.blit(walk_left[enemy.walk_count//3], (enemy.x,enemy.y))
        enemy.walk_count += 1
    elif enemy.right:
        win.blit(walk_right[enemy.walk_count//3], (enemy.x,enemy.y))
        enemy.walk_count += 1
    else:
        win.blit(char, [enemy.x,enemy.y])

    # piirretään teksti uudulle
    win.blit(text, textRect) 

    # päivitetään ruutu
    pygame.display.update()

# tehdään pelisilmukka, jossa peli pyörii

run = True
    
while run:
    clock.tick(29)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # vaihdetaan kuopan pohja pelaajalle pinnaksi jos ollaan kuopassa
    if c[0] <= player.x <= d[0] - 35:
        player.surface = c[1] - 33
    else:
        player.surface = 250

    # vaihdetaan kuopan pohja vastustajalle pinnaksi jos ollaan kuopassa
    if c[0] <= enemy.x <= d[0] - 35:
        enemy.surface = c[1] - 33
    else:
        enemy.surface = 250
        
    # laitetaan pelaajalle painovoima päälle jos ollaan pinnan yläpuolella
    if player.y < player.surface:
        player.use_gravity()
    else:
        player.is_gravity = False
        player.time = 0

    # laitetaan vastustajalle painovoima päälle jos ollaan pinnan yläpuolella
    if enemy.y < enemy.surface:
        enemy.use_gravity()
    else:
        enemy.is_gravity = False
        enemy.time = 0

    # luetaan syöte
    keys = pygame.key.get_pressed()

    # vähentää pelaajan painovoimaa
    if keys[pygame.K_UP]:
        player.gravity -= 0.1

    # lisää pelaajan painovoimaa
    if keys[pygame.K_DOWN]:
        player.gravity += 0.1

    # tekstin tulostaminen ruudulle
    font = pygame.font.Font('freesansbold.ttf', 32) # määrittää fontin
    g_text = player.gravity # sijoittaa g arvon muuttujaan g_text
    g_text = round(g_text, 3) # pyöristää muuttujan g_text kolmeen desimaaliin
    text = font.render('Putoamiskiihtyvyys ' + str(g_text), True, GREEN, BLUE) # renderöi Painovoima tekstin ja muuttaa g_text muuttujan merkkijonoksi
    textRect = text.get_rect() # rakentaa tekstineliön
    win.blit(text, textRect)  # renderöi tekstineliön ruudulle

    # pelihahmon liikkeet
    if keys[pygame.K_LEFT] and player.x > 0 and not(player.x <= b[0] and player.y > b[1] - 33):
        player.move_left()

    elif keys[pygame.K_RIGHT] and player.x < size[0] - player.width \
        and not(player.x >= e[0] - 35 and player.y > e[1] - 33):
        player.move_right()
        
    else:
        player.stand()
        
    if not(player.is_jump):
        if keys[pygame.K_SPACE]:
            player.jump()
    else:
        player.landing()

    # vastustajan liikkeet

    if player.x < enemy.x and enemy.x > 0 and not(enemy.x <= b[0] and enemy.y > b[1] - 33):
        enemy.move_left()

    elif player.x > enemy.x and enemy.x < size[0] - enemy.width \
        and not(enemy.x >= e[0] - 35 and enemy.y > e[1] - 33):
        enemy.move_right()

    else:
        enemy.stand()
    
    if enemy.x > 150 and enemy.x < 500 and not(enemy.is_jump):
        enemy.jump()
    else:
        enemy.landing()

    # muutetaan x ja y koordinaatit kokonaisluvuiksi pelaajalla
    player.x = int(player.x)
    player.y = int(player.y)

    # muutetaan x ja y koordinaatit kokonaisluvuiksi vastustajalla
    enemy.x = int(enemy.x)
    enemy.y = int(enemy.y)
    
    redraw_game_window()
pygame.quit()
