import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def adjust_ace(card_list, new_card):
    if new_card == 11 and sum(card_list) + 11 > 21:
        return 1
    return new_card

def print_result(user_cards, computer_cards):
    print(f"Your final hand {user_cards}, final score {sum(user_cards)}")
    print(f"Computer final hand: {computer_cards}, score {sum(computer_cards)}")


while True:
    choice = input("Do you want to play a game of BlackJack? Type 'y' or 'n':").lower().strip()
    while choice not in ['y', 'n']:
        print("Type 'y' or 'n'")
        choice = input("Do you want to play a game of BlackJack? Type 'y' or 'n':").lower().strip()
    if choice != 'y':
        print("See you next time. Bye!")
        break

    os.system('cls||clear')
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    if sum(user_cards) == 21 or sum(computer_cards) == 21:
        print_result(user_cards, computer_cards)
        if sum(user_cards) == 21 and sum(computer_cards) == 21:
            print("It's a draw")
        elif sum(user_cards) == 21:
            print("Blackjack! You win")
        else:
            print("Computer has Blackjack. You lose")
        continue

    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer first card: {computer_cards[0]}")

    while sum(user_cards) < 21:
        second_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
        while second_choice not in ['y', 'n']:
            print("Wrong answer. Try again!")
            second_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
        if second_choice != 'y':
            break
        new_card = adjust_ace(user_cards, deal_card())
        user_cards.append(new_card)
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer first card: {computer_cards[0]}")
        if sum(user_cards) == 21:
            break

    while sum(computer_cards) < 17:
        new_card = adjust_ace(computer_cards, deal_card())
        computer_cards.append(new_card)
        if sum(computer_cards) == 21:
            break

    print_result(user_cards, computer_cards)
    if sum(user_cards) > 21:
        print("You lose")
    elif sum(computer_cards) > 21 or sum(user_cards) > sum(computer_cards):
        print("You win")
    elif sum(computer_cards) == sum(user_cards):
        print("It's a draw")
    else:
        print("You lose")






