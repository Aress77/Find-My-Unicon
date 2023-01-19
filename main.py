
import pygame
from pygame.locals import *
import gradient_pygame as gp
import random
import os.path

# Initializing pygame
pygame.init()

# Setting up the screen in 1920 pixels wide, and 1080 pixels high
screen = pygame.display.set_mode((1280, 720), pygame.SRCALPHA)
pygame.display.set_caption("Find My Unicorn")
screen = pygame.display.get_surface()

# create a global random variable
x = random.randint(1, 5)

def gradient_background():

    color_1 = (random.randint(0,254), random.randint(58,226), random.randint(60,229))
    color_2 = (random.randint(40,254), random.randint(58,230), random.randint(60,250))

    forward = bool(random.getrandbits(1))

    # See gradient_pygame.py; A block of code shared on the pygame wiki for quick simple gradient generation
    gp.fill_gradient(screen, color_1, color_2, None, False, forward)
    return

gradient_background()


def draw_gradient():
    for n in range(0, 3000):
        x = random.randint(1, 1280)
        y = random.randint(1, 720)
        w = random.randint(1, 320)
        h = random.randint(1, 180)
        rect_1 = Rect(x, y, w, h)
        color_1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        color_2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        vertical = bool(random.getrandbits(1))
        forward = bool(random.getrandbits(1))

        # See gradient_pygame.py; A block of code shared on the pygame wiki for quick simple gradient generation
        gp.gradient_background(screen, color_1, color_2, rect_1, vertical, forward)
        return

# Loading and organizing images into different lists
cloud_1 = pygame.image.load(os.path.join('data', 'cloud1.png'))
mont_2 = pygame.image.load(os.path.join('data', 'mountain2.png'))
mont_1 = pygame.image.load(os.path.join('data', 'mountain1.png'))
mont_3 = pygame.image.load(os.path.join('data', 'mountain3.png'))
mont_5 = pygame.image.load(os.path.join('data', 'mountain5.png'))
mont_4 = pygame.image.load(os.path.join('data', 'mountain4.png'))
mont_6 = pygame.image.load(os.path.join('data', 'mountain6.png'))
cloud_2 = pygame.image.load(os.path.join('data', 'cloud2.png'))
cloud_3 = pygame.image.load(os.path.join('data', 'cloud3.png'))
cloud_4 = pygame.image.load(os.path.join('data', 'cloud4.png'))
word_yes = pygame.image.load(os.path.join('data', 'word_yes1.png'))
word_no1 = pygame.image.load(os.path.join('data', 'word_no1.png'))
word_wrong = pygame.image.load(os.path.join('data', 'word_wrong.png'))
moon = pygame.image.load(os.path.join('data', 'moon1.png'))
unicorn = pygame.image.load(os.path.join('data', 'unicorn.png'))

cloud_images = [cloud_1,cloud_2,cloud_3,cloud_4]
mount_images = [mont_1, mont_2, mont_3, mont_4, mont_5, mont_6]


def draw_image():
    for n in range(0, 5):
        x2 = random.randint(0, 500)
        y2 = random.randint(0, 100)
        screen.blit(random.choice(cloud_images), (x2, y2))

    if x < 5:
        pygame.draw.circle(screen, (random.randint(40,254), random.randint(58,230), random.randint(60,250)), (1000, 300), 100)
        screen.blit(random.choice(mount_images), (0, 30))
        if x == 4:
            screen.blit(word_wrong, (150, 460))
        else:
            screen.blit(word_no1, (150, 460))
    elif x == 5:
        screen.blit(random.choice(mount_images), (0, 30))
        screen.blit(moon, (300,0))
        screen.blit(word_yes,(50,460))
        screen.blit(unicorn, (440,200))
    return


# call the function to draw the loaded images
draw_image()

# Define a function for exiting program
def exit_program():
    pygame.display.quit()
    pygame.quit()
    exit()


# Update the display
pygame.display.update()

n = 1

# infinite run
while True:
    fileName = "drawn{}.png"
    fileName = fileName.format(n)

    if not os.path.exists(fileName):
        fileName = "drawn{}.png"
        fileName = fileName.format(n)
        pygame.image.save(screen, fileName)
        print("export image:", fileName)
        pygame.display.set_caption(fileName)
        running = True
        # Keep Displaying the window until close it manually
        while running:
            if x == 4:
                x1 = 0
                y1 = 0
                keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_UP]:
                    y1 = y1 - 1
                elif keyPressed[pygame.K_DOWN]:
                    y1 = y1 + 1
                elif keyPressed[pygame.K_LEFT]:
                    x1 = x1 - 1
                elif keyPressed[pygame.K_RIGHT]:
                    x1 = x1 + 1
                if x == 4:
                    pygame.draw.circle(screen, (random.randint(40, 254), random.randint(58, 230), random.randint(60, 250)),
                                       (1000, 300), 100)
                pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        exit_program()
    n += 1
