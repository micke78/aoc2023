#!/usr/bin/env python3
from functools import reduce

def parse_input(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    values = []
    for line in lines:
        if line:
            values.append([int(i) for i in line.split(' ')])
    return values

def calc_diffs(line):
    return [line[i] - line[i-1] for i in range(1,len(line))]

def all_diffs(line):
    diffs = [line]
    while set(diffs[-1]) != {0}:
        diffs.append(calc_diffs(diffs[-1]))
    return diffs

def predict_next(line):
    return reduce(lambda acc, next: acc + next[-1], line, 0 )

def predict_prev(line):
    line.reverse()
    return reduce(lambda acc, next: next[0] - acc, line, 0 )

def part1(diffs):
    return sum([predict_next(l) for l in diffs])

def part2(diffs):
    return sum([predict_prev(l) for l in diffs])

def main():
    values = parse_input("day9/input.txt")
    diffs = [all_diffs(line) for line in values]
    print(part1(diffs))
    print(part2(diffs))

if __name__ == "__main__":
    main()