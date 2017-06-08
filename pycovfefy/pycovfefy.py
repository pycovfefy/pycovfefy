# -*- coding: utf-8 -*-
import string


NON_VOWELS = 'bcdfghjklmnpqrstvwxz'


def is_vowel(char):
    return char not in NON_VOWELS


def char_mapper(char):
    dictionary = 'pgtvkhjglmnbqrzdfwxs'
    return dictionary[NON_VOWELS.index(char)]


def get_covfefe(word):
    first_vowel_found = False
    first_consonant_after_first_vowel_found = False
    result = ''
    for i in word:
        if is_vowel(i) and not first_vowel_found:
            first_vowel_found = True
        if i in NON_VOWELS and first_vowel_found:
            c = char_mapper(i)
            first_consonant_after_first_vowel_found = True
            result += i
        if i not in NON_VOWELS and first_consonant_after_first_vowel_found:
            result += c
            result += i
            result += c
            result += i
            return result
        if not first_consonant_after_first_vowel_found:
            result += i
    return result


def covfefy(words):
    words = words.translate(None, string.punctuation)
    words = words.split(' ')
    return ' '.join([get_covfefe(word) for word in words])
