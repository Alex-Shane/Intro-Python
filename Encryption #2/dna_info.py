#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:32:35 2023

@author: Alex
"""

#Alex Shane, ashane4
import random

dna_dict = {"00":"A", "01":"T", "10":"C", "11":"G"}

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

dna_dict_reversed_keys = {"A":"00", "T":"01", "C":"10", "G":"11"}
def decode_sequence (dna):
    decoded = ""
    #go through dna sequence in groups of 4 bases, using helper function
    #to determine the letter those bases refer to. Add letter to decoded string
    for k in range (0,len(dna),4):
        bases = dna[k:k+4]
        decoded += nucleotides_to_letter (bases)
    print (decoded)

def nucleotides_to_letter (bases):
    bin_string = ""
    #for each letter in string, add it's 2 bit pair to binary string
    for i in range (4):
        bin_string += dna_dict_reversed_keys [bases[i]]
    #turn binary string into character and return that value
    return (chr(int(bin_string, 2)))

def encrypt_decrypt (encode, key = "CAT"):
    encrypted = encode
    #use xor helper function to modify current encrypted word, output this value
    #once last letter in key has been used in xor helper function
    for letter in key:
        encrypted = xor_string (encrypted, letter)
    print (encrypted)

xor_dict = {"AA":"A", "AT":"T", "TA":"T","AC":"C", "CA":"C","AG":"G", "GA":"G",
            "TT":"A", "TC":"G", "CT":"G", "TG":"C", "GT":"C", "CC":"A", "CG":"T", 
            "GC":"T", "GG":"A"}
def xor_string (word, letter):
    result = ""
    #for each letter in word, add appropriate letter to xor string based off
    #dictionary values
    for k in range (0, len(word)):
        result += xor_dict [word[k]+letter]
    return (result)

def synthesizer (sequence):
    synthesized = ""
    #for each letter in sequence, generate letter based on probability chart
    for letter in sequence:
        synthesized += generate_base(letter)
    print (synthesized)

def generate_base(letter):
    #if letter is A, automatically return "A"
    if letter == "A":
        return "A"
    #generate random number between 0 (inclusive) and 1 (exclusive)
    rand = random.random()
    #use probabilities from chart to determine what letter should be output based
    #on the value of the random number
    if letter == "T":
        if rand < 0.90:
            return "T"
        elif rand >= 0.90 and rand < 0.95:
            return "A"
        elif rand >= 0.95 and rand < 0.98:
            return "C"
        else:
            return "G"
    elif letter == "C":
        if rand < 0.97:
            return "C"
        elif rand == 0.97:
            return "A"
        elif rand == 0.98:
            return "T"
        else:
            return "G"
    else:
        if rand < 0.95:
            return "G"
        elif rand >= 0.95 and rand < 0.97:
            return "T"
        elif rand >= 0.97 and rand < 0.99:
            return "C"
        else:
            return "A"

    
    