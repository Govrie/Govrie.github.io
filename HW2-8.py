#!/usr/bin/env python3 -tt
"""File: hello.py """

def get_partition(S):
    stroka1 = []
    first1 = 0
    last1 = get_end_of_right_partition_started_at(S, 0)
    stroka1.append(S[first1:last1 + 1])
    while last1 < len(S) - 1:
        first1 = last1 + 1
        last1 = get_end_of_right_partition_started_at(S, first1)
        stroka1.append(S[first1:last1 + 1])
    return stroka1

def get_end_of_right_partition_started_at(s, first2):
    last2 = get_extreme_indexes_for_char(s, s[first2])[1]
    if last2 > first2:
        cursor = first2 + 1
        while cursor < last2:
            e = get_extreme_indexes_for_char(s, s[cursor])[1]
            if e > last2:
                last2 = e
            cursor += 1
    return last2

def get_extreme_indexes_for_char(s, c):
    last3 = -1
    first3 = s.find(c)
    if first3 != -1:
        last3 = first3
        for i in range(first3 + 1, len(s)):
            if s[i] == c:
                last3 = i
    return [first3, last3]

if __name__ == '__main__':
    print(get_partition("qbqbcbqcqdufugduhxjhklxj"))
    print(get_partition("111222333444555"))
