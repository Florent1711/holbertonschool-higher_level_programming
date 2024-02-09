#!/usr/bin/python3
"""
This module adds only integers and returns them
"""


def add_integer(a, b=98):
    """additionne deux nombres qui sont uniquement des entiers."""
    # Vérifie si a ou b est un entier ou un flottant
    if not isinstance(a, (int, float)):
        raise TypeError("a doit être un entier")
    if not isinstance(b, (int, float)):
        raise TypeError("b doit être un entier")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
