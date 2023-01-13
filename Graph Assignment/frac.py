#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:15:28 2023

@author: Alex
"""

#Alex Shane, ashane4

class Frac:
    
    def __init__(self, num, den):
        self.num = num
        self.den = den
        return
    
    def find_greatest_common_divisor(self, num, den):
        while den:
            num, den = den, num % den
        return (num)
    
    def simplify (self):
        divisor = self.find_greatest_common_divisor(self.num, self.den)
        return (Frac((int)(self.num/divisor), (int)(self.den/divisor)))
    
    def __add__(self, other):
        if self.den == other.den:
            new_frac = Frac(self.num+other.num,self.den)
        else:
            new_num1 = self.num*other.den
            new_num2 = other.num*self.den
            new_den = self.den*other.den
            new_frac = Frac(new_num1+new_num2, new_den)
        return (new_frac.simplify())
    
    
    def __sub__(self, other):
        if self.den == other.den:
            new_frac = Frac(self.num-other.num,self.den)
        else:
            new_num1 = self.num*other.den
            new_num2 = other.num*self.den
            new_den = self.den*other.den
            new_frac = Frac(new_num1-new_num2, new_den)
        return (new_frac.simplify())   

    def __mul__(self, other):
        new_frac = Frac (self.num*other.num, self.den*other.den)
        return (new_frac.simplify())
    
    def __truediv__(self, other):
        new_frac = Frac(self.num*other.den, self.den*other.num)
        return (new_frac.simplify())
    
    def __ge__(self, other):
        new_num1 = self.num*other.den
        new_num2 = other.num*self.den
        if new_num1 >= new_num2:
            return True
        return False
    
    def __str__(self):
        return (str(self.num) + "/" + str(self.den))
    

    
    
    

    

    
    
    