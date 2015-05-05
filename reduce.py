#!/usr/bin/python

import sys, collections, ast, fileinput

def main(argv):
    all_freqs = collections.defaultdict(int)
    file = sys.stdin
    file.readline()
    while True:
        line = file.readline().strip()
        if line == '':
            break
        freqs = ast.literal_eval(line)
        for freq in freqs:
            all_freqs[freq] += 1
    print all_freqs

if __name__ == "__main__":
    main(sys.argv)
