import random

class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = [str(n) for n in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in Card.suits for v in Card.values]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def take_card(self, card):
        self.hand.append(card)

    def play_card(self):
        return self.hand.pop(0)

    def has_cards(self):
        return len(self.hand) > 0

def main():
    deck = Deck()

    player1 = Player("Alice")
    player2 = Player("Bob")

    # Deal cards
    while len(deck.cards) > 0:
        player1.take_card(deck.draw_card())
        player2.take_card(deck.draw_card())

    round_number = 1
    while player1.has_cards() and player2.has_cards():
        print(f"Round {round_number}:")
        card1 = player1.play_card()
        card2 = player2.play_card()
        print(f"{player1.name} plays {card1} and {player2.name} plays {card2}")

        if Card.values.index(card1.value) > Card.values.index(card2.value):
            player1.take_card(card1)
            player1.take_card(card2)
            print(f"{player1.name} wins the round!")
        elif Card.values.index(card1.value) < Card.values.index(card2.value):
            player2.take_card(card1)
            player2.take_card(card2)
            print(f"{player2.name} wins the round!")
        else:
            print("It's a tie!")

        round_number += 1

    winner = player1.name if player1.has_cards() else player2.name
    print(f"{winner} wins the game!")

if __name__ == "__main__":
    main()
