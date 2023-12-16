#!/usr/bin/env python3


moveids = { "left":  1, "right": 2, "up":    4, "down":  8 }

items = {
    "|": {
        "left":  [ "up", "down" ],
        "right": [ "up", "down" ],
        "up":    [ "up" ],
        "down":  [ "down" ],
    },
    "-": {
        "left":  [ "left" ],
        "right": [ "right" ],        
        "up":    [ "left", "right" ],
        "down":  [ "left", "right" ],
    },
    "/": {
        "left":  [ "down" ],
        "right": [ "up" ],        
        "up":    [ "right" ],
        "down":  [ "left" ],
    },
    "\\": {
        "left":  [ "up" ],
        "right": [ "down" ],        
        "up":    [ "left" ],
        "down":  [ "right" ],        
    },
}

moves = {
    "left":  {"row": 0,  "col": -1},
    "right": {"row": 0,  "col": 1},
    "up":    {"row": -1, "col": 0},
    "down":  {"row": 1,  "col": 0}
}

class Map():
    def __init__(self, filename):
        with open(filename) as f:
            input = f.read().split('\n')
            self.map = [l for l in input if l]
            self.reset_visited()

    def reset_visited(self):
        self.visited = ["0"*len(l) for l in self.map]

    def get_item(self, row, col):
        if row < 0 or col < 0 or row >= len(self.map) or col >= len(self.map[row]):
            return "X" 
        return self.map[row][col]

    def set_visited(self, row, col, item):
        s = self.visited[row]
        self.visited[row] = s[:col] + item + s[col + 1:]

    def get_visited(self, row, col):
        return int(self.visited[row][col], 16)

    def move(self, row, col, move):
        newrow = row + moves[move]["row"]
        newcol = col + moves[move]["col"]
        item = self.get_item(newrow,newcol)
        if item == "X":
            return []
        if self.revisit(newrow, newcol, move):
            return []
        if item in items:
            return [{"row": newrow, "col": newcol, "move": i} for i in items[item][move]]
        return [{"row": newrow, "col": newcol, "move": move}]

    def revisit(self, row, col, move):
        visitstatus = self.get_visited(row, col)
        been_before = ( visitstatus & moveids[move] == moveids[move] )
        visitstatus = visitstatus | moveids[move]
        self.set_visited(row, col, f'{visitstatus:X}')
        return been_before

    def print(self):
        for row in self.visited:
            print(row)

    def get_visit_count(self):
        visited = 0
        for row in self.visited:
            for char in row:
                if char in "123456789ABCDEF":
                    visited += 1
        return visited


def get_energized(map, start):
    paths = [
        start
    ]
    map.reset_visited()
    while paths:
        newpaths = []
        for location in paths:
            newpaths +=  map.move(**location)
        paths = newpaths
    return map.get_visit_count()

def part1(map):
    print(get_energized(map, { "row": 0, "col": -1, "move": "right" }))

def part2(map):
    en = 0
    for row in range(len(map.map)):
        en2 = get_energized(map, { "row": row, "col": -1, "move": "right" })
        en = max(en,en2)
        en2 = get_energized(map, { "row": row, "col": len(map.map[row]), "move": "left" })
        en = max(en,en2)

    for col in range(len(map.map[0])):
        en2 = get_energized(map, { "row": -1, "col": col, "move": "down" })
        en = max(en,en2)
        en2 = get_energized(map, { "row": len(map.map), "col": col, "move": "up" })
        en = max(en,en2)
    print(en)

    
def main():
    map = Map("day16/input.txt")
    part1(map)
    part2(map)

if __name__ == "__main__":
    main()