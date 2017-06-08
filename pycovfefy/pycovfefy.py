# -*- coding: utf-8 -*-
import string


class Covfefy(object):

    def __init__(self):

        self.non_vowels = 'bcdfghjklmnpqrstvwxz'

    def is_vowel(self, char):
        return char not in self.non_vowels

    def char_mapper(self, char):
        dictionary = 'pgtvkhjglmnbqrzdfwxs'
        return dictionary[self.non_vowels.index(char)]

    def get_covfefe(self, word):
        first_vowel_found = False
        first_consonant_after_first_vowel_found = False
        result = ''
        for i in word:
            if self.is_vowel(i) and not first_vowel_found:
                first_vowel_found = True
            if i in self.non_vowels and first_vowel_found:
                c = self.char_mapper(i)
                first_consonant_after_first_vowel_found = True
                result += i
            if i not in self.non_vowels and first_consonant_after_first_vowel_found:
                result += c
                result += i
                result += c
                result += i
                return result
            if not first_consonant_after_first_vowel_found:
                result += i
        return result

    def transform(self, s):
        s = s.translate(None, string.punctuation)
        s = s.split(' ')
        return ' '.join([self.get_covfefe(word) for word in s])
