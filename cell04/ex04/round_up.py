#!/usr/bin/env python3

def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False
    
nb = input('Give me a number: ')

if is_float(nb):
    nb = float(nb)
    nb_i = int(nb)
    if nb == nb_i:
        print(nb_i)
    elif nb_i >= 0:
        print(nb_i + 1)
    else:
        print(nb_i)