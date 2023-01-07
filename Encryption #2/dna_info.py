#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:32:35 2023

@author: Alex
"""

#Alex Shane, ashane4

dna_dict = {"00":"A", "01":"T", "10":"C", "11":"G"}
dna_dict_reversed_keys = {"A":"00", "T":"01", "C":"10", "G":"11"}

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
    #go through string by pairs, and add corresponding dna base to result string
    for i in range (0, len(num), 2):
        pair = num[i:i+2]
        nucleotide += dna_dict[pair]
    return (nucleotide)

def decode_sequence (dna):
    decoded = ""
    for k in range (0,len(dna),4):
        bases = dna[k:k+4]
        decoded += nucleotides_to_letter (bases)
    print (decoded)

def nucleotides_to_letter (bases):
    bin_string = ""
    for i in range (4):
        bin_string += dna_dict_reversed_keys [bases[i]]
    return (chr(int(bin_string, 2)))


