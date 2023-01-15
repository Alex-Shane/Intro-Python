#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:18:28 2023

@author: Alex
"""

#Alex Shane, ashane4
import pandas as pd
import math
import random

def calculate_ratings(past_matches):
    """Parameters
    past_matches: TYPE, string representing a file name
    
    Returns: a dictionary with player names as keys, and their ratings as values"""
    try:
        #create intial ratings dict
        ratings = dict.fromkeys(range(8), 1500)
        #open previous match data for reading
        df = pd.read_csv(past_matches, index_col=0)
        #go through every game in file and adjust ratings based on the elo
        #system
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
    #if past_matches is not a valid file, call exception
    except FileNotFoundError:
        print("File "+past_matches+" does not exist")
    #if there are any unexpected issues in reading data, call exception
    except:
        print("Unknown error while accessing data in " +past_matches)
    return (ratings)

def simulate_tournament(ratings):
    """Parameters
    ratings: TYPE, dictionary with player names as keys and their ratings as values
    
    Returns: the name of the player who wins this simulated tournament"""
    quarters = [[0,7], [1,6], [2,5], [3,4]]
    semis = []
    finals = []
    #simulate each match in the quarters, sending the winner onto the semis
    #note: same elo formulas used in probabilities in this function
    for match in quarters:
        player_A = match[0]
        player_B = match[1]
        rating_A = ratings[player_A]
        rating_B = ratings[player_B]
        prob_A_win = (pow(math.e, (rating_A-rating_B)/100))/(1+pow(math.e, (rating_A-rating_B)/100))
        num = random.random()
        if num < prob_A_win:
            semis.append(player_A)
        else:
            semis.append(player_B)
    #simulate each match in the semis, sending each winner onto the finals
    #note: same elo formulas used in probabilities in this function
    for player in range(0,4,2):
        player_A = semis[player]
        player_B = semis[player+1]
        rating_A = ratings[player_A]
        rating_B = ratings[player_B]
        prob_A_win = (pow(math.e, (rating_A-rating_B)/100))/(1+pow(math.e, (rating_A-rating_B)/100))
        num = random.random()
        if num < prob_A_win:
            finals.append(player_A)
        else:
            finals.append(player_B)
    #simulate finals with player_A and player_B
    player_A = finals[0]
    player_B = finals[1]
    rating_A = ratings[player_A]
    rating_B = ratings[player_B]
    prob_A_win = (pow(math.e, (rating_A-rating_B)/100))/(1+pow(math.e, (rating_A-rating_B)/100))
    num = random.random()
    #return the name of the player who wins the final
    if num < prob_A_win:
        return player_A
    return player_B

def project_win_probs(ratings_dict):
    """Parameters
    ratings_dict: dictionary with player names as keys and their ratings as values
    
    Returns: a dictionary with player names as keys and the probability of them winning
    the tournament based on 100 simulations of the tournament"""
    #create initial results dictionary where the probabilty that a player wins is zero
    results_dict = dict.fromkeys(range(8),0)
    #simulate the tournament 100 times, and each time a player wins, add .01 to
    #their probability since we simulate 100 times
    for x in range (0,100):
        winner = simulate_tournament(ratings_dict)
        results_dict[winner] += 0.01
    return (results_dict)

ratings_dict = calculate_ratings("past_matches.csv")
prob_dict = project_win_probs(ratings_dict)
    