#!/usr/bin/env python3

import re

def is_symbol(matrix, line, column):
    if line >= 0 and line < len(matrix):
        if column >= 0 and column < len(matrix[line]):
            return matrix[line][column] not in '1234567890.'
    return False

def check_surrounding(matrix, line, column, length):
    for check_col in range(column - 1, column + length + 1):
        if is_symbol(matrix, line - 1, check_col) or is_symbol(matrix, line + 1, check_col):
            return True
    if is_symbol(matrix, line, column - 1) or is_symbol(matrix, line, column + length):
        return True
    return False

def parse_input(filename):
    matrix = []
    with open(filename) as f:
        for line in f.read().split('\n'):
            if line:
                matrix.append(line) 
    numbers = []
    for lineno, content in enumerate(matrix):
        for number in re.findall('\d+',content):
            column = content.index(number)
            content = content.replace(number, '.'*len(number), 1)
            if check_surrounding(matrix, lineno, column, len(number)):
                numbers.append(int(number))
    return numbers


def is_multiply(matrix, line, column):
    if line >= 0 and line < len(matrix):
        if column >= 0 and column < len(matrix[line]):
            if matrix[line][column] == '*':
                return f"({line},{column})"
    return False

def check_for_multiply(matrix, line, column, length):
    for check_col in range(column - 1, column + length + 1):
        for offset in [-1, 1]:
            mul = is_multiply(matrix, line + offset, check_col)
            if mul:
                return mul
    for offset in [-1, length]:
        mul = is_multiply(matrix, line, column + offset)
        if mul:
            return mul
    return False

def parse_inputb(filename):
    matrix = []
    with open(filename) as f:
        for line in f.read().split('\n'):
            if line:
                matrix.append(line) 
    multiplies = {}
    for lineno, content in enumerate(matrix):
        for number in re.findall('\d+',content):
            column = content.index(number)
            content = content.replace(number, '.'*len(number), 1)
            mul = check_for_multiply(matrix, lineno, column, len(number))
            if mul:
                if mul in multiplies:
                    multiplies[mul].append(int(number))
                else:
                    multiplies[mul] = [int(number)]
    numbers = []
    for nums in multiplies.values():
        if len(nums) == 2:
            numbers.append(nums[0]*nums[1])
    return numbers

def main():
    print(sum(parse_input("day3/input.txt")))
    print(sum(parse_inputb("day3/input.txt")))

if __name__ == "__main__":
    main()