# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:41:53 2024

@author: Jacob

Bubble Sort Algorithm
"""

def bubbleSort(array: list) -> list:
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(array)

if __name__ == '__main__':
    array = [5, 2, 3, 8, 0, 4, 6, 7, 1]
    print(array)
    bubbleSort(array)