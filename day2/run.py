#!/usr/bin/env python3

import re

def parse_input(filename):
    with open(filename) as f:
        data=f.read().split('\n')

    games = {}
    gameno = '0'
    for line in data:
        while line:
            match = re.match('Game (\d+): (.*)', line)
            if match:
                gameno = match.group(1)
                games[gameno] = [{}]
                line = match.group(2).strip()

            match = re.match('(\d+) (\w+),? ?(.*)',line)
            if match:
                count = int(match.group(1))
                color = match.group(2)
                games[gameno][-1][color] = count
                line = match.group(3).strip()

            match = re.match('; (.*)',line)
            if match:
                games[gameno].append({})
                line = match.group(1).strip()
    return games

def find_valids(games, limits):
    valids=[]
    for gameno, rounds in games.items():
        isvalid = True
        for round in rounds:
            for color, count in round.items():
                if count > limits[color]:
                    isvalid = False
        if isvalid:
            valids.append(int(gameno))
    return valids

def get_powers(games):
    powers = []
    for rounds in games.values():
        max = {}
        for round in rounds:
            for color, count in round.items():
                if not color in max or count > max[color]:
                    max[color] = count
        power = 1
        for count in max.values():
            power *= count
        powers.append(power)
    return powers

def main():
    games = parse_input("day2/input.txt")
    valids = find_valids(games, { "red": 12, "green": 13, "blue": 14 })
    print(sum(valids))
    powers = get_powers(games)
    print(sum(powers))

if __name__ == "__main__":
    main()