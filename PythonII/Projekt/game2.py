from adds import *

pygame.init()

# centrowanie okna
os.environ['SDL_VIDEO_CENTERED'] = '1'


pygame.display.set_caption('Alienkowo')
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.items = set()
        self.movement_x = 0
        self.movement_y = 0
        self._count = 0
        self.lifes = 3
        self.level = None
        self.direction_of_movement = 'right'
        self.advance = 0

    def turn_right(self):
        if self.direction_of_movement != 'right':
            self.direction_of_movement = 'right'
        self.movement_x = 8

    def turn_left(self):
        if self.direction_of_movement != 'left':
            self.direction_of_movement = 'left'
        self.movement_x = -8

    def turn_up(self):
        if self.direction_of_movement != 'up':
            self.direction_of_movement = 'up'
        self.movement_y = -8

    def turn_down(self):
        if self.direction_of_movement != 'down':
            self.direction_of_movement = 'down'
        self.movement_y = 8

    def stop(self):
        self.movement_x = 0
        self.movement_y = 0


    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def _move(self, image_list):
        if self._count < 4:
            self.image = image_list[0]
        elif self._count < 8:
            self.image = image_list[1]

        if self._count >= 8:
            self._count  = 0
        else:
            self._count += 1

    def update(self):
        # --------------ruch w poziomie---------------
        self.rect.x += self.movement_x

        # sprawdzanie kolizji
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms, False)

        for p in colliding_platforms:
            if self.movement_x > 0:
                self.rect.right = p.rect.left
            if self.movement_x < 0:
                self.rect.left = p.rect.right

        # animacje
        if self.movement_x > 0:
            self._move(image_right)
        if self.movement_x < 0:
            self._move(image_left)
        if self.movement_y > 0:
            self._move(image_right)
        if self.movement_y < 0:
            self._move(image_up)


        # --------------ruch w pionie---------------
        self.rect.y += self.movement_y
        # sprawdzanie kolizji
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms, False)
        for p in colliding_platforms:
            if self.movement_y > 0:
                self.rect.bottom = p.rect.top
            if self.movement_y < 0:
                self.rect.top = p.rect.bottom



        # sprawdzenie kolizji z przedmiotami
        colliding_items = pygame.sprite.spritecollide(
            self, self.level.set_of_items, False)
        for item in colliding_items:
            if item.name == 'drug':
                if self.lifes < 3:
                    self.lifes += 1
                    item.kill()
            if item.name == 'friend1':
                self.items.add('friend1')
                item.kill()
            if item.name == 'friend2':
                self.items.add('friend2')
                item.kill()
            if item.name == 'friend3':
                self.items.add('friend3')
                item.kill()
            if item.name == 'friend4':
                self.items.add('friend4')
                item.kill()
            if item.name == 'n_lvl':
                if len(self.items) == 4:
                    self.advance +=1
                else:
                    Screen_text('Musisz zabrać ze sobą swoich 4 przyjaciół!')


        #Kolizja z rakieta/gwiazdka
        colliding_enemy = pygame.sprite.spritecollide(self, blocksGroup, False)
        for killer in colliding_enemy:
            if self.lifes:
                self.lifes -= 1
                PAIN.play()
                player.rect.center = [880, 590]


        if self.lifes:
            for i in range(self.lifes):
                screen.blit(HEART, [30 * i, 20])



    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.turn_right()
            if event.key == pygame.K_LEFT:
                self.turn_left()
            if event.key == pygame.K_UP:
                self.turn_up()
            if event.key == pygame.K_DOWN:
                self.turn_down()


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.stop()
                self.image = stand_R
            if event.key == pygame.K_LEFT:
                self.stop()
                self.image = stand_L
            if event.key == pygame.K_UP:
                self.stop()
                self.image = up_R
            if event.key == pygame.K_DOWN:
                self.stop()
                self.image = stand_R

class Level:
    def __init__(self, player):
        self.set_of_platforms = set()
        self.player = player
        self.set_of_items = pygame.sprite.Group()


    def update(self):
        for platform in self.set_of_platforms:
            platform.update()

        blocksGroup.update()

    def draw(self, surface):
        for platform in self.set_of_platforms:
            platform.draw(surface, GROUND_LIST)

        self.set_of_items.draw(surface)
        blocksGroup.draw(surface)

class Level_1(Level):
    def __init__(self, player):
        super().__init__(player)
        platforms = [[300,60,724,640], [2, 700, 1024, 0], [2, 700, 0, 0], [1024, 2, 0, 700], [700,1, 0,0], [150, 1, 850, 0]]

        # tworzymy platformy statyczne
        for el in platforms:
            object_P = Platform(LVL1B, *el)
            self.set_of_platforms.add(object_P)



        spaceship = Enemy(LVL1B, SPACE_R, 0, 200, 7, 0)
        blocksGroup.add(spaceship)

        star1 = Enemy(LVL1B, STAR, 200, 20, 0, 4)
        blocksGroup.add(star1)

        star2 = Enemy(LVL1B, STAR, 300, 20, 0, 8)
        blocksGroup.add(star2)

        star3 = Enemy(LVL1B, STAR, 400, 20, 0, 6)
        blocksGroup.add(star3)

        star4 = Enemy(LVL1B, STAR, 500, 20, 0, 12)
        blocksGroup.add(star4)

        star5 = Enemy(LVL1B, STAR, 100, 20, 0, 8)
        blocksGroup.add(star5)


        # tworzymy przedmiot (tabletke)
        drug = Item(DRUG, 'drug')
        drug.rect.x = 80
        drug.rect.bottom = 150
        self.set_of_items.add(drug)

        #przyjaciel
        friend1 = Item(FRIEND1, 'friend1')
        friend1.rect.x = 10
        friend1.rect.bottom = 180
        self.set_of_items.add(friend1)

        # przyjaciel
        friend2 = Item(FRIEND2, 'friend2')
        friend2.rect.x = 150
        friend2.rect.bottom = 600
        self.set_of_items.add(friend2)

        # przyjaciel
        friend3 = Item(FRIEND3, 'friend3')
        friend3.rect.x = 500
        friend3.rect.bottom = 200
        self.set_of_items.add(friend3)

        # przyjaciel
        friend4 = Item(FRIEND4, 'friend4')
        friend4.rect.x = 350
        friend4.rect.bottom = 180
        self.set_of_items.add(friend4)

        #platforma lvl
        n_lvl = Item(WIN, 'n_lvl')
        n_lvl.rect.x = 730
        n_lvl.rect.bottom = 95
        self.set_of_items.add(n_lvl)


# klasa platformy
class Platform(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, rect_x, rect_y):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        screen.blit(colour, (0, 0))
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface, image_list):
        surface.blit(self.image, self.rect)
        if self.width == 3:
            surface.blit(WIN, self.rect)
        else:
            surface.blit(image_list[0], self.rect)
            for i in range(70, self.width - 70, 70):
                surface.blit(image_list[1], [self.rect.x + i,self.rect.y])
            surface.blit(image_list[2], [self.rect.x + self.width - 70,self.rect.y])







BACKGROUND_HELLO = pygame.image.load(os.path.join('png', 'hello.png')).convert()
LVL1 = pygame.image.load(os.path.join('png', 'almostBlack.png')).convert()
LVL1B = pygame.image.load(os.path.join('png', 'LVL1B.png')).convert()
END = pygame.image.load(os.path.join('png', 'earth.png')).convert()
NEXT = pygame.image.load(os.path.join('png', 'darkBlue.png')).convert()
button = Button("START", 300, 120, B_BLUE, LIGHTBLUE)

# konkretyzacja obiektów

player = Player(stand_R)
current_level = Level_1(player)
player.level = current_level
player.rect.center = [880, 590]
finish_text = Text('KONIEC GRY', PINK)
next_text = Text('LEVEL 2', PINK)

# zmienne
window_open = True
active_game = False



# głowna pętla gry
while window_open:
    screen.blit(LVL1, (0, 0))
    # pętla zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
                break
        elif event.type == pygame.QUIT:
            window_open = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                active_game = True
                pygame.mouse.set_visible(True)
                pygame.time.delay(500)
        if active_game:
            player.get_event(event)

    if active_game:
        if not player.lifes:
            window_open = False
        if player.advance > 0:
            screen.blit(NEXT, (0, 0))
            next_text.rect.center = WIDTH // 2, HEIGHT // 2
            next_text.draw(screen)
            pygame.display.flip()
            pygame.time.delay(4000)
            window_open = False
        # rysowanie i aktualizacja obiektów
        current_level.draw(screen)
        player.update()
        player.draw(screen)
        current_level.update()
    else:
        screen.blit(BACKGROUND_HELLO, (0, 0))
        button.draw(screen)
        pygame.display.flip()

    # aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(30)

pygame.time.delay(500)
screen.blit(END, (0, 0))
finish_text.rect.center = WIDTH // 2, HEIGHT // 2+100
finish_text.draw(screen)
pygame.display.flip()
pygame.time.delay(3000)
pygame.quit()

