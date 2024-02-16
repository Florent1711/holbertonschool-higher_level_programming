#!/usr/bin/python3
"""
writes an Object to a text file, using a JSON representation
"""

import json

def save_to_json_file(my_obj, filename):
    # ouvre le fichier en mode écriture
    with open(filename, 'w') as f:
        # convertit l'objet en chaine JSON et l'écrit dans un fichier
        json.dump(my_obj, f)
