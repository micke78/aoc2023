#!/usr/bin/env python3

def parse_input(filename):
    data = {
        "seeds": [],
        "mapnames": [],
        "maps":{}
    }

    with open(filename) as f:
        lines = f.read().split('\n')
    for line in lines:
        if line:
            if line.startswith("seeds: "):
                data["seeds"] = [int(n) for n in line.split(' ')[1:]]
                continue
            elif line[0].isdigit():
                d,s,l = line.split(' ')
                data["maps"][data["mapnames"][-1]].append({"dststart": int(d), "start": int(s), "length": int(l)})
            else:
                name = line.split(' ')[0]
                data["mapnames"].append(name)
                data["maps"][name] = []
    return data


def translate(number, mapping):
    for map in mapping:
        if number >= map["start"] and number < map["start"] + map["length"]:
            return number - map["start"] + map["dststart"]
    return number


def seed_to_location(seed_no, data):
    num = seed_no
    for mapname in data["mapnames"]:
        num = translate(num, data["maps"][mapname])
    return num


def parse_seeds(data):
    return  [ seed_to_location(seed, data) for seed in data["seeds"]]


def get_intersection(range_a, range_b):
    istart = max(range_a["start"], range_b["start"])
    iend = min(range_a["start"] + range_a["length"], range_b["start"] + range_b["length"])
    ilength = iend - istart
    if ilength > 0:
        return {"start": istart, "length": ilength}
    return None


def subtractrange(range_a, range_b):
    parts = []
    if range_a["start"] < range_b["start"]:
        parts.append({"start": range_a["start"], "length": min(range_b["start"] - range_a["start"], range_a["length"])})
    start_b = max(range_b["start"] + range_b["length"], range_a["start"])
    end_b = range_a["start"] + range_a["length"]
    if start_b < end_b:
        parts.append({"start": start_b, "length": end_b - start_b})
    return parts


def seed_range_step(seed_ranges, mappings):
    translated_ranges = []
    leftover_ranges = [*seed_ranges]
    for mapping in mappings:
        ranges = leftover_ranges
        leftover_ranges = []
        for range in ranges:
            intersection = get_intersection(range, mapping)
            if intersection:
                translated_ranges.append({"start": intersection["start"] + mapping["dststart"] - mapping["start"], "length": intersection["length"]})
            leftover_ranges += subtractrange(range, mapping)
    translated_ranges += leftover_ranges
    return translated_ranges


def parse_seed_ranges(data):
    input = [*data["seeds"]]
    seed_ranges = []
    while input:
        seed_ranges.append({"start": input.pop(0), "length":input.pop(0)})

    for mapname in data["mapnames"]:
        seed_ranges = seed_range_step(seed_ranges, data["maps"][mapname])
    return seed_ranges


def main():
    data = parse_input("day5/input.txt")
    print(min(parse_seeds(data)))

    locations = parse_seed_ranges(data)
    minloc = min([l["start"] for l in locations])
    print(minloc)


if __name__ == "__main__":
    main()