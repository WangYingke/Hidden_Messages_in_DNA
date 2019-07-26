#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' HAMMING DISTANCE '

__author__ = ' WANG YINGKE '

def ComputeHammingDist(p,q):
    length = len(p)
    hamming_distance = 0
    for i in range(length):
        if p[i]!=q[i]:
            hamming_distance += 1
    return hamming_distance

#DEBUG
""" p = "GGGCCGTTGGT"
q = "GGACCGTTGAC" """
#DEBUG

fin = open("C:/Users/Administrator/Desktop/dataset_9_3.txt","r")
p = fin.readline().rstrip()
q = fin.readline().rstrip()
fin.close()

hamming_distance = ComputeHammingDist(p,q)

print(hamming_distance,end="")