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


def get_abbreviation(name: str, states: dict) -> str:
    try:
        return states[name]
    except KeyError:
        return None


def get_capital(abbr: str, capital_cities: dict) -> float:
    return capital_cities[abbr]


def main():
    if len(sys.argv) != 2:
        return
    name = sys.argv[1].lower().capitalize()
    abbr = get_abbreviation(name, get_dict_by_name('states'))
    if abbr is not None:
        print(get_capital(abbr, get_dict_by_name('capital_cities')))
    else:
        print('Unknown state')


if __name__ == '__main__':
    main()
