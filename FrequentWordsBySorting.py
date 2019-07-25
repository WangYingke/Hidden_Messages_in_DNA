#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

' FIND FREQUENT WORDS BY SORTING '

__author__ = ' WANG YINGKE '

def PatternToIndex(pattern):
    index = 0
    pattern_len = len(pattern)
    nucleotide_code = {'A':0,'C':1,'G':2,'T':3}
    for i in range(pattern_len):
        index += nucleotide_code[pattern[i]]*4**(pattern_len-i-1)
    return index

def IndexToPattern(index,length):
    nucleotide_code = {0:"A",1:"C",2:"G",3:"T"}
    pattern = ""
    for i in range(length):
        reminder = index%4
        nucleotide = nucleotide_code[reminder]
        pattern += nucleotide
        index = index//4
        i+=1
    pattern = pattern[::-1]
    return pattern

def SortFrequentWords(text,k):
    text_len = len(text)
    frequent_patterns = []
    index = []
    count = []
    for i in range(0,text_len-k+1):
        pattern = text[i:i+k]
        idx = PatternToIndex(pattern)
        index.insert(i,idx)
        count.append(1)
    sorted_index = sorted(index)
    for i in range(1,text_len-k+1):
        if sorted_index[i-1]==sorted_index[i]:
            count[i]=count[i-1]+1
    max_count = max(count)
    for i in range(0,text_len-k+1):
        if count[i]==max_count:
            pattern=IndexToPattern(sorted_index[i],k)
            frequent_patterns.append(pattern)
    
    return frequent_patterns

if __name__ == "__main__":
    start_time = time.time()
    #DEBUG
    text = 'AAGCAAAGGTGGG'
    k=2
    frequent_words = SortFrequentWords(text,k)
    print(frequent_words)
    #DEBUG
    
    end_time = time.time()
    print("Running time =%.9f" %(end_time-start_time))