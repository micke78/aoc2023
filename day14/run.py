#!/usr/bin/env python3

class Map():
    def __init__(self, filename):
        with open(filename) as f:
            self.restore(f.read())

    def print(self):
        for line in self.map:
            print(line)

    def dump(self):
        return "\n".join(self.map)
    
    def restore(self, dump):
        input = dump.split('\n')
        self.map = [ l for l in input if l ]

    def get_item(self, row, col):
        return self.map[row][col]

    def set_item(self, row, col, item):
        s = self.map[row]
        self.map[row] = s[:col] + item + s[col + 1:]

    def try_move(self, row, col, new_row, new_col):
        item = self.get_item(row, col)
        if self.get_item(new_row, new_col) == '.' and item == 'O':
            self.set_item(new_row, new_col, self.get_item(row, col))
            self.set_item(row, col, '.')
            return True
        return False

    def roll_south(self):
        did_change = False
        for row in range(len(self.map) - 2, -1, -1):
            for col in range(len(self.map[row])):
                if self.try_move(row, col, row + 1, col):
                    did_change = True
        return did_change

    def roll_north(self):
        did_change = False
        for row in range(1, len(self.map)):
            for col in range(len(self.map[row])):
                if self.try_move(row, col, row - 1, col):
                    did_change = True
        return did_change

    def roll_east(self):
        did_change = False
        for row in range(len(self.map)):
            for col in range(len(self.map[row]) - 2, -1, -1) :
                if self.try_move(row, col, row, col + 1):
                    did_change = True
        return did_change

    def roll_west(self):
        did_change = False
        for row in range(len(self.map)):
            for col in range(1, len(self.map[row])):
                if self.try_move(row, col, row, col - 1):
                    did_change = True
        return did_change

    def calculate_load(self):
        sum = 0
        for row, content in enumerate(self.map):
            sum += (len(self.map) - row) * content.count('O')
        return sum
    
def part1(map):
    while map.roll_north():
        pass
    print(map.calculate_load())

def part2(map):
    dumps = [map.dump()]
    loopcount = 1000000000
    while True:
        while map.roll_north():
            pass
        while map.roll_west():
            pass
        while map.roll_south():
            pass
        while map.roll_east():
            pass
        dump = map.dump()
        if dump in dumps:
            break
        dumps.append(dump)
    offset = dumps.index(dump)
    period = len(dumps) - offset
    pos = (loopcount - offset) % period + offset
    map.restore(dumps[pos])
    print(map.calculate_load())

def main():
    map = Map("day14/input.txt")
    part1(map)
    part2(map)

if __name__ == "__main__":
    main()