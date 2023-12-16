#!/usr/bin/env python3

def load_patterns(filename):
    patterns = []
    with open(filename) as f:
        input = f.read()
    for line in input.split('\n\n'):
        patterns.append([l for l in line.split('\n') if l])
    return patterns

def almost_equal(line1, line2, one_off_ok):
    if line1 == line2:
        return True, one_off_ok
    if one_off_ok:
        numoffs = len(["x" for a,b in zip(line1, line2) if a!=b])
        if numoffs == 1:
            return True, False
    return False, one_off_ok

def get_horisontal_reflection_line(pattern, smudge = False):
    one_off_ok = False
    for line1, content in enumerate(pattern[1:]):
        equal, one_off_ok = almost_equal(content, pattern[line1], smudge)
        if equal:
            line2 = line1 + 1
            for offset in range(1, min(line2, len(pattern) - line2)):
                equal, one_off_ok = almost_equal(pattern[line1 - offset], pattern[line2 + offset], one_off_ok)
                if not equal:
                    break
            else:
                 if not one_off_ok:
                     return line2
    return 0

def get_column(col, pattern):
    return "".join([ row[col] for row in pattern ])

def get_vertical_reflection_line(pattern, smudge = False):
    translated_pattern = [get_column(no, pattern) for no in range(len(pattern[0]))]
    return get_horisontal_reflection_line(translated_pattern, smudge)

def find_reflections(patterns, smudge=False):
    sum = 0
    for pattern in patterns:
        hline = get_horisontal_reflection_line(pattern, smudge)
        vline = get_vertical_reflection_line(pattern, smudge)
        sum += 100 * hline + vline
    print(sum)

def main():
    patterns = load_patterns("day13/input.txt")
    find_reflections(patterns)
    find_reflections(patterns, True)

if __name__ == "__main__":
    main()