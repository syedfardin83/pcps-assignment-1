import pygame
import random
pygame.init()

opponent_max_health = 100
opponent_initial_health = 100
opponent_health = opponent_initial_health
opponent_attack_factor = 60
opponent_heal_factor = 10

self_max_health = 100
self_initial_health = 100
self_health = self_initial_health
self_attack_factor = 60
self_heal_factor = 10

window_size = (1000,500)

gameWindow = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame")

gameWindow.fill((255,255,255))
pygame.display.update()

exit_game = False
you_win = False
you_lose = False

attack_button_image = pygame.image.load('./images/attack_button.png')
attack_button_image = pygame.transform.scale(attack_button_image,(100,100))
attack_button_rect = attack_button_image.get_rect(topleft=(window_size[0]-150,window_size[1]-150))

heal_button_image = pygame.image.load('./images/heal_button.png')
heal_button_image = pygame.transform.scale(heal_button_image,(100,100))
heal_button_rect = attack_button_image.get_rect(topleft=(window_size[0]-270,window_size[1]-150))

restart_button_image = pygame.image.load('./images/restart.png')
restart_button_image = pygame.transform.scale(restart_button_image,(160,80))
restart_button_rect = restart_button_image.get_rect(topleft=(410,window_size[1]-150))

background_image = pygame.image.load('./images/forest_retro.png')
background_image = pygame.transform.scale(background_image,window_size)

self_image = pygame.image.load('./images/robin_hood.webp')
self_image = pygame.transform.scale(self_image,(100,200))
self_image_rect = self_image.get_rect(topleft=(window_size[0]-150,window_size[1]-400))

hunter_image = pygame.image.load('./images/hunter.png')
hunter_image = pygame.transform.scale(hunter_image,(200,200))
hunter_image_rect = self_image.get_rect(topleft=(100,window_size[1]-400))

you_win_image = pygame.image.load('./images/you_win.png')
you_win_image = pygame.transform.scale(you_win_image,(400,120))
you_win_image_rect = you_win_image.get_rect(topleft=(320,200))

you_lose_image = pygame.image.load('./images/you_lose.png')
you_lose_image = pygame.transform.scale(you_lose_image,(400,120))
you_lose_image_rect = you_lose_image.get_rect(topleft=(320,200))

font = pygame.font.SysFont(None, 48)

while not exit_game:
    self_score_text = font.render(f"SELF HEALTH: {self_health}", True, (255,255,255)) 
    self_score_text_rect = self_score_text.get_rect(center=(100, 50),topleft=(window_size[0]-330,60)) 

    opponent_score_text = font.render(f"OPPONENT HEALTH: {opponent_health}", True, (255,255,255)) 
    opponent_score_text_rect = self_score_text.get_rect(center=(100, 50),topleft=(30,60)) 
    for event in pygame.event.get():
        # print(type(event.type))
        if event.type==pygame.QUIT:
            print('Quitting...')
            exit_game = True
        if event.type == pygame.KEYDOWN:
            print("A key was pressed!")

        if event.type == pygame.MOUSEBUTTONDOWN and not you_lose and not you_win:
            if attack_button_rect.collidepoint(event.pos):
                print("Attack Button clicked!!")
                print("\n***** ATTACKING... ****")
                self_attack = int(random.random()*self_attack_factor)
                opponent_attack = int(random.random()*opponent_attack_factor)
                net_attack = self_attack-opponent_attack
                print(f'Attack amount: {self_attack}\nOpponent attack amount: {opponent_attack}\nEffective Attack: {net_attack}')
                if net_attack<0:
                    print(f"\n*** Opponent successfully defended your attack ***\n****  You dealt damage of {-1*net_attack} ****")
                    if not(self_health+net_attack<0):
                        self_health+=net_attack
                    else:
                        print("You LOST!")
                        you_lose = True
                        self_health = 0
                else:
                    print(f"\n****  Opponent dealt damage of {net_attack} ****")
                    if not (opponent_health-net_attack<0):
                        opponent_health -= net_attack
                    else:
                        print("You Win!")
                        opponent_health = 0
                        you_win = True
                        # exit_game = True
            if heal_button_rect.collidepoint(event.pos):
                print("Heal button clicked!")
                print("\n***** HEALING... ****")
                self_heal = int(random.random()*self_heal_factor)
                opponent_heal = int(random.random()*opponent_heal_factor)

                if not(self_heal+self_health>self_max_health):
                    self_health += self_heal

                if not(opponent_heal+opponent_health>opponent_max_health):
                    opponent_health += opponent_heal

                print(f"\nYou healed by {self_heal}\nOpponent healed by {opponent_heal}")

    gameWindow.blit(background_image,(0,0))
    gameWindow.blit(attack_button_image,attack_button_rect)
    gameWindow.blit(heal_button_image,heal_button_rect)
    gameWindow.blit(self_image,self_image_rect)
    gameWindow.blit(hunter_image,hunter_image_rect)
    gameWindow.blit(self_score_text,self_score_text_rect)
    gameWindow.blit(opponent_score_text,opponent_score_text_rect)
    if you_win:
        gameWindow.blit(you_win_image,you_win_image_rect)
    if you_lose:
        gameWindow.blit(you_lose_image,you_lose_image_rect)
    if you_win or you_lose:
        gameWindow.blit(restart_button_image,restart_button_rect)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if restart_button_rect.collidepoint(event.pos):
                you_lose = False
                you_win = False

                self_health = self_initial_health
                opponent_health = opponent_initial_health



    pygame.display.flip()

pygame.quit()
exit()