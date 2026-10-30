# pygame template

import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 640
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

cloud_x1 = 200
cloud_y1 = 150
cloud1_colour = (255, 255, 255)

cloud_x2 = 300
cloud_y2 = 100
cloud2_colour = (211, 211, 211)

cloud_x3 = 400
cloud_y3 = 80
cloud3_colour = (192, 192, 192)

road_colour = (50, 50, 50)

grass_colour = (0, 75, 0)

roof_points = [
        (251, 300),
        (500, 300),
        (374, 200),
    ]

circle_x = 200
circle_y = 150

person1_x = 80
person1_y = 500

person2_x = -200
person2_y = 500

person3_x = -200
person3_y = 450
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    cloud_x1 += 3
    if cloud_x1 > WIDTH:
        cloud_x1 = 0

    cloud_x2 += 5
    if cloud_x2 > WIDTH:
        cloud_x2 = 0

    cloud_x3 += 7
    if cloud_x3 > WIDTH:
        cloud_x3 = 0



    # DRAWING

    screen.fill((4, 26, 64))  # always the first drawing command

    # moon
    pygame.draw.circle(screen, (134, 119, 95), (680, 80), 80)
    pygame.draw.circle(screen, (44, 45, 45), (646, 50), 10)
    pygame.draw.circle(screen, (44, 45, 45), (628, 97), 17)
    pygame.draw.circle(screen, (44, 45, 45), (694, 35), 13)
    pygame.draw.circle(screen, (44, 45, 45), (715, 110), 20)
    pygame.draw.circle(screen, (44, 45, 45), (678, 76), 20)

    # Cloud 1
    pygame.draw.circle(screen, cloud1_colour, (cloud_x1, cloud_y1-4), 40)
    pygame.draw.circle(screen, cloud1_colour, (cloud_x1+35, cloud_y1+13), 24)
    pygame.draw.circle(screen, cloud1_colour, (cloud_x1-40, cloud_y1-8), 23)
    pygame.draw.circle(screen, cloud1_colour, (cloud_x1-61, cloud_y1+14), 23)
    pygame.draw.rect(screen, cloud1_colour, (cloud_x1-59, cloud_y1-1, 100, 38))

    # Cloud 2
    pygame.draw.circle(screen, cloud2_colour, (cloud_x2, cloud_y2-4), 40)
    pygame.draw.circle(screen, cloud2_colour, (cloud_x2+35, cloud_y2+13), 24)
    pygame.draw.circle(screen, cloud2_colour, (cloud_x2-40, cloud_y2-8), 23)
    pygame.draw.circle(screen, cloud2_colour, (cloud_x2-61, cloud_y2+14), 23)
    pygame.draw.rect(screen, cloud2_colour, (cloud_x2-59, cloud_y2-1, 100, 38))

    # Cloud 3
    pygame.draw.circle(screen, cloud3_colour, (cloud_x3, cloud_y3-4), 43)
    pygame.draw.circle(screen, cloud3_colour, (cloud_x3+35, cloud_y3+13), 27)
    pygame.draw.circle(screen, cloud3_colour, (cloud_x3-40, cloud_y3-8), 26)
    pygame.draw.circle(screen, cloud3_colour, (cloud_x3-61, cloud_y3+14), 26)
    pygame.draw.rect(screen, cloud3_colour, (cloud_x3-59, cloud_y3-1, 100, 41))

    # tree
    pygame.draw.rect(screen, (101, 67, 33), (590, 310, 50, 150))
    pygame.draw.circle(screen, (0, 128, 0), (615, 270), 50)
    pygame.draw.circle(screen, (0, 128, 0), (593, 292), 45)
    pygame.draw.circle(screen, (0, 128, 0), (576, 250), 30)
    pygame.draw.circle(screen, (0, 128, 0), (625, 220), 40)
    pygame.draw.circle(screen, (0, 128, 0), (650, 283), 42)

    # grass hill
    pygame.draw.circle(screen, grass_colour, (400, 1425), 1000)

    # road
    pygame.draw.rect(screen, road_colour, (0, 540, 800, 350))
    pygame.draw.line(screen, road_colour, (400, 430), (136, 580), 80)

    x = 0
    while x < WIDTH:
        y = HEIGHT - 60
        pygame.draw.rect(screen, (255, 255, 0), (x, y, 35, 10))
        x += 70
    # house
    pygame.draw.rect(screen, (245, 214, 108), (298, 300, 150, 130))
    # roof
    pygame.draw.polygon(screen, (255, 0, 0), roof_points)
    # door
    pygame.draw.rect(screen, (150, 75, 0), (350, 350, 50, 80))

    # pumpkin
    pygame.draw.circle(screen, (255, 165, 0), (circle_x + 280, circle_y + 260), 30)
    pygame.draw.circle(screen, (0, 0, 0), (circle_x + 268, circle_y +248), 3)
    pygame.draw.circle(screen, (0, 0, 0), (circle_x + 292, circle_y +248), 3)
    pygame.draw.polygon(screen, (0, 0, 0), ((463, 412), (468, 425), (491, 424), (496, 410), (490, 421), (486, 410), (480, 420), (476, 408), (471, 420), (464, 412)))
    pygame.draw.rect(screen, (144, 238, 144), (473, 365, 15, 23))

    # person 1
    pygame.draw.polygon(screen, (0, 191, 255), ((person1_x, person1_y), (person1_x + 40, person1_y + 70), (person1_x - 40, person1_y + 70)))
    pygame.draw.circle(screen, (255, 203, 164), (person1_x, person1_y - 20), 30)
    pygame.draw.rect(screen, (168, 112, 78), (person1_x-30, person1_y + 70, 20, 50))
    pygame.draw.rect(screen, (168, 112, 78), (person1_x+10, person1_y + 70, 20, 50))
    pygame.draw.circle(screen, (0, 0, 0), (person1_x + 15, person1_y - 30), 5)
    pygame.draw.circle(screen, (0, 0, 0), (person1_x - 15, person1_y - 30), 5)
    pygame.draw.circle(screen, (0, 0, 0), (person1_x, person1_y - 8), 10)


    person1_x += 5

    if person1_x >= 200:
        person1_y -= 5

    if person1_y <= 350:
        person1_x -= 5

    if person1_y <= 350:
        person1_y += 5


    # person 2
    pygame.draw.polygon(screen, (220, 20, 60), ((person2_x, person2_y), (person2_x + 40, person2_y + 70), (person2_x - 40, person2_y + 70)))
    pygame.draw.circle(screen, (255, 203, 164), (person2_x, person2_y - 20), 30)
    pygame.draw.rect(screen, (168, 112, 78), (person2_x-30, person2_y + 70, 20, 50))
    pygame.draw.rect(screen, (168, 112, 78), (person2_x+10, person2_y + 70, 20, 50))
    pygame.draw.circle(screen, (0, 0, 0), (person2_x + 15, person2_y - 30), 5)
    pygame.draw.circle(screen, (0, 0, 0), (person2_x - 15, person2_y - 30), 5)
    pygame.draw.circle(screen, (0, 0, 0), (person2_x, person2_y - 8), 10)

    person2_x += 5

    if person2_x >= WIDTH:
        person2_x = -100

    # person 3
    pygame.draw.polygon(screen, (255, 255, 0), ((person3_x, person3_y), (person3_x + 40, person3_y + 70), (person3_x - 40, person3_y + 70)))
    pygame.draw.circle(screen, (255, 203, 164), (person3_x, person3_y - 20), 30)
    pygame.draw.rect(screen, (168, 112, 78), (person3_x-30, person3_y + 70, 20, 50))
    pygame.draw.rect(screen, (168, 112, 78), (person3_x+10, person3_y + 70, 20, 50))
    pygame.draw.circle(screen, (0, 0, 0), (person3_x + 15, person3_y - 30), 5)
    pygame.draw.circle(screen, (0, 0, 0), (person3_x - 15, person3_y - 30), 5)
    pygame.draw.circle(screen, (0, 0, 0), (person3_x, person3_y - 8), 10)

    person3_x += 13

    if person3_x >= WIDTH:
        person3_x = -200




    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
