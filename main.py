import pygame # Pygame importálás
import os #Operating System

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

    # Konstruktor
    def __init__(self):

        # Képek átadása
        self.sneak_img = sneaking
        self.run_img = running
        self.jump_img = jumping

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
        pass
    
    # Ugrás
    def jump(self):
        pass

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_box.x, self.dino_box.y))

# Main function - később hasznos lesz a menü létrehozásában
def main():
    run = True # Játék állapota
    clock = pygame.time.Clock() # Időmérő létrehozása

    # Player példányosítása
    player = Player()


    # Ablak futtatása
    while run:

        # Lehetőség a játékból való kilépésre ha a felhasználó megnyomja az X-et a sarokban
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Fehér képernyő létrehozása 
        main_screen.fill((255,255,255))

        # A felhasználó által lenyomott gomb
        userInput = pygame.key.get_pressed()

        # Player megjelenítése
        player.draw(main_screen)

        # Lenyomott billentyű átadása
        player.update(userInput)

        # Clock tick megadása
        clock.tick(30)

        # Képernyő update
        pygame.display.update()

# Main hívás
main()