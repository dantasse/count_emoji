#!/usr/bin/env python

import ast
from collections import Counter

combined = Counter()
infiles = ['part-00000', 'part-00001', 'part-00002']
for file in infiles:
    filestr = open(file).read()
    filestr = filestr.split('>,')[1]
    filestr = filestr.split(')')[0].strip()
    dict1 = ast.literal_eval(filestr)

    combined.update(dict1)

print combined
