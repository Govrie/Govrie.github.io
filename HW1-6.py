#!/usr/bin/env python3 -tt
"""File: hello.py """

def get_larger_perimeter(L):
    max_perim = 0
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            for k in range(j + 1, len(L)):
                if (L[i] + L[j] > L[k]) and (L[i] + L[k] > L[j]) and (L[j] + L[k] > L[i]):
                    if max_perim < L[i] + L[j] + L[k]:
                        max_perim = L[i] + L[j] + L[k]
    if max_perim > 0:
        return max_perim
    else:
        print("Net takix otrezkov")
        return 0
#Run only if called as a script
if __name__ == "__main__":
    L = [-4.1, 6.22, 4.333, 1.4444, 100.55555, 0.666666, 8.7777777]
    print(get_larger_perimeter(L))
