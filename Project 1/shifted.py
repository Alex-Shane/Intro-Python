#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 07:30:02 2023

@author: Alex
"""
#Alex Shane, ashane4

decrypted_list = []
#receive the encrypted message from user
message = input("Enter the encrypted message: ")
#go through all 25 shift combos and add decrypted message to decrypted list
for i in range(1,26) :
    normal_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]
    #create list of shifted letters based on current shift factor
    shifted_alphabet = [chr((ord((normal_alphabet[x])) + i - 97) % 26 + 97) 
                        for x in range (26)]
    #create list of all decrypted letters
    decoded_letters = [normal_alphabet[shifted_alphabet.index(c)] if c.isalpha() 
                    else c for c in message]
    #create decrypted message by joining all letters
    decoded_message = "".join(decoded_letters)
    #add decrypted message to list of decrypted messages with differing shifts
    decrypted_list.append(decoded_message)

#open file for reading
text_file = open('pride_prejudice.txt', 'r', encoding='utf-8-sig')
text_string = ""
#go through file, adding each line to a string
for line in text_file : 
    text_string += line
#create list of frequencies for each letter in the text file
freq_list = [text_string.count(letter)/len(text_string) for letter 
             in normal_alphabet]
chi_list = []
n = len(message)
#for each decrypted message, calculate a chi value and add it to chi_list
for k in range (25) : 
    chi_val = 0
    for j in range (26) : 
        #calculate chi value associated with each letter and add to running sum
        chi_val += ((decrypted_list[k].count(normal_alphabet[j])-(freq_list[j]*n))
               **2)/(freq_list[j]*n)
    #add total chi value of decrypted message to chi_list
    chi_list.append(chi_val)
#get the index of the minimum chi value
min_index = chi_list.index(min(chi_list))
#print out message at min_index, since this is most sensible message
print ("The plaintext message is:", decrypted_list[min_index])
    



    