#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:18:28 2023

@author: Alex
"""

#Alex Shane, ashane4
import pandas as pd
import math

def calculate_ratings(past_matches):
    try:
        ratings = dict.fromkeys(range(8), 1500)
        df = pd.read_csv(past_matches, index_col=0)
        for index, row in df.iterrows():
            player_A = row['player_A']
            player_B = row['player_B']
            rating_A = ratings[player_A]
            rating_B = ratings[player_B]
            prob_A_win = (pow(math.e, (rating_A-rating_B)/100))/(1+pow(math.e, (rating_A-rating_B)/100))
            prob_B_win = 1 - prob_A_win
            if row['winner'] == player_A:
                ratings[player_A] += 5*(1-prob_A_win)
                ratings[player_B] -= 5*prob_B_win
            else:
                ratings[player_A] -= 5*prob_A_win
                ratings[player_B] += 5*(1-prob_B_win)
    except FileNotFoundError:
        print("File "+past_matches+" does not exist")
    except:
        print("Unknown error while accessing data in " +past_matches)
    return (ratings)

ratings_dict = calculate_ratings("past_matches.csv")
    