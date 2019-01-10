import random
import time

'''===================Functions==================='''


def display_intro():
    print('''\n***** You are in a land full of dragons! *****
    You set out in search for treasure, guarded by a dragon.
    As you set forth on your adventure, you come to a mountain side.
    In front of you, you see two caves. 
    * One cave will lead you towards a friendly dragon who will give you treasure.
    * The other dragon is greedy and hungry, and will eat you on sight.''')
    print()


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Into which cave will you go (1 or 2)? ')
        cave = input()

    return cave


def choose_path():
    path = ''
    while path != '1' and path != '2':
        print('\nDo you go path (1 or 2)? ')
        path = input()

    return path


def pause_for_dramatic_effect(seconds):
    while seconds > 0:
        print('.', end='')
        time.sleep(1)
        seconds -= 1
    print()


def check_cave(chosen_cave):
    print('You chose cave', chosen_cave, end='')
    random_val = random.randint(1,2)
    if chosen_cave == str(random_val):
        pause_for_dramatic_effect(3)
        print('You approach the cave.', end='')
        pause_for_dramatic_effect(3)
        print('It is dark and spooky.', end='')
        pause_for_dramatic_effect(3)
        print('You reach a fork in the tunnel.', end='')
    else:
        pause_for_dramatic_effect(3)
        print('You approach the cave.', end='')
        pause_for_dramatic_effect(3)
        print('It is warm and dimly lit.', end='')
        pause_for_dramatic_effect(3)
        print('You reach a fork in the tunnel.', end='')


def cave_end_good(cave_path_taken):
    print('You chose path', cave_path_taken, end='')
    pause_for_dramatic_effect(3)
    friendly_cave = random.randint(1, 2)
    if cave_path == str(friendly_cave):
        print('A large dragon jumps out in front of you! He opens his jaws and.', end='')
        pause_for_dramatic_effect(3)
        print('Gives you his treasure! You are rich!')
    else:
        print('You come to a dead end. You leave and return to the start.')


def cave_end_bad(cave_path_taken):
    print('You chose path', cave_path_taken, end='')
    pause_for_dramatic_effect(3)
    enemy_cave = random.randint(1, 2)
    if cave_path == str(enemy_cave):
        print('A large dragon jumps out in front of you! He opens his jaws and.', end='')
        pause_for_dramatic_effect(3)
        print('Gobbles you down in one bite! Ouch!')
    else:
        print('You come to a dead end. You leave and return to the start.')


'''=============================================================='''

proceed = 'yes'
play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    display_intro()

    '''Cave Choice'''
    cave_number = choose_cave()
    '''Cave Continue'''
    check_cave(cave_number)

    '''Path Choice'''
    if cave_number == 1:
        cave_path = choose_path()
        if cave_path == '1':
            cave_end_good(cave_path)
        else:
            cave_end_bad(cave_path)
    else:
        cave_path = choose_path()
        if cave_path == '1':
            cave_end_bad(cave_path)
        else:
            cave_end_good(cave_path)

    print('\nDo you want to play again (yes or no)?')
    play_again = input()

print('\nThanks for playing!')
