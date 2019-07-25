#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

' COMPUTE FREQUENCY ARRAY '

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

def FastClumpFinding(genome,k,L,t):
    frequent_patterns = []
    clump = []
    for i in range(4**k):
        clump.append(0)

    region = genome[0:L]
    freq_array = ComputeFrequencies(region,k)
    for i in range(4**k):
            if freq_array[i]>=t:
                clump[i]=1
    
    genome_len = len(genome)
    for i in range(1,genome_len-L+1):
        first_pattern = genome[i-1:i-1+k]
        idx = PatternToIndex(first_pattern)
        freq_array[idx] = freq_array[idx]-1
        last_pattern = genome[i+L-k:i+L]
        idx = PatternToIndex(last_pattern)
        freq_array[idx] = freq_array[idx]+1
        if freq_array[idx]>=t:
            clump[idx]=1

    for i in range(4**k):
        if clump[i]==1:
            pattern = IndexToPattern(i,k)
            #print(pattern)
            frequent_patterns.append(pattern)
    return frequent_patterns

fin = open("C:/Users/Administrator/Desktop/E_coli.txt","r")
genome = fin.readline().rstrip()
params = fin.readline().rstrip().split()
k = int(params[0])
L = int(params[1])
t = int(params[2])
fin.close()

start_time = time.time()
clump_patterns = FastClumpFinding(genome,k,L,t)
size = len(clump_patterns)
end_time = time.time()
print(size)
""" fout = open("C:/Users/Administrator/Desktop/out.txt","w")
clump_patterns = FastClumpFinding(genome,k,L,t)
for pattern in clump_patterns:
    print(pattern," ",end="",file=fout)
fout.close() """

print("Running time =%.9f"%(end_time-start_time))