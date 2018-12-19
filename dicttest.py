#!/usr/bin/env python3
import sys

output_dict = {}
output_list = []
print_data = []

def handle_data(param):
    param = param.split(':')
    output_dict = {param[0]:param[1]}
    return output_dict

def resolve_data(param1,param2):
    output_list.append('ID:{}'.format(param1))
    output_list.append('Name:{}'.format(param2))
    return output_list

if __name__ == '__main__':

    for arg in sys.argv[1:]:
        output_dict = handle_data(arg)
        for key in output_dict:
            print_data = resolve_data(key,output_dict[key])
    print_data = ' '.join(print_data)
    print(print_data)
        
