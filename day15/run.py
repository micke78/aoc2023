#!/usr/bin/env python3
import re

def read_input(filename):
    with open(filename) as f:
        steps = f.read().replace('\n','').split(',')
    return steps

def hash(input):
    value = 0
    for char in input:
        value = (value + ord(char))*17 % 256
    return value

def remove_lens(box, label):
    for lens in box['content']:
        if label == lens["label"]:
            box['content'].remove(lens)
            return

def set_lens(box, label, focal):
    for lens in box["content"]:
        if label == lens["label"]:
            lens["focal"] = focal
            return
    box["content"].append({"label": label, "focal": focal})

def apply_seq(boxes, seq):
    label, operation, focal = re.match(r'(\w+)([=-])(\d*)', seq).groups()
    box = boxes[hash(label)]
    if operation == '-':
        remove_lens(box, label)
    if operation == '=':
        set_lens(box, label, int(focal))

def box_focal_power(box):
    powers = [ (pos+1) * lens["focal"] for pos, lens in enumerate(box["content"]) ]
    return box["id"] * sum(powers)

def part1(sequences):
    vals = [hash(step) for step in sequences]
    print(sum(vals))

def part2(sequences):
    boxes = [{"id": i+1, "content": []} for i in range(256)]
    for seq in sequences:
        apply_seq(boxes, seq)
    powers = [ box_focal_power(box) for box in boxes ]
    print(sum(powers))
    
def main():
    sequences = read_input('day15/input.txt')
    part1(sequences)
    part2(sequences)

if __name__ == "__main__":
    main()