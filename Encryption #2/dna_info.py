#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:32:35 2023

@author: Alex
"""

#Alex Shane, ashane4

def encode_sequence (message):
    encoded = ""
    #loop through every letter in message, turning it into a set of 4 dna bases
    for letter in message:
        #transform letter into binary representation
        letter_in_binary = format(ord(letter), '08b')
        #call helper function to create 4 dna bases from binary rep. add result
        #to overall encoded message
        encoded += binary_to_nucleotide (letter_in_binary)
    print (encoded)

def binary_to_nucleotide (num):
    nucleotide = ""
    #go through string by pairs, checking what each binary pair should match 
    #with what dna base
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

