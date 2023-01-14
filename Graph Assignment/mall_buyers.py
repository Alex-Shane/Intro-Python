#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:40:28 2023

@author: Alex
"""

#Alex Shane, ashane4

import random
from frac import Frac 

class Node:
    """class represents a node with a unique id, connections to other nodes, 
    pricing information, and revenue tracking
    """
    def __init__(self, id, connected_nodes, minimum_price, fractional_price):
        """Parameters
        id: TYPE, string
        onnected_nodes: TYPE, list
        minimum_price: TYPE, Frac object
        fractional_price: TYPE, Frac object
        revenue: TYPE, Frac object
        
        Returns: an instance of a Node
        """
        self.id = id
        self.connected_nodes = connected_nodes
        self.minimum_price = minimum_price
        self.fractional_price = fractional_price
        #set initial revenue to a frac object equal to zero
        self.revenue = Frac (0,1)
        return
    
    def __str__(self):
        """takes no parameters
        
        Returns: a string representation of a node"""
        return ("ID = {id}, connected to = {connect}, min_price = {min}, frac_price = {frac}, revenue = {rev}").format(id = self.id, connect = self.connected_nodes, min = self.minimum_price, frac = self.fractional_price, rev = self.revenue)
    
class Buyer:
    """class represents a buyer who is in a specific store with a specific budget"""
    
    def __init__(self, current_node_id, remaining_budget):
        """Parameters
        current_node_id: TYPE, string
        remaining_budget: TYPE, Frac object
        
        Returns: an instance of a Buyer"""
        self.current_node_id = current_node_id
        self.remaining_budget = remaining_budget
        
    def __str__(self):
        """takes no parameters
        
        Returns: a string representation of a Buyer"""
        return ("current building ID: {id}, budget left = {budg}").format(id = self.current_node_id, budg = self.remaining_budget)

def create_graph(connections, prices):
    """Parameters
    connections: TYPE, string representing a file name
    prices: TYPE, string representing a file name
    
    Returns: a list of all nodes in the mall with all relevant info"""
    partial_nodes = []
    used_ids = [] 
    #open connections file for reading
    connect_file = open(connections, 'r', encoding='utf-8-sig')
    #go through connections file and add connections data to partial nodes list
    for line in connect_file:
        #put id and connecting node into a list for easy access
        id_and_connect = line.split() 
        id = id_and_connect[0]
        connected = id_and_connect[1]
        #if id is a new id, we need to add new node to partial nodes list
        if used_ids.count(id) == 0:
            partial_nodes.append([id,[connected]])
            #add new id to used_ids list
            used_ids.append(id)
        #if id is not unique, then add connecting node to connected_nodes list
        #at the node in partial nodes list that has the same id
        else:
            #find what index the id is at
            index = used_ids.index(id)
            #add connecting node data to list at that index
            partial_nodes[index][1].append(connected)
            
    #open price file for reading
    price_file = open(prices, 'r', encoding='utf-8-sig')
    #go through price file and add pricing info to partial nodes list
    for line in price_file:
        #seperate all 5 values into a list
        price_info = line.split()
        #set attribute values from price_info list
        min_price = Frac(price_info[1], price_info[2])
        frac_price = Frac (price_info[3], price_info[4])
        index = used_ids.index(price_info[0])
        #add price data to partial node at index
        partial_nodes[index].append(min_price)
        partial_nodes[index].append(frac_price)
    created_nodes = []
    #with all the data now stored, go through each node in partial node list
    #and create actual Node object to be stored in created_nodes list
    for item in partial_nodes:
        node = Node (item[0], item[1], item[2], item[3])
        created_nodes.append(node)
    return (created_nodes)

def create_buyers (budgets, building_ids):
    """Parameters
    budgets: TYPE, string represeting a file name
    building_ids: TYPE, list
    
    Returns: a list of all buyers in the mall with all relevant info"""
    buyers = []
    #open budget file for reading
    budget_file = open(budgets, 'r', encoding='utf-8-sig')
    #since we know this file is only one line, read entire file, and split it
    #so that all budgets are stored in list
    buds = budget_file.read().split()
    #go through budget list and make a new Buyer for each budget in the list
    for b in buds:
        buyers.append(Buyer(random.choice(building_ids), Frac(b,1)))
    return (buyers)

def run_simulation(connections, building_prices, budgets):
    """Parameters
    connections: TYPE, string representing a file name
    building_prices: TYPE, string representing a file name
    budgets: TYPE, string representing a file name
    
    Returns: tuple containing Frac object representing total revenue and dictionary
    containing unique ids of buildings in the mall and their fractional share of 
    mall revenue"""
    #get a list of all buildings in the mall
    buildings = create_graph(connections, building_prices)
    #get list of all unique ids in the mall
    building_ids = [node.id for node in buildings]
    #get list of every buyer in the mall
    buyers = create_buyers(budgets, building_ids)
    #for each buyer in the mall, simulate their spending at random buildings
    #until they run out of money
    for buyer in buyers:
        index = building_ids.index(buyer.current_node_id)
        min_price = buildings[index].minimum_price
        acc_price = buildings[index].fractional_price
        #if the buyer hasn't run out of money for a specific building, make purchase and move
        #on to a new building
        while buyer.remaining_budget >= min_price:
            spent = buyer.remaining_budget*acc_price
            #update budget after purchase
            buyer.remaining_budget = buyer.remaining_budget - spent
            #update revenue after purchase
            buildings[index].revenue = buildings[index].revenue + spent
            #get id of next building for buyer to shop at
            next_node = random.choice (buildings[index].connected_nodes)
            buyer.current_node_id = next_node
            #find index of building to shop at
            index = building_ids.index(buyer.current_node_id)
            #find the minimum price at the next store
            min_price = buildings[index].minimum_price
            #find the fractional price at the next store
            acc_price = buildings[index].fractional_price
    total_revenue = Frac (0,1)
    #go through every building and tally up revenue
    for node in buildings:
        total_revenue = total_revenue + node.revenue
    revenue_dict = {}
    #go through every indiviual building and calculate its share of revenue
    #and store it in a dictionary
    for id in building_ids:
        id_index = building_ids.index(id)
        revenue_dict[id] = buildings[id_index].revenue / total_revenue 
    return total_revenue, revenue_dict



    
