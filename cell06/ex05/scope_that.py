#!/usr/bin/env python3

def add_one(n):
    return n + 1

def is_float(val):
	try:
		float(val)
		return True
	except ValueError:
		return False

n = 41
print(f'Number before add_one: {n}')
n = add_one(n)
print(f'Number after add_one: {n}')