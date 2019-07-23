#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Frequent Words Module '

__author__ = 'Yingke Wang'

def PatternMatch(pattern, genome):
    pos=[]
    pattern_len = len(pattern)
    genome_len = len(genome)
    for i in range(0,genome_len-pattern_len+1):
        if genome[i:i+pattern_len]==pattern:
            pos.append(i)
    return pos

if __name__ == "__main__":
    #debug
    """ pattern = "ATAT"
    genome = "GATATATGCATATACTT"
    pos = PatternMatch(pattern,genome)
    print(str(pos)[1:-1]) """
    #debug

    fin = open("C:/Users/Administrator/Desktop/dataset_3_5.txt","r")
    data_set = fin.readlines()
    pattern = data_set[0].rstrip()
    genome = data_set[1].rstrip()
    pos = PatternMatch(pattern,genome)
    fin.close()
    fout = open("C:/Users/Administrator/Desktop/out.txt","w")
    for element in pos:
        print(element," ",file = fout)
    fout.close()
    
