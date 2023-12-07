#!/usr/bin/env python3
import string

CARDS = "AKQJT98765432"
JOKER_CARDS = "AKQT98765432J"
COMBINATIONS = [[5], [4], [3, 2], [3], [2, 2], [2], [1]]
#                A    B      C     D      E     F    G
def parse_input(filename):
    hands = []
    with open(filename) as f:
        lines = f.read().split('\n')
    for line in lines:
        if line:
            cards, bid = line.split(' ')
            hands.append({"cards": cards, "bid": int(bid)})
    return hands

def compile_cards(cards, with_joker):
    allcards = JOKER_CARDS if with_joker else CARDS
    samecounts = [ cards.count(card) for card in allcards]
    if with_joker:
        joker_count = samecounts.pop()
    samecounts.sort(reverse=True)
    if with_joker:
        samecounts[0] = min(samecounts[0] + joker_count, 5)                

    cardvalues = "".join([strength(card, with_joker) for card in cards])
    return samecounts, cardvalues

def strength(card, with_joker):
    allcards = JOKER_CARDS if with_joker else CARDS
    return string.ascii_uppercase[allcards.index(card)]

def rank_string(cards, with_joker=False):
    samecounts, cardvalues = compile_cards(cards, with_joker)
    for index, combination in enumerate(COMBINATIONS):
        if samecounts[:len(combination)] == combination:
            return f"{string.ascii_uppercase[index]}{cardvalues}"

def play(hands, with_joker):
    evaluated_cards = [ {"bid": hand["bid"], "rank": rank_string(hand["cards"], with_joker) } for hand in hands ]
    evaluated_cards.sort(key=lambda x: x["rank"], reverse = True)
    score = sum([ (i+1)*c["bid"] for i, c in enumerate(evaluated_cards) ])
    print(score)

def main():
    hands = parse_input("day7/input.txt")
    play(hands, with_joker=False)
    play(hands, with_joker=True)

if __name__ == "__main__":
    main()