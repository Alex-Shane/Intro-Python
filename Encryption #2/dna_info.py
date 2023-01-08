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
    """takes in a message and uses the binary representation of each letter
       to determine what dna base to add to the encoded sequence. Since each
       dna base is matched with 2 bit pairs, each binary representation of a letter
       corresponds to 4 dna bases added to the final encoded sequence""""
    encoded = ""
    #loop through every letter in message, turning it into a set of 4 dna bases
    for letter in message:
        #transform letter into binary representation
        letter_in_binary = format(ord(letter), '08b')
        #call helper function to create 4 dna bases from binary rep. add result
        #to overall encoded message
        encoded += binary_to_nucleotide (letter_in_binary)
    return(encoded)

def binary_to_nucleotide (num):
    """helper function for encode_sequence() which takes in the binary represenation
       of a letter and turns it into a string of 4 dna bases using dna_dict""""
    nucleotide = ""
    #go through string by pairs, and add corresponding dna base to result string
    for i in range (0, len(num), 2):
        pair = num[i:i+2]
        nucleotide += dna_dict[pair]
    return (nucleotide)

dna_dict_reversed_keys = {"A":"00", "T":"01", "C":"10", "G":"11"}
def decode_sequence (dna):
    """takes in a dna sequence and outputs what the english version of the sequence
       is. accomplishes this by going through the sequence 4 bases at a time and 
       determines what letter those 4 bases refer to.""""
    decoded = ""
    #go through dna sequence in groups of 4 bases, using helper function
    #to determine the letter those bases refer to. Add letter to decoded string
    for k in range (0,len(dna),4):
        bases = dna[k:k+4]
        decoded += nucleotides_to_letter (bases)
    return(decoded)

def nucleotides_to_letter (bases):
    """helper function for decode_sequence that takes in 4 dna bases and outputs
       what letter these bases correspond to by using dna_dict_reversed_keys.""""
    bin_string = ""
    #for each letter in string, add it's 2 bit pair to binary string
    for i in range (4):
        bin_string += dna_dict_reversed_keys [bases[i]]
    #turn binary string into character and return that value
    return (chr(int(bin_string, 2)))

def encrypt_decrypt (message, key = "CAT"):
    """takes in a message and optional key (default is "CAT") and for each letter
       in the key, uses the xor operator to encode the current encrypted message.
       after the last letter in key is used to encrypt the message, that message
       is output as the encrypted message.""""
    encrypted = message
    #use xor helper function to modify current encrypted word, output this value
    #once last letter in key has been used in xor helper function
    for letter in key:
        encrypted = xor_string (encrypted, letter)
    return(encrypted)

xor_dict = {"AA":"A", "AT":"T", "TA":"T","AC":"C", "CA":"C","AG":"G", "GA":"G",
            "TT":"A", "TC":"G", "CT":"G", "TG":"C", "GT":"C", "CC":"A", "CG":"T", 
            "GC":"T", "GG":"A"}
def xor_string (word, letter):
    """helper function for encrypt_decrypt() which takes in a word to be encrypted
       and the current letter from the key and outputs the string that results
       from the xor operator on every letter of word.""""
    result = ""
    #for each letter in word, add appropriate letter to xor string based off
    #dictionary values
    for k in range (0, len(word)):
        result += xor_dict [word[k]+letter]
    return (result)

def synthesizer (sequence):
    """simulates robot synthesizing an inputted dna sequence but with some imprecision.
       the robot is faulty in some of its synthesizing and as such generates the 
       wrong base some of the time in the helper function generate_base(). The
       actual dna sequence created by the robot is the output of the function""""
    synthesized = ""
    #for each letter in sequence, generate letter based on probability chart
    for letter in sequence:
        synthesized += generate_base(letter)
    return (synthesized)

def generate_base(letter):
    """helper function for synthesizer() that takes in a dna base and generates
       a base to be synthesized based on the probability chart provided in the 
       project description.""""
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

def error_count (word1, word2):
    """"takes in two strings and compares them character by character, outputting
        the number of letters that don't match each other."""
    mismatched = 0
    #loop through length of strings and if the letters aren't equal, add to the 
    #total mismatched count.
    for k in range (len(word1)):
        if word1[k] != word2[k]:
            mismatched += 1
    return mismatched

def redundancy (n, word):
    """creates a synthesized dna sequence n times and then finds the most
       frequent character at each position in the sequence and declares that
       to be the "correct" base and thus adds that to the final sequence which 
       gets outputted once every position in the sequence has been checked and 
       determined what letter should be there.""""
    fixed = ""
    synthesized_list = []
    #for n times, create a synthesized sequence and store it in a list
    for i in range (n):
        synthesized_list.append(synthesizer(word))
    #for the length of each sequence, find the most frequent character at the 
    #current position in the sequence and add that character to the final string
    for k in range (len(word)):
        counts = {"A":0, "T":0, "C":0, "G":0}
        for sequence in synthesized_list:
            #add letter in sequence to counts dictionary to update frequency
            counts[sequence[k]] += 1
        #find the max value of counts dictionary, which is a dna base, and add
        #that base to the final string
        fixed += max(counts, key = counts.get)
    return fixed

#create error file 
f = open("error_count.txt", "w")
#perform 5 tests with different n values to see how increasing n decreases
#the number of errors in the string outputted by redundancy()
for i in range (1,6):
    result = redundancy (i, "GGCAGCGCGAAGGTGGCGCCACGGCCCTTGAAGCCCGGCTCAGTCAGTTCGAGCGCAACGCCGCGGGCGGCGCGGGGCGGCGGTGGGCGCCCGACACTGGGCGGCGCCCAGCCCGGCAGCGGAG")
    error = error_count(result, "GGCAGCGCGAAGGTGGCGCCACGGCCCTTGAAGCCCGGCTCAGTCAGTTCGAGCGCAACGCCGCGGGCGGCGCGGGGCGGCGGTGGGCGCCCGACACTGGGCGGCGCCCAGCCCGGCAGCGGAG")
    f.write("Error for n = " + str(i) + " was " + str(error) + " letters" + "\n") 
f.close()
    
    
    