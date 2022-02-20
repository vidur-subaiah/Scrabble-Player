import re
import itertools
from typing import List

class InputValidator:
    """A class to validate string input from the user"""
    
    def __init__(self,text):
        self.input = text
    
    def validate_input(self):
        '''This method determines whether the InputValidator object has 
        a valid input.
        
        uses the input attribute
        returns: a boolean if valid, incorrect character if invalid'''

        spaces_removed = self.input.replace(' ', '')
        commas_removed = spaces_removed.replace(',', '')
        
        for character in commas_removed:
            if character.isalpha():
                continue
            else:
                return character
        return True
        
    def type_of_input(self):
        '''This method determines what type of input the InputValidator object has.
        
        uses the input attribute
        return: an int 1 or 2 or 3 representing which format, returns false if pattern cannot be found'''

        format1_regex = r"[A-Za-z]+"
        format2_regex = r"[A-Za-z]\s"
        format3_regex = r"[A-Za-z],"

        match1 = re.search(format1_regex, self.input)
        match2 = re.search(format2_regex, self.input)
        match3 = re.search(format3_regex, self.input)

        if match3:
            return 3
        if match2: 
            return 2
        if match1:
            return 1
        return False # if an input pattern could not be found  


class WordGenerator:
    """A class to generate all permutations of letters from a string of letters"""

    def __init__(self, letters) :
        self.letter_string = letters
    
    def word_possibilities(self):
        '''This method returns all permutations of the letters in the letter_string attribute
        
        uses the letter_string attribute
        returns: a set'''

        words = set()
        for i in range(1, len(self.letter_string)+ 1):
            letter_permutations = itertools.permutations(self.letter_string, i)
            letter_combinations = itertools.combinations_with_replacement(self.letter_string, i)
            for item in letter_permutations:
                words.add(item)
            for item in letter_combinations:
                words.add(item)
        return words


class WordValidator:
    """A class used to determine whether words are valid Scrabble words"""

    def __init__(self, set_of_words):
        self.total_word_set = set_of_words
    
    def valid_words(self):
        '''This method takes in the words in the total_word_set attribute,
         and checks to see if each word is a valid word in the game of scrabble. It returns a list of the words
        that are valid.
        
        uses the total_word_set attribute
        returns: a list'''

        file = open('scrabble_list.txt', 'r')
        contents = file.read()
        cleaned_contents = contents.strip()
        list_of_scrabble_words = cleaned_contents.split('\n')
        file.close()
        valid_word_list = []
        for each_tuple in self.total_word_set:
            word = ''
            for character in each_tuple:
                word += character
            if word.upper() in list_of_scrabble_words:
                valid_word_list.append(word)
        return valid_word_list


class Word:
    """A class that stores a word, it's length, and scrabble score"""

    def __init__(self, word):
        self.string = word
        self.length = len(word)
        self.word_score(word)
    
    def word_score(self,word):
        sum_score = 0
        for character in word:
            sum_score += self.letter_score(character)
        self.score = sum_score
    
    def letter_score(self, character):
        tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                 "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                 "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                 "x": 8, "z": 10}
        return tile_score[character]






