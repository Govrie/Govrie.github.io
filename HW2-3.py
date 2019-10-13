#!/usr/bin/env python3 -tt
"""File: hello.py """

def count_unique_codes(words):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    morse_base = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    morse_dict = dict(zip(abc, morse_base))
    morse_set = set()
    for word in words:
        morse_word = ''
        for i in range(len(word)):
            morse_word = morse_word + morse_dict[word[i]]
        morse_set.add(morse_word)
    return len(morse_set)
#Run only if called as a script
if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg"]
    print(count_unique_codes(words))
