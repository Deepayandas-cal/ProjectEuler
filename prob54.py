import urllib.request
from collections import Counter

CARD_ORDER = "23456789TJQKA"
HAND_STRENGTHS = {
    "High Card": 1, "One Pair": 2, "Two Pair": 3, "Three of a Kind": 4, "Straight": 5,
    "Flush": 6, "Full House": 7, "Four of a Kind": 8, "Straight Flush": 9
}

def get_card_values(hand):
    values = sorted([CARD_ORDER.index(rank) for rank, _ in hand], reverse=True)
    return [3, 2, 1, 0, -1] if values == [12, 3, 2, 1, 0] else values

def evaluate_hand(hand):
    values = get_card_values(hand)
    counts = Counter(values)
    sorted_counts = sorted(counts.values(), reverse=True)
    ranked_values = sorted(counts.keys(), key=lambda x: (-counts[x], -x))
    is_flush = len(set(suit for _, suit in hand)) == 1
    is_straight = values == list(range(values[0], values[0] - 5, -1))

    if is_flush and is_straight: return ("Straight Flush", ranked_values)
    if sorted_counts == [4, 1]: return ("Four of a Kind", ranked_values)
    if sorted_counts == [3, 2]: return ("Full House", ranked_values)
    if is_flush: return ("Flush", ranked_values)
    if is_straight: return ("Straight", ranked_values)
    if sorted_counts == [3, 1, 1]: return ("Three of a Kind", ranked_values)
    if sorted_counts == [2, 2, 1]: return ("Two Pair", ranked_values)
    if sorted_counts == [2, 1, 1, 1]: return ("One Pair", ranked_values)
    return ("High Card", ranked_values)

def determine_winner(hand1, hand2):
    rank1, values1 = evaluate_hand(hand1)
    rank2, values2 = evaluate_hand(hand2)
    return 1 if HAND_STRENGTHS[rank1] > HAND_STRENGTHS[rank2] or (HAND_STRENGTHS[rank1] == HAND_STRENGTHS[rank2] and values1 > values2) else 2

def fetch_hands():
    url = "https://projecteuler.net/resources/documents/0054_poker.txt"
    return urllib.request.urlopen(url).read().decode("utf-8").strip().split("\n")

def main():
    player_one_wins = sum(determine_winner([(c[0], c[1]) for c in line.split()[:5]], [(c[0], c[1]) for c in line.split()[5:]]) == 1 for line in fetch_hands())
    print(f"Player 1 wins {player_one_wins} times.")

if __name__ == "__main__":
    main()
