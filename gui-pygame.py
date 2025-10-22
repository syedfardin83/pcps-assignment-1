import pygame
pygame.init()

window_size = (1000,500)

gameWindow = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame")

gameWindow.fill((255,255,255))
pygame.display.update()

exit_game = False

attack_button_image = pygame.image.load('./images/attack_button.png')
attack_button_image = pygame.transform.scale(attack_button_image,(100,100))
attack_button_rect = attack_button_image.get_rect(topleft=(window_size[0]-150,window_size[1]-150))

heal_button_image = pygame.image.load('./images/heal_button.png')
heal_button_image = pygame.transform.scale(heal_button_image,(100,100))
heal_button_rect = attack_button_image.get_rect(topleft=(window_size[0]-270,window_size[1]-150))

background_image = pygame.image.load('./images/forest_retro.png')
background_image = pygame.transform.scale(background_image,window_size)

self_image = pygame.image.load('./images/robin_hood.webp')
self_image = pygame.transform.scale(self_image,(100,200))
self_image_rect = self_image.get_rect(topleft=(window_size[0]-150,window_size[1]-400))

hunter_image = pygame.image.load('./images/hunter.png')
hunter_image = pygame.transform.scale(hunter_image,(200,200))
hunter_image_rect = self_image.get_rect(topleft=(100,window_size[1]-400))




while not exit_game:
    for event in pygame.event.get():
        # print(type(event.type))
        if event.type==pygame.QUIT:
            print('Quitting...')
            exit_game = True
        if event.type == pygame.KEYDOWN:
            print("A key was pressed!")

        if event.type == pygame.MOUSEBUTTONDOWN:
            if attack_button_rect.collidepoint(event.pos):
                print("Attack Button clicked!!")
            if heal_button_rect.collidepoint(event.pos):
                print("Heal button clicked!")

    gameWindow.blit(background_image,(0,0))
    gameWindow.blit(attack_button_image,attack_button_rect)
    gameWindow.blit(heal_button_image,heal_button_rect)
    gameWindow.blit(self_image,self_image_rect)
    gameWindow.blit(hunter_image,hunter_image_rect)

    pygame.display.flip()

pygame.quit()
exit()