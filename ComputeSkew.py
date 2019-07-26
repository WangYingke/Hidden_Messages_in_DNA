#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' COMPUTE SKEW '

__author__ = ' WANG YINGKE '

#Compute the difference between #G and #C, define skew = #G-#C in a linearized genome
def ComputeSkew(genome):
    skew = []
    genome_len = len(genome)
    for i in range(genome_len+1):
        skew.append(0)
    
    for i in range(len(genome)):
        if genome[i]=='C':
            skew[i+1]=skew[i]-1
        elif genome[i]=='G':
            skew[i+1]=skew[i]+1
        else:
            skew[i+1]=skew[i]
    return skew

genome = "GAGCCACCGCGATA"
skew = ComputeSkew(genome)
fout = open("C:/Users/Administrator/Desktop/out.txt","w")
for i in skew:
    print(i,"",end="",file=fout)
fout.close() 
