import random  

name = input("Whats your name bro? ").lower()

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
        '7': 7, '8': 8, '9': 9, '10': 10, 
        'J': 10, 'Q': 10, 'K': 10, 'A': 11
    }
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit, ranks[rank]))
    random.shuffle(deck)
    return deck

def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        score += card[2]
        if card[0] == 'A':
            aces += 1
    # Convert Aces from 11 to 1 if score exceeds 21
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def play_blackjack():
    print("--- Welcome to Blackjack dude! ---")
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    while True:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        
        print(f"\nAlright {name} you have: {[c[0] + ' of ' + c[1] for c in player_hand]} (Score: {player_score})")
        print(f"I have a: {dealer_hand[0][0]} of {dealer_hand[0][1]}")

        if player_score == 21:
            print(f"Blackjack! You win! Congrats {name}")
            return
        if player_score > 21:
            print(f"Bust! You went over 21. You lose. typa greed they talk about in the bible c'mon {name}")
            return

        choice = input("Do you want to [hit] or [stand]? ").lower()
        if choice == 'hit':
            player_hand.append(deck.pop())
        elif choice == 'stand':
            break

    # Dealer's turn
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"\nYour final hand kid: {[c[0] + ' of ' + c[1] for c in player_hand]} (Score: {player_score})")
    print(f"My final hand: {[c[0] + ' of ' + c[1] for c in dealer_hand]} (Score: {dealer_score})")

    if dealer_score > 21 or player_score > dealer_score:
        print("You win bro good looks!")
    elif player_score < dealer_score:
        print("I win brodie!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    while True:
        play_blackjack()
        if input("\nWanna Play again? (y/n): ").lower() != 'y':
            break
