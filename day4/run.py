#!/usr/bin/env python3

from functools import reduce
import re

def parse_input(filename):
    cards = []
    with open(filename) as f:
        for line in f.read().split('\n'):
            if line:
                number_type = "winning"
                cards.append({"winning": [], "having": [], "instances": 1})
                for field in re.sub(r"Card\s+\d+: ", "", line).split(' '):
                    if not field:
                        continue
                    if field == "|":
                        number_type = "having"
                    if field.isdigit():
                        cards[-1][number_type].append(int(field))
    return cards

def factoral(n):
    return reduce(lambda x,y:x*2,[1]*n)

def winning_nums(card):
    return list(filter(lambda number: number in card['having'], card['winning']))

def card_score(card):
    winning = winning_nums(card)
    if winning:
        return factoral(len(winning))
    return 0

def get_scores(cards):
    return [card_score(card) for card in cards]

def win_copies(cards):
    for card_no, card in enumerate(cards):
        no_of_winning = len(winning_nums(card))
        for copycard in cards[card_no + 1:card_no + 1 + no_of_winning]:
            copycard["instances"] += card["instances"]
    return [card["instances"] for card in cards]

def main():
    cards = parse_input("day4/input.txt")
    scores = get_scores(cards)
    print(sum(scores))

    card_counts = win_copies(cards)
    print(sum(card_counts))

if __name__ == "__main__":
    main()