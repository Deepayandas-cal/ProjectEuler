import urllib.request
from collections import Counter

CARD_RANKS = "23456789TJQKA"
HAND_RANKINGS = {
    "High Card": 1,
    "One Pair": 2,
    "Two Pair": 3,
    "Three of a Kind": 4,
    "Straight": 5,
    "Flush": 6,
    "Full House": 7,
    "Four of a Kind": 8,
    "Straight Flush": 9
}

def get_card_ranks(cards):
    ranks = sorted([CARD_RANKS.index(rank) for rank, _ in cards], reverse=True)
    if ranks == [12, 3, 2, 1, 0]:  # Adjust for Ace-low straight
        return [3, 2, 1, 0, -1]
    return ranks

def is_flush(cards):
    return len(set(suit for _, suit in cards)) == 1

def is_straight(ranks):
    return ranks == list(range(ranks[0], ranks[0] - 5, -1))

def get_hand_rank(cards):
    ranks = get_card_ranks(cards)
    rank_counts = Counter(ranks)
    sorted_counts = sorted(rank_counts.values(), reverse=True)
    rank_values = sorted(rank_counts.keys(), key=lambda x: (-rank_counts[x], -x))

    flush = is_flush(cards)
    straight = is_straight(ranks)

    if flush and straight:
        return ("Straight Flush", rank_values)
    if sorted_counts == [4, 1]:
        return ("Four of a Kind", rank_values)
    if sorted_counts == [3, 2]:
        return ("Full House", rank_values)
    if flush:
        return ("Flush", rank_values)
    if straight:
        return ("Straight", rank_values)
    if sorted_counts == [3, 1, 1]:
        return ("Three of a Kind", rank_values)
    if sorted_counts == [2, 2, 1]:
        return ("Two Pair", rank_values)
    if sorted_counts == [2, 1, 1, 1]:
        return ("One Pair", rank_values)
    return ("High Card", rank_values)

def compare_hands(hand1, hand2):
    rank1, ranks1 = get_hand_rank(hand1)
    rank2, ranks2 = get_hand_rank(hand2)

    if HAND_RANKINGS[rank1] > HAND_RANKINGS[rank2]:
        return 1
    elif HAND_RANKINGS[rank1] < HAND_RANKINGS[rank2]:
        return 2
    else:
        return 1 if ranks1 > ranks2 else 2

def parse_hand(input_str):
    return [(card[0], card[1]) for card in input_str.split()]

def fetch_poker_data():
    url = "https://projecteuler.net/resources/documents/0054_poker.txt"
    with urllib.request.urlopen(url) as response:
        data = response.read().decode("utf-8")
    return data.strip().split("\n")

def main():
    hands = fetch_poker_data()
    player1_wins = 0
    
    for hand in hands:
        cards = hand.split()
        hand1, hand2 = parse_hand(" ".join(cards[:5])), parse_hand(" ".join(cards[5:]))
        if compare_hands(hand1, hand2) == 1:
            player1_wins += 1
    
    print(f"Player 1 wins {player1_wins} times.")

if __name__ == "__main__":
    main()