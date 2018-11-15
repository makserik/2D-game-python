import pygame

#Defineerime värvid
BLACK = (0, 0, 0)
class Player(pygame.sprite.Sprite):
    """ Mängija klass"""

    # Kiirus
    change_x = 0
    change_y = 0

    # Punktid
    points = 0

    def __init__(self, x, y):
        """ Constructor funktsioon """

        # Kõrgema konstruktori kutsumine
        super().__init__()

        # Laius,kõrgus
        self.img_file = "./sprites/player/p3_front.png"
        self.image = pygame.image.load(self.img_file)
        self.image = pygame.transform.scale(self.image, (30,30))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def collision(self):
        if self.col == 0:
            self.col = 1

    def changespeed(self, x, y):
        """ Muudab mängija kiirust, nupuvahetusega"""
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        """ Liigutab mängijat"""

        # Liigub paremale/vasakule
        self.rect.x += self.change_x

        # Kas me tabasime seina?
        wall_collision_list = pygame.sprite.spritecollide(self, walls, False)
        for block in wall_collision_list:
            # Ei muuda asukohta
            if self.change_x > 0:
                self.rect.right = block.rect.left
                self.collision()

            else:
                # Ei muuda asukohta
                self.rect.left = block.rect.right
                self.collision()

        # Liigub üles/alla
        self.rect.y += self.change_y

        # Kas me tabasime seina?
        wall_collision_list = pygame.sprite.spritecollide(self, walls, False)
        for block in wall_collision_list:

            # Ei muuda asukohta
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.collision()


            else:
                # Ei muuda asukohta
                self.rect.top = block.rect.bottom
                self.collision()

    col = 0

