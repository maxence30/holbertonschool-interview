#!/usr/bin/python3
"""Fonction pour calculer le nombre minimum de pièces."""

def makeChange(coins, total):
    """Retourne le minimum de pièces pour atteindre total."""
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)
    nb_pieces = 0

    for coin in coins:
        nb_pieces += total // coin
        total %= coin
        
    if total != 0:
        return -1
    
    return nb_pieces
