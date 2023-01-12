#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:40:28 2023

@author: Alex
"""

#Alex Shane, ashane4
import Frac
import random

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
    partial_nodes = []
    used_ids = [] 
    connect_file = open(connections, 'r', encoding='utf-8-sig')
    for line in connect_file:
        id_and_connect = line.split() 
        id = id_and_connect[0]
        connected = id_and_connect[1]
        if used_ids.count(id) == 0:
            partial_nodes.append([id,[connected]])
            used_ids.append(id)
        else:
            index = used_ids.index(id)
            partial_nodes[index][1].append(connected)
    price_file = open(prices, 'r', encoding='utf-8-sig')
    for line in price_file:
        price_info = line.split()
        min_price = Frac(price_info[1], price_info[2])
        frac_price = Frac (price_info[3], price_info[4])
        index = used_ids.index(price_info[0])
        partial_nodes[index].append(min_price)
        partial_nodes[index].append(frac_price)
    created_nodes = []
    for item in partial_nodes:
        node = Node (item[0], item[1], item[2], item[3], item[4])
        created_nodes.append(node)
    return (created_nodes)

def create_buyers (budgets, building_ids):
    buyers = []
    budget_file = open(budgets, 'r', encoding='utf-8-sig')
    for budget in budget_file:
        index = random.randint(0,4)
        new_buyer = Buyer (building_ids[index], Frac(budget,budget))
        buyers.append (new_buyer)
    return (buyers)

def run_simulation(connections, building_prices, budgets):
    buildings = create_graph(connections, building_prices)
    building_ids = [node[0] for node in buildings]
    buyers = create_buyers(budgets, building_ids)

    
    