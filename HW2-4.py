#!/usr/bin/env python3 -tt
"""File: hello.py """

def get_most_frequent(words, k):
    words_len_list = list()
    words_value_list = list()
    for word in sorted(words):
        word_count = 0
        for i in words:
            if word == i:
                word_count +=1
        words_len_list.append(word_count)
        words_value_list.append(word)
    words_dict = dict(zip(words_value_list, words_len_list))
    words_value_list = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
    words_value_list = [v for v, k in words_value_list]
    return words_value_list[:k]
#Run only if called as a script
if __name__ == '__main__':
    words = ["hello", "world", "hello", "my", "dear", "world", "hello"]
    k = 3
    print(get_most_frequent(words, k))

