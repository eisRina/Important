import pygame
from pygame.color import THECOLORS
import sys

pygame.init() # Обязательная инициализация библиотеки!

cards_for_game = [
    {'name': 'Golgari Grave-Troll', 'cost' : '5', 'type': 'Creature', 'strength' : '0' , 'health' : '0' },
    {'name': 'Force of Negation', 'cost' : '3', 'type': 'Instant', 'effect': 'If its not your turn, you may exile a blue card from your hand rather than pay this spells mana cost'},
    {'name': 'Ather Vial', 'cost' : '1', 'type': 'Artifact', 'strength' : '' , 'health' : ''},
    {'name': 'Shamans Trance', 'cost' : '3', 'type': 'Instant', 'strength' : '' , 'health' : ''},
    {'name': 'Cabal Ritual', 'cost' : '2', 'type': 'Instant', 'strength' : '' , 'health' : ''} #найти человеков 
]

# Реализуйте в этом методе создание окна размером 1280х720
def create_screen():
    screen_size = length, width = (1280, 720)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Все будет хорощо :)')
    return screen


def information_about_card(screen,card_info):
    font = pygame.font.SysFont(None,25)
    all_information = f"Название карты {card_info['name']}, Цена {card_info['cost']},Тип {card_info['type']}"
    if 'strenght' in card_info and 'health' in card_info:
        all_information += f"Сила {card_info['strength']}, Выносливость {card_info['health']}"
    elif 'effect' in card_info:
        all_information += f"Эффект {card_info['effect']}"
    render_text = font.render(all_information,True,THECOLORS['black'])
    screen.blit(render_text,(720,360))
    
    
def textures():
    enter = pygame.image.load('pictures/inter/play.png')
    enter = pygame.transform.scale(enter,(180,180))
    enter_ance = enter.get_rect()
    enter_ance.center = (550,360)
    enter_settings = enter_ance,enter
    
    exit = pygame.image.load('pictures/inter/exit.png')
    exit = pygame.transform.scale(exit,(180,180))
    exit_ance = exit.get_rect()
    exit_ance.center = (760,360)
    exit_settings = exit_ance,exit
    
    return enter_settings, exit_settings

def loading_background():
    background = pygame.image.load('pictures/playing_field/field.jpg')
    background = pygame.transform.scale(background,(1280,720))
    return background
    
    

def new_game():
    print('ghbdndnn')


# Опишите базовый цикл, который считывает и выводит на экран нажатие клавиш
# Если нажата клавиша ESC, то окно закрывается
def game_loop(screen):
    font = pygame.font.SysFont(None,40)
    our_card = None
    
    background = loading_background()
    start_button,exit_button = textures()
    
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
                if start_button[0].collidepoint(event.pos):
                    new_game()
                if exit_button[0].collidepoint(event.pos):
                    running = False
            
        screen.blit(background,(0,0))
        
        screen.blit(start_button[1],start_button[0])
        screen.blit(exit_button[1],exit_button[0])
        
        pygame.display.flip()
    pygame.quit()
    sys.exit()
    
    
    
  
# main функция, из которой будет запускаться игра
if __name__ == '__main__':
  screen = create_screen()
  game_loop(screen)
  
  
  
  