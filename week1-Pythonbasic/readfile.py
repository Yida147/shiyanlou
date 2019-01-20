#!/usr/bin/env python3
filename = input('Enter file path:')
try:
    f = open(filename)
    print(f.read())
    f.close()
except FileNotFoundError as err:
    print('Erro: {0}'.format(err))
