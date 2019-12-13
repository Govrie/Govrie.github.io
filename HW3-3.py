#!/usr/bin/env python3 -tt
"""File: hello.py """
def cyclic_string_generator(filename):
    while True:
        with open(filename, "r") as f:
            for line in f:
                yield line.strip()

if __name__ == '__main__':
    gen = cyclic_string_generator("file.txt")
    for i, line in enumerate(gen):
        print(line)
        if i > 20:
            break
