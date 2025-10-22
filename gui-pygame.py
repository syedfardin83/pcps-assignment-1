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
attack_button_rect = attack_button_image.get_rect(topleft=(150,150))

background_image = pygame.image.load('./images/forest_retro.png')
background_image = pygame.transform.scale(background_image,window_size)

self_image = pygame.image.load('./images/robin_hood.webp')




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
                print("Button clicked!!")

    gameWindow.blit(background_image,(0,0))
    gameWindow.blit(attack_button_image,attack_button_rect)

    pygame.display.flip()

pygame.quit()
exit()