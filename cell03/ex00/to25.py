#!/usr/bin/env python3

def is_int(val):
	try:
		int(val)
		return True
	except ValueError:
		return False

print('Enter a number less than 25')
nb = input().strip()

if is_int(nb):
	nb = int(nb)
	if nb <= 25:
		while nb <= 25:
			print('Inside the loop, my variable is', nb)
			nb = nb + 1
	else:
		print('Error')
