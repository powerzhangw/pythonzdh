# -*- coding: UTF-8 -*-
from testing.william import module


l = [1, 3, 5, 7, 2, 4, 8, 10, 9]
# module.selectSort(l)
# print(l)

def sub_sort(array, low, high):
    pivotkey = array[low]
    while low < high:
        while low < high and array[high] >= pivotkey:  # 从右向左，找到第一个小于pivotkey的索引
            high -= 1
        array[low] = array[high]
        while low < high and array[low] <= pivotkey:  # 从左向右，找到第一个大于pivotkey的索引
            low += 1
        array[high] = array[low]
    array[low] = pivotkey
    return low

def quick_sort(array,low,high):
    if low < high :
        pivoloc=sub_sort(array,low,high)
        quick_sort(array,low,pivoloc-1)
        quick_sort(array,pivoloc+1,high)


quick_sort(l,0,len(l)-1)
print(l)
