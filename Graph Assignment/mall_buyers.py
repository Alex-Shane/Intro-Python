#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:40:28 2023

@author: Alex
"""

#Alex Shane
import Frac

class Node:
    def __init__(self, id, connected_nodes, minimum_price, fractional_price):
        self.id = id
        self.connected_nodes = connected_nodes
        self.minimum_price = minimum_price
        self.fractional_price = fractional_price
        self.revenue = 0
        return
    
class Buyer:
    def __init__(self, current_node_id, remaining_budget):
        self.current_node_id = current_node_id
        self.remaining_budget = remaining_budget

def create_graph(connections, prices):
    building_graph = []
    file = open(connections, 'r', encoding='utf-8-sig')
    for line in file:
        building_found = False
        cur_building_ = ""
        connected_to = ""
        for letter in line:
            if letter.isalpha():
                if building_found == False:
                    building_found = True
                    cur_building = letter
                else:
                    connected_to = letter
                    break
        building_graph.append (Node(id(cur_building), ))

def run_simulation(connections, building_prices, budgets):
    buildings = create_graph(connections, building_prices)
    buyers = create_buyers(budgets)

    
    