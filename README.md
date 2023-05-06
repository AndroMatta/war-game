Define the Card class:

The Card class represents a single card in a standard 52-card deck.
We define class variables "suits" and "values" as lists to hold the possible suit and face value options for each card.
The __init__ method initializes a card instance with a given suit and value.
The __repr__ method is used to provide a human-readable representation of the card when printed.
Define the Deck class:

The Deck class represents a deck of cards.
In the __init__ method, we create a list called "cards" that holds all possible combinations of suits and values, effectively creating a standard 52-card deck. We then shuffle the deck using random.shuffle.
The draw_card method is used to draw a card from the top of the deck (the end of the list) and removes it from the deck using the pop method.
Define the Player class:

The Player class represents a player in the game.
In the __init__ method, we initialize a player instance with a given name and an empty hand (a list called "hand").
The take_card method appends a card to the player's hand.
The play_card method removes and returns the first card in the player's hand.
The has_cards method checks if the player still has cards in their hand.
Implement the main game loop in the main function:

First, we create a deck of cards and two players.
Next, we deal the cards to the players by drawing cards from the deck and giving them to each player until the deck is empty.
We then enter a loop that continues as long as both players have cards in their hands.
In each iteration (round) of the loop, both players play a card from their hands.
We compare the cards' values using their indices in Card.values. The player with the higher card value wins the round and takes both cards.
If the cards have the same value, it's a tie, and no one takes the cards.
We increment the round counter.
Once a player runs out of cards, the other player wins the game. We print the winner's name.
