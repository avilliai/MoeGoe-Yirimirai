import numpy as np


def readConfig(txt):
    f = open(txt)
    line = f.readline()
    data_list = []
    while line:
        line = f.readline()
        data_list.append(line)
        print(line)
    f.close()
    return data_list

if __name__ == '__main__':
    txt = r"Config\moyu\groups.txt"
    groupList = readConfig(txt)
    for i in groupList:
        print(type(i))