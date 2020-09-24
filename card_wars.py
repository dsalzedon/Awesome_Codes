from itertools import product
from random import shuffle, choice


class Cards:
    suits = ["♠", "♣", "♥", "♦"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    deck = [str(j) + " " + i for i,j in product(suits, values)]
    shuffle(deck)


class War:

    def __init__(self):
        self.p1 = "Daniel"
        # self.p1 = input("Type yourname")
        self.p2 = "Ivan"
        # self.p2 = input("Type yourname")

        self.p1_wins = 0
        self.p2_wins = 0
        self.draws = 0

        print("Welcome player1:\n{} \nWelcome player2:\n{}".format(self.p1, self.p2))


    def game(self):
        while True:
            player_1_card = choice(Cards.deck)
            Cards.deck.remove(player_1_card)
            player_2_card = choice(Cards.deck)
            Cards.deck.remove(player_2_card)

            p1_card = player_1_card.split()
            p2_card = player_2_card.split()

            print("\n{} draws: \n{} \n{} draws: \n{}\n".format(self.p1, player_1_card, self.p2, player_2_card))

            if self.p1_wins == 10:
                print("Finish, {} wins".format(self.p1))
                print(len(Cards.deck))
                break
            elif self.p2_wins == 10:
                print("Finish, {} wins".format(self.p2))
                print(len(Cards.deck))
                break
            elif self.draws ==10:
                print("No one wins")
                print(len(Cards.deck))
            else:
                p1_value = self.check_char(p1_card[0])
                p2_value = self.check_char(p2_card[0])
                print(self.card_battle(p1_value, p2_value))


    def check_char(self,string):

        self.string = string

        if string == "J":
            return 11
        elif string == "Q":
            return 12
        elif string == "K":
            return 13
        else:
            return int(string)


    def card_battle(self,card1, card2):

        self.card1 = card1
        self.card2 = card2

        if card1 > card2:
            self.p1_wins += 1
            return "Player 1 wins"
        elif card1 == card2:
            self.draws += 1
            return "Draw"
        else:
            self.p2_wins += 1
            return "Player 2 wins"

        
game = War()
game.game()
