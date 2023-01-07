#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:32:35 2023

@author: Alex
"""

#Alex Shane, ashane4

def encode_sequence (message):
    encoded = ""
    for letter in message:
        letter_in_binary = format(ord(letter), '08b')
        #print (letter_in_binary)
        encoded += binary_to_nucleotide (letter_in_binary)
    print (encoded)
    print (encoded == "TATCTGACTCCTTCTTTGCCTCAT")

def binary_to_nucleotide (num):
    nucleotide = ""
    for i in range (0, len(num), 2):
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
#print(format(97,'08b'))
