#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:05:15 2023

@author: Alex
"""

#create list of alphabet in correct order
normal_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                   "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                   "w", "x", "y", "z"]
#create a list containing the alphabet in reverse
reverse_alphabet = normal_alphabet[:]
reverse_alphabet.reverse()
#take in encrypted message
message = input("Enter the encrypted message: ")
decoded_list = []
#loop through every character in message and apply decryption formula
for character in message :
    #check if character is a letter, if it is, decode it and add to decode list
    if character.isalpha() :
        index = reverse_alphabet.index(character)
        decoded_list.append(normal_alphabet[index])
    #if character isn't a letter, added character to decode list
    else :
        decoded_list.append(character);
#turn decode list into a string and print it back to user
decoded_message = "".join(decoded_list)
print("The plaintext message is:", decoded_message)
