#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:15:28 2023

@author: Alex
"""

#Alex Shane, ashane4

class Frac:
    """class represents a fraction with two attributes, a numerator and denominator"""
    
    def __init__(self, num, den):
        """Parameters
        ----------
        num : TYPE, int
        den: TYPE, int

        Returns
        -------
        Creates an instance of Frac
        """
        self.num = num
        self.den = den
        return
    
    def find_greatest_common_divisor(self, num, den): 
        """Parameters
        num: TYPE, int
        den: TYPE, int
        
        Returns: int representing the greatest common divisor between the two inputs"""
        #python integration of Euclidian algorithm to find greatest common
        #divisor
        while den:
            num, den = den, num % den
        return (num)
    
    def simplify (self):
        """Takes in no parameters
           Returns: a Frac object that cannot be further simplified"""
        #use divisor helper function to obtain gcd
        divisor = self.find_greatest_common_divisor(self.num, self.den)
        #divide both numerator and denominator by gcd, and return a Frac object
        #of the simplified denom and numerators
        return (Frac((int)(self.num/divisor), (int)(self.den/divisor)))
    
    def __add__(self, other):
        """Parameters
        other: TYPE, Frac object
        
        Returns: simplified Frac object that is the addition of self and other"""
        #if common denoms, then simply add the numerators
        if self.den == other.den:
            new_frac = Frac(self.num+other.num,self.den)
        #if not common denom, then create common denom through multiplication,
        #then add the adjusted numerators
        else:
            new_num1 = (int)(self.num)*(int)(other.den)
            new_num2 = (int)(other.num)*(int)(self.den)
            new_den = (int)(self.den)*(int)(other.den)
            new_frac = Frac(new_num1+new_num2, new_den)
        return (new_frac.simplify())
    
    
    def __sub__(self, other):
        """Parameters
        other: TYPE, Frac object
        
        Returns: simplified Frac object that is the subtraction of self and other"""
        #if common denoms, then simply subtract the numerators
        if self.den == other.den:
            new_frac = Frac(self.num-other.num,self.den)
        #if not common denom, then create common denom through multiplication,
        #then subtract the adjusted numerators
        else:
            new_num1 = (int)(self.num)*(int)(other.den)
            new_num2 = (int)(other.num)*(int)(self.den)
            new_den = (int)(self.den)*(int)(other.den)
            new_frac = Frac(new_num1-new_num2, new_den)
        return (new_frac.simplify())   

    def __mul__(self, other):
        """Parameters
        other: TYPE, Frac object
        
        Returns: simplified Frac object that is the multiplication of self and other"""
        #create new fraction by multiplying both numerators together and denominators together
        new_frac = Frac ((int)(self.num)*(int)(other.num), (int)(self.den)*(int)(other.den))
        return (new_frac.simplify())
    
    def __truediv__(self, other):
        """Parameters
        other: TYPE, Frac object
        
        Returns: simplified Frac object that is the division of self and other"""
        #create new fraction by multiplying self by the reciprocal of other
        new_frac = Frac ((int)(self.num)*(int)(other.den), (int)(self.den)*(int)(other.num))
        return (new_frac.simplify())
    
    def __ge__(self, other):
        """Parameters
        other: TYPE, Frac object
        
        Returns: True if self is greater than or equal to other, False otherwise"""
        #adjust numerators by multiplying by the other fractions denominator so 
        #that we have two fractions with common denominators to allow for comparison
        new_num1 = (int)(self.num)*(int)(other.den)
        new_num2 = (int)(other.num)*(int)(self.den)
        #since we now have common denom, if selfs numerator is greater than or equal
        #to others numerator, then the fractions follow
        if new_num1 >= new_num2:
            return True
        return False
    
    def __str__(self):
        """takes no parameters
        
        Returns: string representation of a Frac object"""
        return (str(self.num) + "/" + str(self.den))
    
    

    

    
    
    