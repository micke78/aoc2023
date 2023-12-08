#!/usr/bin/env python3
import re
from pprint import pprint
from math import lcm

def parse_input(filename):
    with open(filename) as f:
        lines = f.read().split('\n')    
    instructions = {"directions": lines.pop(0)}
    for line in lines:
        if line:
            match = re.match(r'(\w+)\s*=\s*\(\s*(\w+)\s*,\s*(\w+)\s*\)', line)
            if match:
                this, left, right = match.groups()
                instructions[this] = {"L": left, "R":right}
    return instructions

def follow_path(instructions):
    steps = 0
    location = "AAA"
    directions = instructions["directions"]
    while location != "ZZZ":
        move = directions[steps % len(directions)]
        location = instructions[location][move]
        steps += 1
    return steps

def ghost_follow_path(instructions):
    locations = [p for p in instructions if p.endswith("A")]
    directions = instructions["directions"]
    periods = []
    for location in locations:
        states=[]
        while True:
            step = len(states) % len(directions)
            states.append(f"{location}{step}")
            move = directions[step]
            location = instructions[location][move]
            try:
                offset = states.index(f"{location}{step + 1}")
                length = len(states) - offset
                break
            except ValueError:
                pass
        zloc = [i for i,loc in enumerate(states) if loc[2] == "Z"]
        periods.append({"offset":offset, "length":length, "zloc": zloc})
    return periods


def main():
    instructions = parse_input("day8/input.txt")
    print(follow_path(instructions))
    periods = ghost_follow_path(instructions)
    pprint(periods)
    l = [p['length'] for p in periods]
    print(lcm(*l))


if __name__ == "__main__":
    main()