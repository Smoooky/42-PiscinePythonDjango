#!/usr/bin/env python3

def my_var():
    variables = (
        42,  # int
        '42', # str
        'quarante-deux', #str
        42.0,  # float
        True,  # bool
        [42],  # list
        {42: 42},  # dict
        (42, ),  # tuple
        set()  # set
    )
    output = ''
    for var in variables:
        print(var, "has a type", type(var))


if __name__ == '__main__':
    my_var()
