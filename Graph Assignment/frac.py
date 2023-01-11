#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:15:28 2023

@author: Alex
"""

#Alex Shane, ashane4

class Frac:
    
    def _init_(self, num, den):
        self.num = num
        self.den = den
        return
    
    def find_greatest_common_divisor(self):
        while self.den:
            self.num, self.den = self.den, self.num % self.den
        return (self.num)
    
    def simplify (self):
        divisor = self.find_greatest_common_divisor()
        return (Frac(self.num/divisor, self.den/divisor))
    
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

    def _mul_(self, other):
        return (self.simplify(Frac(self.num*other.num, other.den*self.den)))
    
    def _div_(self, other):
        return (self.simplify(Frac(self.num*other.den, self.den*other.num)))

    

    
    
    