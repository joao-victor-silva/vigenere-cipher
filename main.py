#!/usr/bin/env python3

import sys
from math import ceil, floor
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
    'english': [
        0.08167,
        0.01492,
        0.02782,
        0.04253,
        0.12702,
        0.02228,
        0.02015,
        0.06094,
        0.06966,
        0.00153,
        0.00772,
        0.04025,
        0.02406,
        0.06749,
        0.07507,
        0.01929,
        0.00095,
        0.05987,
        0.06327,
        0.09056,
        0.02758,
        0.00978,
        0.02360,
        0.00150,
        0.01974,
        0.00074, 
    ],
}


def cipher(key: str, message: str) -> str:
    key_stream = key.lower() * ((len(message) // len(key)) + 1)
    key_stream = key_stream[0:len(message)]

    encrypted_message = ''

    plain_text_letter = ''
    for i in range(len(message)):
        # remap letters with accents and ç
        plain_text_letter = remap_letter(message[i])

        # skip spaces, punctuation, etc.
        if plain_text_letter not in ascii_lowercase:
            encrypted_message += message[i]
            continue

        # cipher letter
        encrypted_letter = -2 * ord('a')
        encrypted_letter += ord(plain_text_letter) + ord(key_stream[i]) 
        encrypted_message += chr((encrypted_letter % 26) + ord('a'))

    return encrypted_message

def decipher(key: str, encrypted_message: str) -> str:
    key_stream = key.lower() * ((len(encrypted_message) // len(key)) + 1)
    key_stream = key_stream[0:len(encrypted_message)]

    decrypted_message = ''

    for i in range(len(encrypted_message)):
        # skip spaces, punctuation, etc.
        if encrypted_message[i] not in ascii_lowercase:
            decrypted_message += encrypted_message[i]
            continue

        decrypted_letter = ord(encrypted_message[i]) - ord(key_stream[i]) 
        if decrypted_letter < 0:
            decrypted_letter += 26

        decrypted_message += chr(decrypted_letter + ord('a'))

    return decrypted_message

def scalar_product(rhs: List[float], lhs: List[float]) -> float:
    value = 0
    for i, j in zip(rhs, lhs):
        value += i * j
    return value


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
        case 'decipher':
            print(decipher(args['key'], data), end='')
        case _:
            print('invalid option. quiting...')
            exit(1)

def remap_letter(letter: str) -> str:
    mapped_letters = {
        'á': 'a',
        'â': 'a',
        'ã': 'a',
        'à': 'a',
        'ä': 'a',
        'å': 'a',
        'é': 'e',
        'ê': 'e',
        'ẽ': 'e',
        'è': 'e',
        'í': 'i',
        'î': 'i',
        'ĩ': 'i',
        'ì': 'i',
        'ó': 'o',
        'ô': 'o',
        'õ': 'o',
        'ò': 'o',
        'ö': 'o',
        'ú': 'u',
        'û': 'u',
        'ũ': 'u',
        'ù': 'u',
        'ü': 'u',
        'ç': 'c',
    }

    # remap letter with accents and ç
    if letter.lower() in mapped_letters.keys():
        return mapped_letters[letter.lower()]

    return letter.lower()


if __name__ == "__main__":
    main()
