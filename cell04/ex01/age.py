#!/usr/bin/env python3

def is_int(val):
	try:
		int(val)
		return True
	except ValueError:
		return False

age = input('Please tell me your age: ').strip()

if is_int(age):
	age = int(age)
	print('You are currently', age, 'years old.')
	print("In 10 years, you'll be",age+10,'years old.')
	print("In 20 years, you'll be",age+20,'years old.')
	print("In 30 years, you'll be",age+30,'years old.')
