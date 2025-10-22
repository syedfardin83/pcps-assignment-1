import time
import random

opponent_health = 20
opponent_attack_factor = 60
opponent_heal_factor = 10

self_health = 100
self_attack_factor = 60
self_heal_factor = 10

while True:
    if opponent_health<=0:
        for i in range(1):
            print('\n*** GAME OVER: YOU WIN!!! ***')
        exit()
    elif self_health<=0:
        for i in range(1):
            print('\n*** GAME OVER: YOU LOST!!! ***')
        exit()

    print(f'\n    ************\nOpponent health: {opponent_health}\nYour health: {self_health}\n\nEnter choice: \n\t1. Attack \n\t2. Heal\n\t3. Quit')
    ch = input()

    if ch=='3':
        print('Quitting...')
        exit()

    elif ch=='1':
        print("\n***** ATTACKING... ****")
        self_attack = int(random.random()*self_attack_factor)
        opponent_attack = int(random.random()*opponent_attack_factor)
        net_attack = self_attack-opponent_attack
        print(f'Attack amount: {self_attack}\nOpponent attack amount: {opponent_attack}\nEffective Attack: {net_attack}')
        if net_attack<0:
            print(f"\n*** Opponent successfully defended your attack ***\n****  You dealt damage of {-1*net_attack} ****")
            self_health+=net_attack
        else:
            print(f"\n****  Opponent dealt damage of {net_attack} ****")
            opponent_health -= net_attack
        time.sleep(2)

    elif ch=='2':
        print("\n***** HEALING... ****")
        self_heal = int(random.random()*self_heal_factor)
        opponent_heal = int(random.random()*opponent_heal_factor)

        self_health += self_heal
        opponent_health += opponent_heal

        print(f"\nYou healed by {self_heal}\nOpponent healed by {opponent_heal}")

        time.sleep(2)





    else:
        print('********** INVALID INPUT!!  **********')
        time.sleep(2)
        continue