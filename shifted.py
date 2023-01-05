#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 07:30:02 2023

@author: Alex
"""

encrypted_list = []
message = input("Enter the decrypted message: ")
for i in range(1,26) :
    normal_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]
    shifted_alphabet = [normal_alphabet[x-i] if x-i >= 0 else normal_alphabet
                        [x+26-i] for x in range (26)]
    decoded_list = [normal_alphabet[shifted_alphabet.index(c)] if c.isalpha() 
                    else c for c in message]
    decoded_message = "".join(decoded_list)
    encrypted_list.append(decoded_message)

text_file = open('pride_prejudice.txt', 'r', encoding='utf-8-sig')
text_string = ""
for line in text_file : 
    text_string += line
freq_list = [text_string.count(letter)/len(text_string) for letter 
             in normal_alphabet]

chi_list = []
n = len(message)
for k in range (25) : 
    chi_val = 0
    for j in range (26) : 
        chi_val += ((encrypted_list[k].count(normal_alphabet[j])-(freq_list[j]*n))
               **2)/(freq_list[j]*n)
    chi_list.append(chi_val)
min_index = chi_list.index(min(chi_list))
print ("The plaintext message is:", encrypted_list[min_index])
    



    