#!/usr/bin/env pyhton3
import sys
for arg in sys.argv[1:]:
    if len(arg) > 3:
        print(arg)
    else:
        pass
