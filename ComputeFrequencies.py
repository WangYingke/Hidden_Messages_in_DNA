#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

' IMPROVED CLUMP FINDING '

__author__ = ' WANG YINGKE '

def PatternToIndex(pattern):
    index = 0
    pattern_len = len(pattern)
    nucleotide_code = {'A':0,'C':1,'G':2,'T':3}
    for i in range(pattern_len):
        index += nucleotide_code[pattern[i]]*4**(pattern_len-i-1)
    return index

def IndexToPattern(index,k):
    nucleotide_code = {0:"A",1:"C",2:"G",3:"T"}
    pattern = ""
    for i in range(k):
        reminder = index%4
        nucleotide = nucleotide_code[reminder]
        pattern += nucleotide
        index = index//4
        i+=1
    pattern = pattern[::-1]
    return pattern

def ComputeFrequencies(text,k):
    text_len = len(text)
    frequencies = []
    for i in range(4**k):
        frequencies.append(0)
    for i in range(0,text_len-k+1):
        pattern = text[i:i+k]
        idx = PatternToIndex(pattern)
        frequencies[idx] = frequencies[idx]+1
    return frequencies

start_time = time.time()
fin = open("C:/Users/Administrator/Desktop/dataset_2994_5.txt","r")
text = fin.readline().rstrip()
k = int(fin.readline().rstrip())
fin.close()

fout = open("C:/Users/Administrator/Desktop/out.txt","w")
frequencies = ComputeFrequencies(text,k)
for i in frequencies:
    print(i," ",end="",file=fout)
fout.close()
end_time = time.time()

print("Running time =%.9f"%(end_time-start_time))

