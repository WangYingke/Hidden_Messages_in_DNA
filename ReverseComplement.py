#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Reverse Complement Module '

__author__ =  "Wang Yingke"

def ReverseComplement(text):
    dna_seq = text.rstrip()#attention, here the input file has a \n at the end!!!
    dna_seq_rever = reversed(dna_seq)
    str_rever_compl = ""
    for i in dna_seq_rever:
        if i=="A":
            str_rever_compl = str_rever_compl+"T"
        elif i=="T":
            str_rever_compl = str_rever_compl+"A"
        elif i=="C":
            str_rever_compl = str_rever_compl+"G"
        else:
            str_rever_compl = str_rever_compl+"C"
    return str_rever_compl

if __name__ == "__main__":
    #debug block
    """ rev_comp_dna_seq = ReverseComplement("AAAACCCGGT")
    print(rev_comp_dna_seq) """
    #debug block

    f_in = open("C:/Users/Administrator/Desktop/dataset_3_2.txt","r")
    data_set = f_in.readlines()
    dna_seq = data_set[0]
    rev_comp_dna_seq = ReverseComplement(dna_seq)
    f_in.close()
    
    f_out = open("C:/Users/Administrator/Desktop/out.txt","w")
    print(rev_comp_dna_seq,file = f_out)
    f_out.close()
       


