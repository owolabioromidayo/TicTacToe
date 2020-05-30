import sys, copy
from math import inf as infinity
import random


def choice_to_index(state, choice):
    size = len(state)
    y = choice // size
    x = choice - y*size

    return y,x


def get_empty_cells(state):
    size = len(state)

    empty_cells = []
    for y in range(size):
        for x in range(size):
            if state[y][x] == ' ':
                empty_cells.append( (y*size) + x)

    return empty_cells


def check_win(state):
 
    d1, d2 = [],[]
    for idx,row in enumerate(state):
         #check rows
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return row[0] 
    
        col = [row[idx] for row in state]
        if col.count(col[0]) == len(col) and col[0] != ' ':
            return col[0]


        d1.append(state[idx][idx])
        d2.append(state[idx][len(state)-1-idx])

    if d1.count(d1[0]) == len(d1) and d1[0] != ' ':
        return d1[0]

    if d2.count(d2[0]) == len(d2) and d2[0] != ' ':
        return d2[0]



    #check draw
    if get_empty_cells(state) == []: return 'draw'

    
    return None


def play_move(state, idx, player):
    y,x = choice_to_index(state, idx)
    state[y][x] = player 




def minimax(state, player):
    #base case/ leaf case
    
    winner = check_win(state)
    if winner == 'O': return {'value': -1}
    if winner == 'X': return {'value': 1}
    if winner == 'draw': return {'value': 0}

    
    #recursive case
    children = get_empty_cells(state)

    best = {'index':None}

    if player is 'X': #maximizing player
        best['value'] =  -infinity
        
        for child in children:
            store = {}
            store['index'] = child
            
            new_state = copy.deepcopy(state)
            play_move(new_state, child, player)
            store['value'] = minimax(new_state, 'O')['value']
            

            if store['value'] > best['value']:
                best = store

        return best

    else: #O, minimizing
        best['value'] =  infinity
        
        for child in children:
            store = {}
            store['index'] = child
            
            new_state = copy.deepcopy(state)
            play_move(new_state, child, player)

            store['value'] = minimax(new_state, 'X')['value']
          

            if store['value'] < best['value']:
                best = store

        return best




def alphabeta(state, player, alpha, beta):
    #base case/ leaf case
    
    winner = check_win(state)
    if winner == 'O': return {'value': -1}
    if winner == 'X': return {'value': 1}
    if winner == 'draw': return {'value': 0}

    
    #recursive case
    children = get_empty_cells(state)

    best = {'index':None}

    if player is 'X': #maximizing player
        best['value'] =  -infinity
        
        for child in children:
            store = {}
            store['index'] = child
            
            new_state = copy.deepcopy(state)
            play_move(new_state, child, player)
            store['value'] = alphabeta(new_state, 'O', alpha, beta)['value']
            

            if store['value'] > best['value']:
                best = store

            alpha = max(alpha, best['value'])
            if alpha >= beta:
                break

        

    else: #O, minimizing
        best['value'] =  infinity
        
        for child in children:
            store = {}
            store['index'] = child
            
            new_state = copy.deepcopy(state)
            play_move(new_state, child, player)

            store['value'] = alphabeta(new_state, 'X', alpha, beta)['value']
          

            if store['value'] < best['value']:
                best = store

            beta = min(beta, best['value'])
            if beta <= alpha:
                break

    return best





        

 
   
