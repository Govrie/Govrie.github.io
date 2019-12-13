#!/usr/bin/env python3 -tt
"""File: hello.py """

def cyclic_string_generator(filename):
    while True:
        with open(filename, "r") as f:
            for line in f:
                yield line.strip()

if __name__ == '__main__':
    gen = cyclic_string_generator("file.txt")
    filtered_nod = filter(lambda x: "NOD19" in x, gen)
    for i, line in enumerate(filtered_nod):
        print(line)
        if i > 50:
            break

