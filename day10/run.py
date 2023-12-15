#!/usr/bin/env python3

nextmoves = {
    "F": {"left":"down", "up":"right"},
    "-": {"right":"right", "left":"left"},
    "7": {"right":"down", "up":"left"},
    "|": {"up":"up", "down":"down"},
    "J": {"down":"left", "right":"up"},
    "L": {"down":"right", "left":"up"},
}

moves = {
    "left": {"row": 0, "col": -1},
    "right": {"row": 0, "col": 1},
    "up": {"row": -1, "col": 0},
    "down": {"row": 1, "col": 0}
}

class Map():
    def __init__(self, filename):
        with open(filename) as f:
            input = f.read().split('\n')
            self.map = [l for l in input if l]

    def get_item(self, row, col):
        try:
            return self.map[row][col]
        except:
            return '.'

    def find_start(self):
        for row, content in enumerate(self.map):
            if "S" in content:
                return {"row": row, "col": content.index("S")}

    def move(self, row, col, move):
        newrow = row + moves[move]["row"]
        newcol = col + moves[move]["col"]
        item = self.get_item(newrow,newcol)
        if item == "S":
            return {"row": newrow, "col": newcol, "move": None}
        if item == '.' or move not in nextmoves[item]:
            return None
        return {"row": newrow, "col": newcol, "move": nextmoves[item][move]}

    def prettyprint():
        pass

def part1(map):
    steps = 0
    starting_point = map.find_start()
    paths = [
        {**starting_point, "move": "left"},
        {**starting_point, "move": "right"},
        {**starting_point, "move": "up"},
        {**starting_point, "move": "down"}
    ]
    while True:
        newpaths = []
        steps += 1
        for location in paths:
            newpos = map.move(**location)
            if newpos:
                newpaths.append(newpos)
                if newpos["row"] == starting_point["row"] and newpos["col"] == starting_point["col"]:
                    break
        else:
            paths = newpaths
            continue
        break
    return steps//2

    
def main():
    map = Map("day10/input.txt")
    print(part1(map))

if __name__ == "__main__":
    main()