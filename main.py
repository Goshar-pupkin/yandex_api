import pygame
import sys
from io import BytesIO
from os import remove
import requests
from PIL import Image

pygame.init()

fps = 10
size = 1200, 620
screen = pygame.display.set_mode(size)
running = True
clock = pygame.time.Clock()

toponym_to_find = " ".join(sys.argv[1:])
if not toponym_to_find:
    toponym_to_find = input('Введите координаты и маштаб').split()
map_api_server = "http://static-maps.yandex.ru/1.x/"
params = {
        "ll": ",".join([toponym_to_find[0], toponym_to_find[1]]),
        "spn": ",".join([toponym_to_find[2], toponym_to_find[3]]),
        "l": "map"
    }
response = requests.get(map_api_server, params=params)

pilImage = Image.open(BytesIO(response.content))
pilImage.save('ol.png')
image = pygame.image.load('ol.png')
remove('ol.png')
image_rect = image.get_rect(center=screen.get_rect().center)
pygame.display.flip()
while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(pygame.Color('RED'))
    screen.blit(image, image_rect)
    pygame.display.flip()
pygame.quit()
