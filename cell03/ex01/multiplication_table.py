#!/usr/bin/env python3

def is_int(val):
	try:
		int(val)
		return True
	except ValueError:
		return False

print('Enter a number')
nb = input().strip()

if is_int(nb):
	nb = int(nb)
	i = 0
	while i <= 9:
		res = nb * i
		print(i, 'x', nb, '=', res)
		i = i + 1
