import pygame
from pygame.color import THECOLORS
import sys

pygame.init() # Обязательная инициализация библиотеки!

# Реализуйте в этом методе создание окна размером 1280х720
def create_screen():
    screen_size = length, width = (1280, 720)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Все будет хорощо :)')
    return screen

def textures():
    date = pygame.image.load('pictures/inter/play.png')
    date = pygame.transform.scale(date,(130,130))
    date_rect = date.get_rect()
    date_rect.center = (640,360)
    return date_rect, date
    

def new_game():
    print('ghbdndnn')

# Опишите базовый цикл, который считывает и выводит на экран нажатие клавиш
# Если нажата клавиша ESC, то окно закрывается
def game_loop(screen):
    my_button = textures()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                print(f'Нажата клавиша: {pygame.key.name(event.key)}')
                if event.key == pygame.K_ESCAPE:
                    running = False  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if my_button[0].collidepoint(event.pos):
                    new_game()
        screen.fill(THECOLORS['blue'])
        screen.blit(my_button[1],my_button[0])
        pygame.display.flip()
    pygame.quit()
    sys.exit()
    
    
    
  
# main функция, из которой будет запускаться игра
if __name__ == '__main__':
  screen = create_screen()
  game_loop(screen)
  