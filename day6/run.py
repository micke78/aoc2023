#!/usr/bin/env python3
from functools import reduce
from math import sqrt, ceil, floor

def parse_input(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    times = [ int(v) for v in lines[0].split(':')[1].split(' ') if v ]
    dists = [ int(v) for v in lines[1].split(':')[1].split(' ') if v ]
    return times, dists

def parse_input2(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    time = int(lines[0].split(':')[1].replace(' ', ''))
    dist = int(lines[1].split(':')[1].replace(' ', ''))
    return time, dist

def multiply(lst):
    return reduce(lambda x,y:x*y,lst)

def dist(mindist, maxtime):
    longest = floor(maxtime/2 + sqrt((maxtime/2)**2-mindist-.1))
    shortest = ceil(maxtime/2 - sqrt((maxtime/2)**2-mindist-.1))
    return longest - shortest + 1

def main():
    times, dists = parse_input("day6/input.txt")
    ways = [ dist(d,t) for d,t in zip(dists, times) ]
    print(multiply(ways))

    time, dst = parse_input2("day6/input.txt")
    print(dist(dst,time))


if __name__ == "__main__":
    main()