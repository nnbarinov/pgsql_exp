from os import close


import os

with open('sql.txt', 'r') as f:
    for line in f.readlines():
        print(line)
f.close()