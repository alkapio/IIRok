from graph import *


pygame.init()


## ustawienia ekranu i gry
SIZESCREEN = WIDTH, HEIGHT = 1024, 700
screen = pygame.display.set_mode(SIZESCREEN)

blocksGroup = pygame.sprite.Group()


class Button:
    def __init__(self, text, width, height, background_colour, text_colour):
        self.text = text
        self.width = width
        self.height = height
        self.background_colour = background_colour
        self.text_colour = text_colour
        self.font = pygame.font.SysFont(None, 72)
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = [WIDTH//2, HEIGHT//2]
        self.set()

    def set(self):
        self.image = self.font.render(
            self.text,1, self.text_colour, self.background_colour)
        self.rect_image = self.image.get_rect()
        self.rect_image.center = self.rect.center

    def draw(self, surface):
        surface.fill(self.background_colour, self.rect)
        surface.blit(self.image, self.rect_image)

# klasa tekst
class Text:
    def __init__(self, text, text_colour, size = 74):
        self.text = text
        self.text_colour = text_colour
        self.font = pygame.font.SysFont(None, size)
        self.image = self.font.render(str(self.text), 1, self.text_colour)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def Screen_text(info_text):
    largeText = pygame.font.Font('freesansbold.ttf', 18)
    TextSurf, TextRect = Text_objects(info_text, largeText)
    TextRect.center = ((WIDTH / 2), (HEIGHT / 2))
    screen.blit(TextSurf, TextRect)

def Text_objects(info_text, font):
    textSurface = font.render(info_text, True, LIGHTBLUE)
    return textSurface, textSurface.get_rect()

# ogólna klasa wroga
class Enemy(pygame.sprite.Sprite):
    def __init__(self, colour, file_image, rect_x, rect_y, movement_x, movement_y):
        super().__init__()
        self.screen = screen
        self.image = file_image
        self.rect = self.image.get_rect()
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.rect.x = rect_x
        self.rect.y = rect_y
        screen.blit(colour, (0, 0))


    def update(self):
        #ruch w poziomie
        if self.rect.x < 900:
            self.rect.x += self.movement_x
        else:
            self.rect.x = 0

        # ruch góra/dół
        if self.rect.y < 700:
            self.rect.y += self.movement_y
        else:
            self.rect.y = 20



    def draw(self, surface):
        surface.blit(self.image, self.rect)




# klasa przedmiotu
class Item(pygame.sprite.Sprite):
    def __init__(self, image, name):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.name = name