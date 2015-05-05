#!/usr/bin/python

import sys, collections, ast, fileinput

def main(argv):
    all_freqs = collections.defaultdict(int)
    for line in fileinput.input():
        freqs = ast.literal_eval(line.strip())
        for freq in freqs:
            all_freqs[freq] += 1
    print all_freqs

if __name__ == "__main__":
    main(sys.argv)
