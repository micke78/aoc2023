#!/usr/bin/env python3

from functools import reduce


def load_universe(filename):
    with open(filename) as f:
        return [ l for l in f.read().split('\n') if l ]

def get_all_galaxies(universe):
    cols =  len(universe[0])
    data = "".join(universe)
    last = -1
    galaxies = []
    while True:
        try:
            last = data.index("#", last + 1)
            galaxies.append({"row": last // cols, "col": last % cols})
        except:
            break
    return galaxies

def get_distance(point1, point2):
    return abs(point1["row"] - point2["row"]) + abs(point1["col"] - point2["col"])

def calculate_distances(point, galaxies):
    return sum([get_distance(point, galaxy) for galaxy in galaxies])

def expand_universe(galaxies, times):
    universe_size = reduce(lambda acc, next: {"rows": max(next["row"], acc["rows"]), "cols": max(next["col"], acc["cols"])}, galaxies, {"rows":0, "cols": 0})
    for row in range(universe_size["rows"], -1, -1):
        if not ["X" for gal in galaxies if gal["row"] == row]:
            for galaxy in galaxies:
                if galaxy["row"] > row:
                    galaxy["row"] += (times - 1) 

    for col in range(universe_size["cols"], -1, -1):
        if not ["X" for gal in galaxies if gal["col"] == col]:
            for galaxy in galaxies:
                if galaxy["col"] > col:
                    galaxy["col"] += (times - 1) 

def get_distances(galaxies):
    distance = 0
    while galaxies:
        galaxy = galaxies.pop()
        distance += calculate_distances(galaxy, galaxies)
    return distance

def part1(universe):
    galaxies = get_all_galaxies(universe)
    expand_universe(galaxies, 2)
    print(get_distances(galaxies))

def part2(universe):
    galaxies = get_all_galaxies(universe)
    expand_universe(galaxies, 1000000)
    print(get_distances(galaxies))

def main():
    universe = load_universe("day11/input.txt")
    part1(universe)
    part2(universe)

if __name__ == "__main__":
    main()