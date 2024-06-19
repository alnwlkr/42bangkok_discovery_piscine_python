#!/usr/bin/env python3

print('Enter the first number:')
fnbr = int(input().strip())

print('Enter the second number:')
snbr = int(input().strip())

res = fnbr * snbr
print(fnbr, 'x', snbr, '=', res)

if res == 0:
	print('The result is positive and negative.')
elif res > 0:
	print('The result is positive.')
else:
	print('The result is negative.')

