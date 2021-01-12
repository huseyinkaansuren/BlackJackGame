############### Blackjack Project #####################
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards=[]
computer_cards=[]
player_score=0
computer_score=0
def card_append():
    for i in range(2):
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
def blackjack_checker(player_score,computer_score):
    if computer_cards.count(11) and computer_cards.count(10):
        print("Computer has a BlackJack.Computer Win")

    elif player_cards.count(11) and player_cards.count(10):
        print("You have a BlackJack.You Win")

def game_checker(player_score,computer_score):
    if player_score > 21:
        print("You went over. You Lose")
    elif player_score == 21:
        print("You Win")
    elif computer_score > 21:
        print("Computer went over.You Win")
    elif player_score > computer_score:
        print("You Win")
    else:
        print("You Lose")

should_continue=True
while should_continue:
    player_cards=[]
    computer_cards=[]
    player_score=0
    computer_score=0

    card_append()

    player_score=player_cards[0]+player_cards[1]
    computer_score=computer_cards[0]+computer_cards[1]

    print(f"Your Cards [{player_cards}], current score:{player_score}")
    print(f"Computer Cards [{computer_cards[0]},?]")

    blackjack_checker(player_score,computer_score)

    if player_cards.count(11) and player_score > 21:
        player_cards[player_cards.count(11)] = 1
        player_score = player_cards[0] + player_cards[1]
        print(f"Computer's Final Cards[{computer_cards}],final score:{computer_score}")
        print("You Win")

    selection=input("Type 'y' to get another card, type 'n' to pass:")
    if selection=="y":
        player_cards.append(random.choice(cards))
        player_score+=player_cards[-1]
        print(f"Your Final Cards [{player_cards}], current score:{player_score}")
        print(f"Computer's Final Cards[{computer_cards}],final score:{computer_score}")


    elif selection=="n":
        com_score=True
        while com_score:
            if computer_score<16:
                print("Computer is drawing now")
                computer_cards.append(random.choice(cards))
                computer_score+=computer_cards[-1]
                com_score=False
            else:
                com_score=False
        print(f"Your Final Cards [{player_cards}], current score:{player_score}")
        print(f"Computer's Final Cards[{computer_cards}],final score:{computer_score}")

    game_checker(player_score,computer_score)

    while_selection=input("Type 'y' for play again, 'n' for end:")
    if while_selection=="n":
        should_continue=False
        print("Thanks for playing!")

