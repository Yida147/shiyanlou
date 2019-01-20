#!/usr/bin/env python3
import sys
sys_input = int(sys.argv[1])
if sys_input >= 0 and sys_input < 10:
    print('you belong to kids')
elif sys_input >= 10 and sys_input < 18:
    print('you belong to teenager')
elif sys_input >= 18 and sys_input < 30:
    print('you belong to adult')
elif sys_input >= 30 and sys_input < 60:
    print('you belong to older')
elif sys_input >= 60 and sys_input < 120:
    print('you belong to oldest')
else:
    pass
