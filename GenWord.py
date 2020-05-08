#! usr/bin/env python3
# -*- coding: UTF-8 -*-

# =================================================
# =                GENWORD - V1.0                 =
# = Generate all possible combinaisons for a word =
# =                                               =
# =               ©2020 - Ayckinn                 =
# =================================================

from os import system
from itertools import permutations

system('clear')

# /////////////////////////////////////////////////////////////////////////////

user_word = input("\nPlease choose a word : ")
len_word = len(user_word)

def random_word():
    word_list = [''.join(x) for x in permutations(user_word, len_word)]

    counter = 0
    for word in word_list:
        counter += 1

    print()
    print('\n'.join(word_list))
    print("\nIl y a \033[1;31m{}\033[1;m lettres dans le mot et \033[1;32m{}\033[1;m combinaisons possibles\n".format(len_word, counter))

# /////////////////////////////////////////////////////////////////////////////
random_word()

# /////////////////////////////////////////////////////////////////////////////
# TODO : Create an external file to store results for each word