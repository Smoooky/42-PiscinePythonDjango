#!/usr/bin/env python3

import sys


def get_dict_by_name(name: str) -> dict:
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if name == 'states':
        return states
    elif name == 'capital_cities':
        return capital_cities
    else:
        return None


def print_state(capital):
    states = get_dict_by_name('states')
    capital_cities = get_dict_by_name('capital_cities')

    try:
        abbr = list(capital_cities.keys())[list(capital_cities.values()).index(capital)]
        state_name = list(states.keys())[list(states.values()).index(abbr)]
        print(state_name)
    except ValueError:
        print('Unknown capital city')


def main():
    if len(sys.argv) != 2:
        return
    print_state(sys.argv[1])


if __name__ == '__main__':
    main()
