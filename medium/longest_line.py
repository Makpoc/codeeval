#!/usr/bin/env python2.7
import sys

test_cases = open(sys.argv[1], 'r')

rows_to_print = int(test_cases.readline())
all_rows = {}

for test in test_cases:
    test = test.strip('\n')
    
    if len(test) == 0:
        continue
        
    all_rows[len(test)] = test
    
index = 0
result = []
for key in sorted(all_rows, reverse=True):
    if index == rows_to_print:
        print '\n'.join(result)
        
    result.append(all_rows[key])
    index += 1
    

test_cases.close()
