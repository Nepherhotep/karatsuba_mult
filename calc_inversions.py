import os
import numpy as np


def load_input_array():
    results = []
    with open('fixtures/inversions.txt') as f:
        for line in f.readlines():
            results.append(int(line.strip()))
    return np.array(results, dtype=int)


def main():
    a = load_input_array()
    for i, value in enumerate(a):
        print(i, value)




if __name__ == '__main__':
    main()
