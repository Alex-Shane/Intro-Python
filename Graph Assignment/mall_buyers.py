#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:40:28 2023

@author: Alex
"""

#Alex Shane, ashane4
#import Frac
import random

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
            new_num1 = (int)(self.num)*(int)(other.den)
            new_num2 = (int)(other.num)*(int)(self.den)
            new_den = (int)(self.den)*(int)(other.den)
            new_frac = Frac(new_num1+new_num2, new_den)
        return (new_frac.simplify())
    
    
    def __sub__(self, other):
        if self.den == other.den:
            new_frac = Frac(self.num-other.num,self.den)
        else:
            new_num1 = (int)(self.num)*(int)(other.den)
            new_num2 = (int)(other.num)*(int)(self.den)
            new_den = (int)(self.den)*(int)(other.den)
            new_frac = Frac(new_num1-new_num2, new_den)
        return (new_frac.simplify())   

    def __mul__(self, other):
        new_frac = Frac (self.num*other.num, self.den*other.den)
        return (new_frac.simplify())
    
    def __truediv__(self, other):
        new_frac = Frac(self.num*other.den, self.den*other.num)
        return (new_frac.simplify())
    
    def __ge__(self, other):
        new_num1 = (int)(self.num)*(int)(other.den)
        new_num2 = (int)(other.num)*(int)(self.den)
        if new_num1 >= new_num2:
            return True
        return False
    
    def __str__(self):
        return (str(self.num) + "/" + str(self.den))

class Node:
    def __init__(self, id, connected_nodes, minimum_price, fractional_price):
        self.id = id
        self.connected_nodes = connected_nodes
        self.minimum_price = minimum_price
        self.fractional_price = fractional_price
        self.revenue = Frac (0,1)
        return
    
    def __str__(self):
        return ("ID = {id}, connected to = {connect}, min_price = {min}, frac_price = {frac}, revenue = {rev}").format(id = self.id, connect = self.connected_nodes, min = self.minimum_price, frac = self.fractional_price, rev = self.revenue)
    
class Buyer:
    def __init__(self, current_node_id, remaining_budget):
        self.current_node_id = current_node_id
        self.remaining_budget = remaining_budget
        
    def __str__(self):
        return ("current building ID: {id}, budget left = {budg}").format(id = self.current_node_id, budg = self.remaining_budget)

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
        node = Node (item[0], item[1], item[2], item[3])
        created_nodes.append(node)
    return (created_nodes)

def create_buyers (budgets, building_ids):
    buyers = []
    budget_file = open(budgets, 'r', encoding='utf-8-sig')
    buds = budget_file.read().split()
    for b in buds:
        buyers.append(Buyer(random.choice(building_ids), Frac(b,1)))
    return (buyers)

def run_simulation(connections, building_prices, budgets):
    buildings = create_graph(connections, building_prices)
    building_ids = [node.id for node in buildings]
    buyers = create_buyers(budgets, building_ids)
    for buyer in buyers:
        index = building_ids.index(buyer.current_node_id)
        build_price = buildings[index].minimum_price
        while buyer.remaining_budget >= build_price:
            buyer.remaining_budget = buyer.remaining_budget - build_price
            buildings[index].revenue = buildings[index].revenue + build_price
            next_node = random.choice (buildings[index].connected_nodes)
            buyer.current_node_id = next_node
            index = building_ids.index(buyer.current_node_id)
            build_price = buildings[index].minimum_price
        buyers.remove(buyer)
    total_revenue = Frac (0,1)
    for node in buildings:
        total_revenue = total_revenue - node.revenue
    revenue_dict = {}
    for id in building_ids:
        id_index = building_ids.index(id)
        revenue_dict[id] = total_revenue / buildings[id_index].revenue
    return ((total_revenue, revenue_dict))

res = run_simulation ("connections.txt", "pricing.txt", "budgets.txt")
print (res[0])
    
