#!/usr/bin/env python3

import sys

def is_int(val):
	if is_float(val):
		val_f = float(val)
		if val_f == int(val):
			return True
	return False
	
def is_float(val):
	try:
		float(val)
		return True
	except ValueError:
		return False

argc = len(sys.argv)
# print(sys.argv)

if argc == 3:
	l = sys.argv[1]
	r = sys.argv[2]
	if is_int(l) and is_int(r):
		l = int(l)
		r = int(r)
		if l > r:
			l,r = r,l
		res = [*range(l, r+1)]
		print(res)
else:
    print("none")