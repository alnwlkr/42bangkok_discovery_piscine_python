#!/usr/bin/env python3

def find_the_redheads(family_dict):
    redheads = list(filter(lambda name: family_dict[name] == 'red', family_dict))
    #filter used to iterate the iteratable var using first parameter function
    #lamda check if the hair is red then return True or False
    return redheads
    
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))