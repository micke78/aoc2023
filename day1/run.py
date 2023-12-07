#!/usr/bin/env python3

import re

def get_int(line):
    first_digit = re.search('\d', line).group(0)
    last_digit = re.search('(\d)[^\d]*$', line).group(1)
    return int(f'{first_digit}{last_digit}')

def get_sum(data):
    suma, sumb = 0, 0
    for line in data.split('\n'):
        if not line:
            continue
        suma += get_int(line)
        sumb += get_int(compile(line))
    return suma, sumb

def compile(line):
    numbers=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    newline=""
    while line:
        for number, string in enumerate(numbers):
            if line.startswith(string):
                newline += str(number)
                break
        else:
            newline += line[0]
        line = line[1:]
    return newline


with open('day1/input.txt') as f:
    data=f.read()

print(get_sum(data))
