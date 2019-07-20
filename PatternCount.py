#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Pattern Count Module '

__author__ = 'Yingke Wang'


def PatternCount(text, pattern):
     count =0
     text_len = len(text)
     pattern_len = len(pattern)
     
     for i in range(0,text_len-pattern_len+1):
         if text[i:i+pattern_len] == pattern:
             count = count + 1
     return count

if __name__ == "__main__":
   with open("C:/Users/Administrator/Desktop/dataset_2_7.txt","r") as f:
       data_set = f.readlines()
       dna_seq = data_set[0].rstrip()
       #print(dna_seq)
       pattern = data_set[1].rstrip()
       print(pattern)
       count = PatternCount(dna_seq,pattern)
       print('count =',count)
