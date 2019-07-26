#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' MINIMUM SKEW PROBLEM '

__author__ = ' WANG YINGKE '

#Compute the difference between #G and #C, define skew = #G-#C in a linearized genome
def ComputeSkew(genome):
    skew = []
    genome_len = len(genome)
    for i in range(genome_len+1):
        skew.append(0)
    
    for i in range(genome_len):
        if genome[i]=='C':
            skew[i+1]=skew[i]-1
        elif genome[i]=='G':
            skew[i+1]=skew[i]+1
        else:
            skew[i+1]=skew[i]
    return skew

def FindMinIdx(genome):
    min_idx = []
    skew = ComputeSkew(genome)
    genome_len = len(genome)
    min_skew = min(skew)
    if skew[-1]==min_skew:
        min_idx.append(genome_len-1)
    
    for i in range(genome_len):
        if skew[i] == min_skew:
            min_idx.append(i)

    return min_idx

fin = open("C:/Users/Administrator/Desktop/dataset_7_6.txt","r")
genome = fin.readline().rstrip()
#print(genome)
fin.close()

min_idx = FindMinIdx(genome)
fout = open("C:/Users/Administrator/Desktop/out.txt","w")
for i in min_idx:
    print(i,"",end="",file=fout)
fout.close() 