#-*- coding: utf-8-*-



import os
import re



def fileter(input_words_list):
    with open('filtered_words.txt', 'r', encoding='utf-8') as k:
        words = k.read().splitlines()
        k.close()
    if not set(input_words_list).intersection(words):
        print('Human Rights')
    else:
        print('Freedom')


if __name__ == '__main__':
    input_words_list = input('Input some words:').split()
    fileter(input_words_list)
