from itertools import product
from random import shuffle, choice


class War:

    def game():
        while True:

            player_1_card = choice(deck)
            deck.remove(player_1_card)
            player_2_card = choice(deck)
            deck.remove(player_2_card)

            p1_card = player_1_card.split()
            p2_card = player_2_card.split()

            print("\n{} draws: \n{} \n{} draws: \n{}\n".format(p1, player_1_card, p2, player_2_card))

            if p1_wins > 10:
                print("Finish, {} wins".format(p1))
                break
            elif p2_wins > 10:
                print("Finish, {} wins".format(p2))
                break
            elif draws >10:
                print("No one wins")
            else:
                p1_value = War.check_char(p1_card[0])
                p2_value = War.check_char(p2_card[0])
                print(War.card_battle(p1_value, p2_value))


    def check_char(string):
        if string == "J":
            return 11
        elif string == "Q":
            return 12
        elif string == "K":
            return 13
        else:
            return int(string)


    def card_battle(card1, card2):
        global p1_wins, p2_wins, draws

        if card1 > card2:
            p1_wins += 1
            return "Player 1 wins"
        elif card1 == card2:
            draws += 1
            return "Draw"
        else:
            p2_wins += 1
            return "Player 2 wins"


suits = ["♠", "♣", "♥", "♦"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
deck = [str(j) + " " + i for i,j in product(suits, values)]
shuffle(deck)

p1 = "Daniel"
# p1 = input("Type yourname")
p2 = "Ivan"
# p2 = input("Type yourname")

p1_wins = 0
p2_wins = 0
draws = 0

print("Welcome player1:\n{} \nWelcome player2:\n{}".format(p1, p2))

War.game()
