import sys

source_filepath = '/home/shiyanlou/shiyanlou.txt'
copy_filepath = '/home/shiyanlou/shiyanlou_copy.txt'


def copyfile(filepath,copy_filepath):
    with open(filepath,'r') as scr_file:
        with open(copy_filepath,'w') as copy_file:
            for line in scr_file.readlines():    
                copy_file.write(line)

def add_num(filepath):
    with open(filepath,'r') as file: 
        copyfile = file.readlines()
        space = []
        for i,line in enumerate(copyfile,start=1):
            space.append(str(i)+' '+line)
    with open(filepath,'w') as file_writer:
        for element in space:
            file_writer.write(element)
                  

copyfile(source_filepath,copy_filepath)
add_num(copy_filepath)
with open(copy_filepath) as file:
    for line in file:
        print(line)
#readfile(copy_filepath)        
