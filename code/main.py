import pygame
import sys
from settings import *
from level import Level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

# Variável para controlar se o jogo está no menu
in_menu = True

# Carregar a imagem de fundo
background_image = pygame.image.load("Menu_logo.png")
background_rect = background_image.get_rect(center=(screen_width // 2, screen_height // 2))

# Mensagem do menu
font = pygame.font.Font(None, 36)
menu_message = font.render("Pressione qualquer tecla para iniciar", True, (255, 255, 255))
menu_rect = menu_message.get_rect(center=(screen_width // 2, screen_height * 0.8))  # Posiciona abaixo da imagem

while in_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            in_menu = False

    screen.blit(background_image, background_rect)  # Desenha a imagem de fundo
    screen.blit(menu_message, menu_rect)  # Desenha a mensagem do menu

    pygame.display.update()
    clock.tick(60)

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)
