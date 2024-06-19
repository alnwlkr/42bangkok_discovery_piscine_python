#!/usr/bin/env python3

def is_int(val):
	try:
		int(val)
		return True
	except ValueError:
		return False

nb = input().strip()

if is_int(nb):
	nb = int(nb)
	if nb == 0:
		print("This number is both positive and negative.")
	elif nb < 0:
		print("This number is negative.")
	else:
		print("This number is positive.")