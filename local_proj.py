import sys
import os

root_dir = str(sys.argv[1])
main_names = ['input', 'src', 'models', 'notebooks', 'notes']

def create():
    # create directory 
    for i in range(0, len(main_names)):
        dir_name = str(root_dir) + '/' + str(main_names[i])
        os.makedirs(dir_name)

if __name__ == "__main__":
    create()