#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:32:35 2023

@author: Alex
"""

#Alex Shane, ashane4

def encode_sequence (message):
    for letter in message:
        letter_in_binary = bin(ord(letter))
        #print (letter_in_binary)
        print (binary_to_nucleotide (letter_in_binary))

def binary_to_nucleotide (num):
    nucleotide = ""
    for i in range (2, len(num), 2):
        pair = num[i:i+2]
        if pair == "00":
            nucleotide += "A"
        elif pair == "01":
            nucleotide += "T"
        elif pair == "10":
            nucleotide += "C"
        else:
            nucleotide += "G"
    return (nucleotide)

encode_sequence ("Frieza")
print (bin(ord('a')))