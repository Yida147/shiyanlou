#!/usr/bin/env python3

def compute(base, value):
    if value not in base:
        base.append(value)
        print(base)
    result = sum(base)
    base.remove(value)
    print(result)

if __name__ == '__main__':
    testlist = [10,20,30]
    compute(testlist, 15)
    compute(testlist, 25)
    compute(testlist, 35)
