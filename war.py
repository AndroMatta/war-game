import time
import os
import random

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Deck:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"] # class variable containing the suits
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"] # class variable containing the ranks

    # Constructor method to initialize a new instance 
    def __init__(self):
        self.cards = [(rank, suit) for rank in self.ranks for suit in self.suits] # Instance variable containing all cards in the deck
        random.shuffle(self.cards)

    def split(self):
        return self.cards[:26], self.cards[26:] # Return two halves of the deck as tuples

    # Generate a human readable description of the card
    @staticmethod
    def card_description(card):
        rank, suit = card
        return f"{rank} of {suit}"

def clear_screen():
    pass  # Implement the clear screen functionality depending on your platform


def get_game_mode():
    while True:
        mode = input("Choose 1P or 2P: ").lower().strip()
        if mode in ["1p", "2p"]:
            return mode
        else:
            print("Invalid input. Please choose either 1P or 2P.")


def get_player_names(mode):
    if mode == "1p":
        player_name = input("Enter your name: ")
        opponent_name = "Computer"
    else:
        player_name = input("Enter player1 name: ")
        opponent_name = input("Enter player2 name: ")

    return player_name, opponent_name


def play_round(player_name, opponent_name, player_deck, opponent_deck, mode):
    input(f"\n{player_name}, press Enter to play your card...")
    clear_screen()

    player_card = player_deck.pop(0)
    opponent_card = opponent_deck.pop(0)

    player_card_description = Deck.card_description(player_card)
    print(f"{player_name} plays {player_card_description}.")

    if mode == "1p":
        for _ in range(4):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print(".")
    else:
        input(f"{opponent_name}, press Enter to play your card...")

    opponent_card_description = Deck.card_description(opponent_card)
    print(f"{opponent_name} plays {opponent_card_description}.")
    for _ in range(4):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(".", end="")

    if Deck.ranks.index(player_card[0]) > Deck.ranks.index(opponent_card[0]):
        player_deck.extend([player_card, opponent_card])
        print(f"\n{player_name} wins this round.")
    else:
        opponent_deck.extend([opponent_card, player_card])
        print(f"\n{opponent_name} wins this round.")
    for _ in range(4):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(".")

    print(f"\n{player_name} has {len(player_deck)} cards remaining.")
    print(f"{opponent_name} has {len(opponent_deck)} cards remaining.")


def play_game():
    try:
        clear_screen()
        print("Welcome to the card game War!")
        time.sleep(2)  # Pause for two seconds

        mode = get_game_mode()
        player_name, opponent_name = get_player_names(mode)

        deck = Deck()
        player_deck, opponent_deck = deck.split()  # Split the deck into two halves

        while player_deck and opponent_deck:
            play_round(player_name, opponent_name, player_deck, opponent_deck, mode)

        winner = player_name if player_deck else opponent_name
        print(f"\nCongratulations {winner}, you have won the game!")

        while True:
            play_again = input("Would you like to play again? (yes/no): ").lower().strip()
            if play_again == "yes":
                play_game()
                break
            elif play_again == "no":
                print("Thanks for playing!")
                break
            else:
                print("Invalid input. Please enter yes or no.")
    except (EOFError, KeyboardInterrupt):
        print("\nThank you for playing!")


def main():
    play_game()


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
