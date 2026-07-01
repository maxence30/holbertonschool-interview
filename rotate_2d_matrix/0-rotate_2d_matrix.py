#!/usr/bin/python3
"""
Module contenant la fonction rotate_2d_matrix.
"""


def rotate_2d_matrix(matrix):
    """
    Fait pivoter une matrice nxn de 90 degrés
    dans le sens des aiguilles d'une montre.

    La rotation est effectuée directement sur
    la matrice sans en créer une nouvelle.

    Args:
        matrix (list): matrice carrée à modifier.
    """
    matrix.reverse()

    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]