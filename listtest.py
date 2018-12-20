#!/usr/bin/env python3
import sys
long_str = []
short_str = []
for i in sys.argv[1:]:
    if len(i) <= 3:
        long_str.append(i)
    else:
        short_str.append(i)
for n in long_str:
    if n != long_str[-1]:
        print(n,end=" ")
    else:
        print(n,end="\n")
for m in short_str:
    if m != short_str[-1]:
        print(m,end=" ")
    else:
        print(m,end="\n")
