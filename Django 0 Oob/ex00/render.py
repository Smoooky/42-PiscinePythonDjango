#!/usr/bin/env python3

from settings import *
import sys
import os


def main():
    if len(sys.argv) != 2:
        return print("only one argument needed")
    if not os.path.splitext(sys.argv[1])[1] == '.template':
        return print("file with extension .template needed")
    if not os.path.isfile(sys.argv[1]):
        return print("file not exist")

    with open(sys.argv[1], 'r') as templ_file:
        data = templ_file.read()

    with open(sys.argv[1][:-9] + '.html', 'w') as out_file:
        out_file.write(data.format_map(globals()))


if __name__ == '__main__':
    main()
