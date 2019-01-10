import random
import time


def display_intro():
    print('''You are in a land full of dragons. In front of you,
     you see two caves. In one cave, the dragon is friendly and
     will share his treasure with you. The other dragon is greedy
      and hungry, and will eat you on sight.''')
    print()


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Into which cave will you go (1 or 2)? ')
        cave = input()

    return cave


def pause_for_dramatic_effect(seconds):
    while seconds > 0:
        print('.', end='')
        time.sleep(1)
        seconds -= 1
    print()


def check_cave(chosen_cave):
    print('You approach the cave.', end='')
    pause_for_dramatic_effect(3)
    print('It is dark and spooky.', end='')
    pause_for_dramatic_effect(6)
    print('A large dragon jumps out in front of you! He opens his jaws and.', end='')
    pause_for_dramatic_effect(9)

    friendly_cave = random.randint(1, 2)

    if chosen_cave == str(friendly_cave): print('Gives you his treasure! You are rich!')
    else: print('Gobbles you down in one bite! Ouch!')


play_again = 'yes'


while play_again == 'yes' or play_again == 'y':
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)

    print('\nDo you want to play again (yes or no)?')
    play_again = input()
