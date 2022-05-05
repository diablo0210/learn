# Blackjack or 21 Game Programme

import random
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.


def card_draw():
    i = random.randint(0, 12)
    # print(deck[i])
    return deck[i]

def winner():
    # print(f"Your cards are {player} and your total is {player_sum}.")
    print(f"Computer's cards are {computer} and its total is {computer_sum}.\n")
    if player_sum > 21:
        print("Fuck! You Lost.\n")
    elif computer_sum > 21:
        print("Yay! You win.\n")
    elif player_sum == computer_sum:
        print("Its a Draw!!!\n")
    elif player_sum == 21:
        print("Yo! Yo! Blackjack! You win.\n")
    elif computer_sum == 21:
        print("Shit Blackjack! You Lost.\n")
    elif player_sum > computer_sum:
        print("Yo! Yo! Yo! You win!!!\n")
    else:
        print("Fuck! You Lost.\n")


want_to_play = input("Do you want to play a game of Blackjack?\nType 'y' for yes or 'n' for no.: \n").lower()
if want_to_play == "n":
    print("Fuck OFF!!!")
while want_to_play == "y":
    computer = []
    player = []
    computer_sum = 0
    player_sum = 0
    computer.append(card_draw())
    player.append(card_draw())
    computer.append(card_draw())
    player.append(card_draw())
    # print(computer)
    # print(player)
    computer_sum = sum(computer)
    player_sum = sum(player)
    # print(computer_sum)
    # print(player_sum)
    print(f"Your cards are {player} and your total is {player_sum}.")
    print(f"Computer's first card is {computer[0]}")
    next_card = input("Type 'y' to get another card or 'n' to pass.\n").lower()
    if next_card == "y":
        player.append(card_draw())
        player_sum = sum(player)
        print(f"Your cards are {player} and your total is {player_sum}.")
        if player_sum < 17:
            next_card = input("Type 'y' to get another card or 'n' to pass.\n").lower()
            if next_card == "y":
                player.append(card_draw())
                player_sum = sum(player)
                print(f"Your cards are {player} and your total is {player_sum}.")
        elif computer_sum < 17:
            computer.append(card_draw())
            computer_sum = sum(computer)
            # print(computer)
            print(f"Computer's total is {computer_sum}")
            if computer_sum < 17:
                computer.append(card_draw())
                computer_sum = sum(computer)
    elif next_card == "n":
        if computer_sum < 17:
            computer.append(card_draw())
            computer_sum = sum(computer)
            # print(computer)
            print(f"Computer's total is {computer_sum}")
            if computer_sum < 17:
                computer.append(card_draw())
                computer_sum = sum(computer)
                # print(computer)
                print(f"Computer's total is {computer_sum}")

    winner()
    want_to_play = input("Do you want to play another game of Blackjack?\nType 'y' for yes or 'n' for no.: ").lower()
    if want_to_play == "n":
        print("Fuck OFF!!!")









