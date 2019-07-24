#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Clump Finding Module -- strightforward brutal force, naive way '

__author__ = 'Yingke Wang'

def PatternCount(text, pattern):
    count =0
    text_len = len(text)
    pattern_len = len(pattern)
     
    for i in range(0,text_len-pattern_len+1):
        if text[i:i+pattern_len] == pattern:
            count = count + 1
    return count

def ClumpFinding(genome,k,L,t):
    genome_length = len(genome)
    clump = []
    for i in range(0,genome_length-L+1):
        region = genome[i:i+L]
        for j in range(0,L-k+1):
            pattern = region[j:j+k]
            pattern_count = PatternCount(region,pattern)
            if pattern_count>=t:
                clump.append(pattern)
    clump = list(set(clump))
    return clump

if __name__ == "__main__":
    #debug case
    """ genome = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA" 
    k = 5
    L = 50
    t = 4
    clump = ClumpFinding(genome,k,L,t)
    print(clump) """
    #debug case
    fin = open("C:/Users/Administrator/Desktop/dataset_4_5.txt","r")
    data_set = fin.readlines()
    #print(data_set)
    genome = data_set[0].rstrip()
    k = int(data_set[1].rstrip())
    L = int(data_set[2].rstrip())
    t = int(data_set[3].rstrip())
    clump = ClumpFinding(genome,k,L,t)
    fin.close()
    fout = open("C:/Users/Administrator/Desktop/out.txt","w")
    for c in clump:
        print(c,file=fout)
    fout.close()
    



