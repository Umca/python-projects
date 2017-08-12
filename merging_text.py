import os
import datetime

def get_file_name():
    d = datetime.datetime.now()
    return d.strftime("%Y-%m-%d-%H-%M-%S-%f") + '.txt'

def create_file():
    file_name = get_file_name()
    new_file = open(file_name, 'w+')
    dir = 'files/'
    for file in os.listdir(path="./files"):
        f = open(dir + file, 'r')
        for line in f:
            new_file.write(line + '\n')
    new_file.close()

create_file()
