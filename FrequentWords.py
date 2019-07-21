#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Frequent Words Module '

__author__ = 'Yingke Wang'


def PatternCount(text, pattern):
    count =0
    text_len = len(text)
    pattern_len = len(pattern)
     
    for i in range(0,text_len-pattern_len+1):#right side of the range excluded, the same for string truncation.
        if text[i:i+pattern_len] == pattern:
            count = count + 1
    return count

def FrequentWords(text,k): #where k is the length of the pattern.
    frequent_patterns=[]
    count=[]
    text_len = len(text)
    for i in range(0,text_len-k+1):
        pattern = text[i:i+k]
        pattern_count = PatternCount(text,pattern)
        count.append(pattern_count)
        max_count = max(count)
    for i in range(0,text_len-k+1):
        if count[i] == max_count:
            frequent_patterns.append(text[i:i+k])
    frequent_patterns = list(set(frequent_patterns))
    return frequent_patterns

if __name__ == "__main__":
    with open("C:/Users/Administrator/Desktop/dataset_2_10.txt","r") as f:
        data = f.readlines()
        text = data[0].rstrip()
        k = int(data[1].rstrip())
    frequent_patterns = FrequentWords(text,k)
    print("Frequent Patterns =",frequent_patterns)