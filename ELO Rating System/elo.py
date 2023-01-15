#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:18:28 2023

@author: Alex
"""

#Alex Shane, ashane4
import pandas as pd
import matplotlib.pyplot as plt
import math
import random
import csv
import operator

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

def display_ratings(ratings):
    """Parameters
    ratings: TYPE, dictionary with player names as keys and their ratings as values
    
    Returns: a bar graph of ratings for players in the tournament, also saves bar graph to pdf file"""
    #set font
    plt.rc('font', family='sans serif')
    fig = plt.figure(figsize=(6,5))
    #set x axis data
    players = [x for x in range(8)]
    #set y axis data
    ratings = [val for val in ratings.values()]
    #label y axis
    plt.ylabel('Rating', fontsize=20)
    #label x axis
    plt.xlabel ('Player', fontsize=20)
    #set bounds on y axis
    #change tick mark size
    plt.ylim(1200,1700)
    plt.xticks(fontsize=20)
    plt.yticks([i*100 + 1200 for i in range(6)], fontsize=20)
    #create bar graph
    plt.bar(players, ratings)
    plt.tight_layout()
    #save bar graph
    plt.savefig('projections.pdf')
    #display bar graph
    plt.show(fig)

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

def display_probs (probs):
    """Parameters: 
    probs: TYPE, dictionary with player names as keys and their probabilities of winning
    the tournament based on 100 simulations as the values
    
    Returns: No return value but creates 2 files: one csv file with the players
    listed by greatest to least chance of winning, and one pie chart of the player
    probabilities"""
    #create list of tuples where each tuple is a key:value pair and this list
    #is sorted by value in descending order
    sorted_dict = sorted(probs.items(), key=operator.itemgetter(1),reverse=True)
    #create list of sorted probabilities if the value is not zero
    sorted_probs = [pair[1] for pair in sorted_dict if pair[1] != 0]
    #create list of sorted keys if its associated value is not zero
    sorted_keys = [pair[0] for pair in sorted_dict if pair[1] != 0]
    #name csv file
    file_name = "probs.csv"
    #open csv file
    with open (file_name,'w') as csv_file:
        #create writer object
        csv_writer = csv.writer(csv_file)
        #write the fields of the file
        csv_writer.writerow(['player','probability of winning'])
        #for every player, write down their name and probability
        for pair in sorted_dict:
            row = [pair[0],pair[1]]
            csv_writer.writerow(row)
    #close file once done writiing
    csv_file.close()
    fig = plt.figure(figsize =(6, 5))
    #create pie chart
    plt.pie(sorted_probs, labels = sorted_keys)
    plt.tight_layout()
    #save piechart to working directory
    plt.savefig('projections_pie.pdf')
    #display chart in console
    plt.show(fig)
    return 
    
    