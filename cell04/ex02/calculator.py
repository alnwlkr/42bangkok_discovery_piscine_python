#!/usr/bin/env python3

def is_int(val):
	try:
		int(val)
		return True
	except ValueError:
		return False

nb1 = input('Give me the first number: ').strip()
nb2 = input('Give me the second number: ').strip()
print('Thank you!')
if is_int(nb1) and is_int(nb2):
	nb1 = int(nb1)
	nb2 = int(nb2)
	print(nb1, '+', nb2, '=', nb1+nb2)
	print(nb1, '-', nb2, '=', nb1-nb2)

	if nb2 == 0:
		print('Cannot devide by zero!')
	else:
		print(nb1, '/', nb2, '=', int(nb1/nb2))

	print(nb1, '*', nb2, '=', nb1*nb2)
