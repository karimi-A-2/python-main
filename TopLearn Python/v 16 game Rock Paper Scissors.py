import random

print('Rock'.lower())
print('Paper'.lower())
print('Scissors'.lower())
print('------------------')
random_number = random.randint(0, 2)

elements = ['rock', 'scissors', 'paper']
computer_move = elements[random_number]

player_1 = input('Player 1, make your move: ').lower()
player_2 = input('Player 2, make your move: ').lower()
# print(f'Player 1, make your move: {computer_move}')
# player_2 = computer_move

if player_1 == player_2:
    print("that's a tie")
else:
    index_1 = elements.index(player_1)
    next_item = elements[((index_1 + 1) % 3)]
    previous_item = elements[((index_1 - 1) % 3)]
    if player_2 == next_item:
        print('player 1 wins')
    elif player_2 == previous_item:
        print('player 2 wins')
    else:
        print("something went wrong")

print('end')