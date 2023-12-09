import pygame
from support import import_folder

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()

        # Índice do frame atual na animação
        self.frame_index = 0

        # Velocidade de animação
        self.animation_speed = 0.5

        # Importa os frames da animação com base no tipo (jump ou land)
        if type == 'jump':
            self.frames = import_folder('../graphics/character/dust_particles/jump')
        elif type == 'land':
            self.frames = import_folder('../graphics/character/dust_particles/land')

        # Configura a imagem inicial do sprite
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        # Atualiza o índice do frame com base na velocidade de animação
        self.frame_index += self.animation_speed

        # Verifica se a animação chegou ao final
        if self.frame_index >= len(self.frames):
            self.kill()  # Remove o sprite do grupo quando a animação é concluída
        else:
            self.image = self.frames[int(self.frame_index)]  # Atualiza a imagem do sprite

    def update(self, x_shift):
        # Atualiza a animação e move o sprite ao longo do eixo x
        self.animate()
        self.rect.x += x_shift

