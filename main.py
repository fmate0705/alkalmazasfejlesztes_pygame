import pygame # Pygame importálás
import os #Operating System
import random # Random modul - random számok generálása

pygame.init() # Pygame inicializálás

# Globális változók
screen_height = 600
screen_width = 1100

# Képernyő létrehozása
main_screen = pygame.display.set_mode((screen_width,screen_height))

# Sprite-ok betöltése

# Dinó futás
running = [pygame.image.load(os.path.join("Sprites/Dino", "DinoRun1.png")),
            pygame.image.load(os.path.join("Sprites/Dino", "DinoRun2.png"))]

# Dínó ugrás
jumping = pygame.image.load(os.path.join("Sprites/Dino", "DinoJump.png"))
sneaking = [pygame.image.load(os.path.join("Sprites/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Sprites/Dino", "DinoDuck2.png"))]

# Kaktuszok
small_cactus = [pygame.image.load(os.path.join("Sprites/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Sprites/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Sprites/Cactus", "SmallCactus3.png"))]
large_cactus = [pygame.image.load(os.path.join("Sprites/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Sprites/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Sprites/Cactus", "LargeCactus3.png"))]

# Madár
bird = [pygame.image.load(os.path.join("Sprites/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Sprites/Bird", "Bird2.png"))]

# Felhő
cloud = pygame.image.load(os.path.join("Sprites/Other", "Cloud.png"))

# Háttér / track
background = pygame.image.load(os.path.join("Sprites/Other", "Track.png"))

# Player class létrehozása
class Player:

    # Alap pozíció
    x = 80
    y = 310

    y_sneak = 340
    jump_velocity = 8.5

    # Konstruktor
    def __init__(self):

        # Képek átadása
        self.sneak_img = sneaking
        self.run_img = running
        self.jump_img = jumping

        # Ugráshoz szükséges változó
        self.jump_vel = self.jump_velocity # Hiba javítás

        # A játékos állapota
        self.dino_run = True
        self.dino_sneak = False
        self.dino_jump = False

        self.step_index = 0 # Lépések indexe - Animációnál lesz hasznos
        self.image = self.run_img[0] # A jelenlegi sprite tárolása
        self.dino_box = self.image.get_rect() # Hitbox létrehozása
        self.dino_box.x = self.x
        self.dino_box.y = self.y

    def update(self,userInput):

        # A dínó állapota alapján meghívjuk a megfelelő functiont
        if self.dino_sneak:
            self.sneak()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        # Step index - max 10-ig mehet utána 0 lesz - Animációban segít
        if self.step_index >= 10:
            self.step_index = 0
        
        # A dínó állapotának beállítása - Ha a felhasználó megnyom egy gombot és lehetséges az állapotváltás
        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_sneak = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_sneak = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_sneak = False
            self.dino_run = True
            self.dino_jump = False

    # Futás
    def run(self):
        self.image = self.run_img[self.step_index // 5] # Futás animáció
        self.dino_box = self.image.get_rect() # Hitbox
        self.dino_box.x = self.x
        self.dino_box.y = self.y

        # step_index növelése - minden update-nál
        self.step_index += 1

    # Sneak
    def sneak(self):
        self.image = self.sneak_img[self.step_index // 5] # Futás animáció
        self.dino_box = self.image.get_rect() # Hitbox
        self.dino_box.x = self.x
        self.dino_box.y = self.y_sneak

        # step_index növelése - minden update-nál
        self.step_index += 1
    
    # Ugrás
    def jump(self):
        self.image = self.jump_img # Ugrás kép
        if self.dino_jump: # Ha a ugrik
            self.dino_box.y -= self.jump_vel * 4 # Ha eléri a csúcsot akkor 0 lesz, innentől negatívba megy ezér elkezd lefelé esni.
            self.jump_vel -= 0.8 # jump_vel csökkentése

        if self.jump_vel < - self.jump_velocity: #Ha a jump_vel eléri az ugás magasság negatív értékét akkor leesett a földre
            self.dino_jump = False # Ugrás állapot leállítása
            self.jump_vel = self.jump_velocity # jump_vel visszaállítása

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_box.x, self.dino_box.y))


# Felhő osztály
class Cloud:
    def __init__(self):
        self.x = screen_width + random.randint(800,1000) # Random felhő spawnolás - A felhő a képernyőn kívül random távolságra spawnol
        self.y = random.randint(50,100) # Random magasság
        self.image = cloud # Sprite beállítása
        self.width = self.image.get_width() # Sprite szélességének leérése

    def update(self):
        self.x -= game_speed # Felhő mozgatása

        # Ha a felhő lemegy a képernyőről akkor visszakerül egy random x kordinátára a képernyőn kívül
        if self.x < -self.width:
            self.x = screen_width + random.randint(2500, 3000)
            self.y = random.randint(50, 100) # + Egy másik random magasságba

    def draw(self,SCREEN):
        SCREEN.blit(self.image, (self.x, self.y)) # Megjelenítés a képernyőn
    

# Obstacle parrent class
class Obstacle:
    def __init__(self,image,OBStype):
        self.image = image
        self.type = OBStype # Akadály típus 0..2
        self.rect = self.image[self.type].get_rect() # Akadály hitbox
        self.rect.x = screen_width # A képernyő végé lesz az x kordináta

    def update(self):
        self.rect.x -= game_speed # X kordináta változtatása a game_speed globális változó alapján
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self,SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

# Kis kaktusz osztály
class SmallCactus(Obstacle):
    def __init__(self,image):
        self.type = random.randint(0,2) # Random típus kiválasztás
        super().__init__(image, self.type) # Parent konstruktor hívás
        self.rect.y = 325 # y kordináta

# Nagy kaktusz osztály - Ugyanaz mint a kis kaktusz, viszont lentebb kell megjeleníteni a képernyőn
class LargeCactus(Obstacle):
    def __init__(self,image):
        self.type = random.randint(0,2) # Random típus kiválasztás
        super().__init__(image, self.type) # Parent konstruktor hívás
        self.rect.y = 300 # y kordináta

# Madár / Terodaktilusz osztály - Örököl az Obstacle osztályból
class Bird(Obstacle):
    def __init__(self,image):
        self.type = 0
        super().__init__(image,self.type)
        self.rect.y = 250
        self.index = 0
    
    def draw(self,SCREEN): # Felülírja a parent class draw() function-t : A madár animált, illetve nem kaktusz típusú
        if self.index >= 9: # HA az index nagyobb vagy egyenlő mint 9 akkor nullázódik
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect) # Madár megjelenítése
        self.index += 1 # Index növelése

# Main function - később hasznos lesz a menü létrehozásában
def main():
    # Globális változók létrehozása
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True # Játék állapota
    clock = pygame.time.Clock() # Időmérő létrehozása

    # Globális változók incializálása
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0

    font = pygame.font.Font('freesansbold.ttf', 20) # Betűtípus létrehozása a kiiratáshoz

    obstacles = [] # Akadályok tömb az akadályok tárolására

    def score():
        global points,game_speed
        points += 1 # Pontok növelése minden hívásnál - minden képfrissítésnél
        if points % 100 == 0:
            game_speed += 1 # Játék sebességének a növelése minden 100 pont után
        
        # Pontok megjelenítése
        text = font.render(str(points), True, (0, 0, 0))
        textRect = text.get_rect() 
        textRect.center = (1000, 40) # Jobb felső sarokba helyezés
        main_screen.blit(text, textRect) # Megjelenítés

    # Háttér
    def bg():
        global x_pos_bg, y_pos_bg
        bg_img_width = background.get_width() # Háttér szélességének lekérése
        main_screen.blit(background, (x_pos_bg, y_pos_bg)) # Háttér megjelenítés
        main_screen.blit(background, (bg_img_width + x_pos_bg, y_pos_bg)) # Második háttér megjelenítése
        # Ha az első háttér lemegy a képről akkor a második következik utána - végtelenül ismétlődik a háttér
        if x_pos_bg <= - bg_img_width:
            main_screen.blit(background, (bg_img_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed # Háttér mozgatása

    # Player példányosítása
    player = Player()

    # Felhő példányosítása
    cloud = Cloud()

    # Ablak futtatása
    while run:

        # Lehetőség a játékból való kilépésre ha a felhasználó megnyomja az X-et a sarokban
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Fehér képernyő létrehozása 
        main_screen.fill((255,255,255))

        userInput = pygame.key.get_pressed() # A felhasználó által lenyomott gomb

        player.draw(main_screen) # Player megjelenítése
        player.update(userInput) # Lenyomott billentyű átadása

        if len(obstacles) == 0: # HA nincs a képernyőn akadály akkor random létrehozunk egyet
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(small_cactus)) # Kis kaktusz létrehozása
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(large_cactus)) # Nagy kaktusz létrehozása
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(bird)) # Madár létrehozása

        for obstacle in obstacles: # Akadályok végig-iterálása
            obstacle.draw(main_screen) # Akadály megjelenítése
            obstacle.update() # Akadály mozgatása
            if player.dino_box.colliderect(obstacle.rect): # HA a player hozzáér az akadály hitboxához
                pygame.draw.rect(main_screen,(0,0,0),player.dino_box,2) # Fekete négyzet kirajzolása

        cloud.draw(main_screen) # Felhő megjelenítése
        cloud.update() #Felhő mozgatása
        
        score() # Pontok létrehozása

        bg() # Background létrehozása

        # Clock tick megadása
        clock.tick(30)

        # Képernyő update
        pygame.display.update()

# Main hívás
main()