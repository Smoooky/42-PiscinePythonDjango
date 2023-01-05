#!/usr/bin/env python3

def print_nums():
    try:
        with open("numbers.txt", 'r') as f:
            for line in f.readlines():
                line = line.strip()
                nums = line.split(",")
                for num in nums:
                    print(num)
    except FileNotFoundError:
        print('file numbers.txt needed')


if __name__ == '__main__':
    print_nums()
