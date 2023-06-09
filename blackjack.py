import random
class Card:
    #instance creates each card
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name
    def __str__(self):
        return f"{self.suit} of {self.name}"

class Player():
    #sets the value added for each card and adds the score each time a card is added to the player/dealer's hand
    def adding_score(self, target):
        target.hand_value = 0
        for card in target.hand:
            if card.name in {'King', 'Queen', 'Jack'}:
                target.hand_value += 10
            elif card.name == 'Ace':
                target.hand_value += 1
            else:
                #adds the card value to the player/dealer's hand
                target.hand_value += card.name
    def show_score(self, target):
        #prints out the value of all cards in the hand
        print(f"\nValue in your hand: {target.hand_value}\n")
    def show_hand(self, target):
        #shows the cards in the player/dealer's hand
        for card in target.hand:
            print(f"\n{card.name} of {card.suit}")
    #method sends out a card to the player/dealer
    def deal_card(self, target):
        #shuffles the card in the hand
        random.shuffle(deck)
        #takes the last card from the shuffled deck
        card_to_add = deck.pop()
        #adds the card taken from the deck to the player/dealer's hand
        target.hand.append(card_to_add)

class Dealer(Player):
    #instance that creates the hand for the dealer and it starts the hand value
    def __init__(self, target):
        self.hand = []
        self.hand_value = 0
        super().__init__()
    #method creates the deck with all 52 cards and shuffles them
    def generate_deck(self):
        global deck
        deck = []
        suits = ['\u2666','\u2665', '\u2663', '\u2660']
        names = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        #creates 13 cards for each suit
        for suit in suits:
            for name in names:
                deck.append(Card(suit, name))
        #shuffles the deck
        random.shuffle(deck)
class Human(Player):
    #instance creates a hand for the human and starts the hand value
    def __init__(self, target):
        self.hand = []
        self.hand_value = 0
        super().__init__()
class Game():
    #creates the instances for the games and calls the player/dealer
    def __init__(self):
        self.dealer = Dealer(self)
        self.player = Human(self)

    def start_game(self):
        self.dealer.generate_deck()
        self.dealer.deal_card(self.dealer)
        self.dealer.deal_card(self.dealer)
        print("\nThe Dealer's Hand:\n")
        print(self.dealer.hand[0])
        print("\nHIDDEN...")
        self.player.adding_score(self.dealer)
        self.player.show_score(self.dealer)
        if self.dealer.hand_value == 21:
            return "BLACKJACK! Dealer Won!"
        #gives two cards to the player
        self.player.deal_card(self.player)
        self.player.deal_card(self.player)
        print(f"\nThe Player's Hand:")
        #shows the cards the dealer was given
        self.player.show_hand(self.player)
        #adds the value of the cards given
        self.player.adding_score(self.player)
        #if the player's value of cards equals to 21 then it is a blackjack and it wins
        self.player.show_score(self.player)
        if self.player.hand_value == 21:
            return "BLACKJACK! Player Won!"


    def hit_or_stand(self):
        while True:
            print("$"*40)
            question = input("\nWould you like to hit/stand?Enter 'quit' to quit the game!").lower()
            while question not in {'hit', 'stand', 'quit'}:
                question = input("\nINVALID ANSWER! Would you like to hit/stand?Enter 'quit' to quit the game!").lower()
            #as long as the human doesn't enter quit, the game will continue
            if question == 'hit':
                #the cards are shuffled again
                random.shuffle(deck)
                #the dealer receives a card, their updated hand is shown, and their updated hand value
                self.dealer.deal_card(self.dealer)
                print("\nThe Dealer's Hand:\n")
                print(self.dealer.hand[0])
                print("\nHIDDEN...")
                self.player.adding_score(self.dealer)
                self.player.show_score(self.dealer)
                #if the dealer's hand value equals 21 or more then it is a bust
                if self.dealer.hand_value >= 21:
                    print("BUST")
                    play_again = input("Would you like to play again? Enter 'yes' or 'no'.")
                    if play_again == 'yes':
                        main()
                    elif play_again == 'no':
                        print("THANKS FOR PLAYING")
                        break


                print(f"\nThe Player's Hand:")
                #the player receives a card, their updated hand is shown, and their updated hand value
                self.dealer.deal_card(self.player)
                self.player.show_hand(self.player)
                self.player.adding_score(self.player)
                self.player.show_score(self.player)
                #if the player's hand value equals 21 or more then it is a bust
                if self.player.hand_value >= 21:
                    print("BUST")
                    play_again = input("Would you like to play again? Enter 'yes' or 'no'.")
                    if play_again == 'yes':
                        main()
                    elif play_again == 'no':
                        print("THANKS FOR PLAYING")
                        break


            if question == 'stand':
                #both dealer and player scores will be added up
                self.player.adding_score(self.dealer)
                self.player.adding_score(self.player)
                #if the player's score is higher than the dealers then the player wins and both hands are shown
                if self.player.hand_value > self.dealer.hand_value:
                    print(f"\nThe Player's Hand: {self.player.hand[0]} | {self.player.hand[1]}\nValue: {self.player.hand_value}\n")
                    print(f"\nThe Dealer's Hand: {self.dealer.hand[0]} | HIDDEN...\nValue: {self.dealer.hand_value}\n")
                    print("\nPLAYER WON!\n")
                    play_again = input("Would you like to play again? Enter 'yes' or 'no'.")
                    if play_again == 'yes':
                        main()
                    elif play_again == 'no':
                        print("THANKS FOR PLAYING")
                        break


                #if the dealer's score is higher than the players then the dealer wins and both hands are shown
                elif self.player.hand_value < self.dealer.hand_value:
                    print(f"\nThe Player's Hand: {self.player.hand[0]} | {self.player.hand[1]}\nValue: {self.player.hand_value}\n")
                    print(f"\nThe Dealer's Hand: {self.dealer.hand[0]} | HIDDEN...\nValue: {self.dealer.hand_value} \n")
                    print("\nDEALER WON!\n")
                    play_again = input("Would you like to play again? Enter 'yes' or 'no'.")
                    if play_again == 'yes':
                        main()
                    elif play_again == 'no':
                        print("THANKS FOR PLAYING")
                        break



def main():
    play = Game()
    play.start_game()
    play.hit_or_stand()

main()
