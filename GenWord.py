#! usr/bin/env python3
# -*- coding: UTF-8 -*-

from os import system
from itertools import permutations

system('clear')

print('''\n
                         .........
  ...................../| GENWORD |......................
 /:                                                     : 
 /:     .----- VERSION -----.   .------ AUTHOR -----.   :
 /:     [        2.0        ]   [  ©2020 - Ayckinn  ]   :
 /:     '-------------------'   '-------------------'   :
 /:                                                     : 
 /:  .------------------ DESCRIPTION -----------------. :
 /:  [ Generate all possibles combinations for a word ] :
 /:  '------------------------------------------------' :
 /:.....................................................:
 ///////////////////////////////////////////////////////
''')

user_word = input("\nPlease choose a word : ")
len_word = len(user_word)

def random_word():
    word_list = [''.join(x) for x in permutations(user_word, len_word)]
    counter = 0

    for word in word_list:
        counter += 1

    print()
    print('\n'.join(word_list))
    print(f"\nThere are \033[1;31m{len_word}\033[1;m letters in your word and"
          f" \033[1;32m{counter}\033[1;m combinations\n")


random_word()