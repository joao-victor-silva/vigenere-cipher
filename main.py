#!/usr/bin/env python3

import sys
from typing import List, Optional
from string import ascii_lowercase
from argparse import ArgumentParser


letter_frequency_per_language = {
    'portuguese': [
        0.1463,
        0.0104,
        0.0388,
        0.0499,
        0.1257,
        0.0102,
        0.0130,
        0.0128,
        0.0618,
        0.0040,
        0.0002,
        0.0278,
        0.0474,
        0.0505,
        0.1073,
        0.0252,
        0.0120,
        0.0653,
        0.0781,
        0.0434,
        0.0463,
        0.0167,
        0.0001,
        0.0021,
        0.0001,
        0.0047,
    ],
}


def main():
    parser = ArgumentParser()
    parser.add_argument('action', choices=['cipher', 'decipher', 'decrypt'], help='action to do with informed message')
    parser.add_argument('-m', '--message', help='message text to cipher, decipher or break encryption')
    parser.add_argument('-k', '--key', help='key used to cipher the text')
    args = vars(parser.parse_args())
    # print(args)

    data = args.get('message')
    if data is None:
        data = sys.stdin.read()

    match args['action']:
        case 'cipher':
            print(cipher(args['key'], data), end='')
        case _:
            print('invalid option. quiting...')
            exit(1)

if __name__ == "__main__":
    main()
