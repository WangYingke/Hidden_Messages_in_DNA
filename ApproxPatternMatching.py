#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' APPROXIMATED PATTERN MATCHING PROBLEM '

__author__ = ' WANG YINGKE '

def ComputeHammingDist(p,q):
    length = len(p)
    hamming_distance = 0
    for i in range(length):
        if p[i]!=q[i]:
            hamming_distance += 1
    return hamming_distance

def ApproxPatternPos(pattern,gene,d):
    pos = []
    l = len(pattern)
    gene_len = len(gene)
    for i in range(gene_len-l+1):
        sub_pattern = gene[i:i+l]
        hamming_dist = ComputeHammingDist(pattern,sub_pattern)
        if hamming_dist <= d:
            pos.append(i)
    return pos

#DEBUG
""" pattern = "ATTCTGGA"
gene = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
d = 3 """
#DEBUG

fin = open("C:/Users/Administrator/Desktop/dataset_9_4.txt","r")
data = fin.readlines()
pattern = data[0].rstrip()
gene = data[1].rstrip()
d = int(data[2].rstrip())
fin.close()

fout = open("C:/Users/Administrator/Desktop/out.txt","w")
pos = ApproxPatternPos(pattern,gene,d)
for i in pos:
    print(i,"",end="",file = fout)

    
