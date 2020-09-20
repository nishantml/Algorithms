"""

Given a List of words, return the words that can be typed using letters of alphabet on only one row's
of American keyboard like the image below.






Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]


Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

"""

from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'];
        row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

        inteligentWords = []

        for word in words:
            Hash = {'first': 0, 'second': 0, 'third': 0}
            for letter in list(word.lower()):
                if letter in row1:
                    Hash['first'] = Hash['first'] + 1

                if letter in row2:
                    Hash['second'] = Hash['second'] + 1

                if letter in row3:
                    Hash['third'] = Hash['third'] + 1

            if Hash['first'] == len(word) or Hash['second'] == len(word) or Hash['third'] == len(word):
                inteligentWords.append(word)

        return inteligentWords
