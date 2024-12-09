import random

def deal_card():
    """Return a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(hand):
    """Calculate the score of a given hand."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def blackjack():
    """Main game logic."""
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    game_over = False
    while not game_over:
        if calculate_score(player_hand) == 0 or calculate_score(player_hand) > 21:
            game_over = True
        else:
            action = input("Type 'hit' to get another card or 'stand' to pass: ").lower()
            if action == "hit":
                player_hand.append(deal_card())
            else:
                game_over = True

        print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")

    while calculate_score(dealer_hand) != 0 and calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    print(f"Dealer's final hand: {dealer_hand}, final score: {calculate_score(dealer_hand)}")
    print(f"Your final hand: {player_hand}, final score: {calculate_score(player_hand)}")

    if calculate_score(player_hand) > 21:
        return "You went over. You lose."
    elif calculate_score(dealer_hand) > 21 or calculate_score(player_hand) > calculate_score(dealer_hand):
        return "You win!"
    elif calculate_score(player_hand) < calculate_score(dealer_hand):
        return "You lose."
    else:
        return "Draw!"