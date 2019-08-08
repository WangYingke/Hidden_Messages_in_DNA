#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' COMPUTE FREQUENCIES WITH MISMATCHES '

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

def ComputeHammingDist(p,q):
    length = len(p)
    hamming_distance = 0
    for i in range(length):
        if p[i]!=q[i]:
            hamming_distance += 1
    return hamming_distance

def GenerateNeighbors(pattern,d):
    nucleotides = ['A','T','C','G']
    if d == 0:
        return pattern 
    pattern_len = len(pattern)
    if pattern_len == 1:
        return ['A','T','C','G']
    neighborhood = set()
    pattern_suffix = pattern[1:pattern_len]
    neighbor_suffix = GenerateNeighbors(pattern_suffix,d)
    neighborhood.add(pattern)
    for text in neighbor_suffix:
        if ComputeHammingDist(pattern_suffix,text)<d:
            for nucleotide in nucleotides:
                neighborhood.add(nucleotide+text)
        else:
            neighborhood.add(pattern[0]+text)
    return neighborhood

def ComputeFreqWithMismatches(gene,k,d):
    gene_len = len(gene)
    freq = []
    for i in range(4**k):
        freq.append(0)
    for i in range(0,gene_len-k+1):
        pattern = gene[i:i+k]
        neighborhood = GenerateNeighbors(pattern,d)
        for element in neighborhood:
            idx = PatternToIndex(element)
            freq[idx] += 1
    return freq

def FindFreqWordsWithMismatches(gene,k,d):
    freq = ComputeFreqWithMismatches(gene,k,d)
    freq_words = set()
    max_count = max(freq)
    for i in range(4**k):
        if freq[i] == max_count:
            pattern = IndexToPattern(i,k)
            freq_words.add(pattern)
    return freq_words

#DEBUG 
gene = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1
freq_words = FindFreqWordsWithMismatches(gene,k,d)
for i in freq_words:
    print(i,"",end="")
#DEBUG 