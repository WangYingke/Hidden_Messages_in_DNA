#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' GENERATE NEIGHBORS '

__author__ = ' WANG YINGKE '

def ComputeHammingDist(p,q):
    length = len(p)
    hamming_distance = 0
    for i in range(length):
        if p[i]!=q[i]:
            hamming_distance += 1
    return hamming_distance

def SingleMutation(pattern):
    nucleotides = ['A','T','C','G']
    single_mutation = []
    pattern_len = len(pattern)
    for i in range(0,pattern_len):
        symbol = pattern[i]
        for nucleotide in nucleotides:
            if nucleotide != symbol:
                pattern[i]=nucleotide
                single_mutation.append(pattern)
                pattern[i]=symbol
    return single_mutation

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

#DEBUG
""" pattern = "ACG"
d = 1
neighborhood = GenerateNeighbors(pattern,d)
for element in neighborhood:
    print(element,"",end="") """
#DEBUG

fin = open("C:/Users/Administrator/Desktop/dataset_3014_4.txt","r")
params = fin.readlines()
pattern = params[0].rstrip()
d = int(params[1].rstrip())
fin.close()

fout = open("C:/Users/Administrator/Desktop/out.txt","w")
neighborhood = GenerateNeighbors(pattern,d)
for element in neighborhood:
    print(element,"",end="",file=fout)
fout.close()


