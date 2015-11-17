#!/usr/bin/env python
# coding:utf-8
import string
import itertools

__author__ = 'VDTConstructor'


def verify_function(candidate_password):
	"""verify the candidate_password whether it works"""
	if 
	return False, candidate_password
	return True, candidate_password


def verify_password(password_length_range, verify_function):
	# chars = string.printable[:10]
	# chars = string.printable[:-9]
	chars = string.printable[:62]
	print chars

	for i in xrange(password_length_range['min_length'], password_length_range['max_length'] + 1):
		for candidate_secret in itertools.product(chars, repeat=5):
			works_or_not = verify_function(''.join(candidate_secret))
			if works_or_not[0]:
				print works_or_not[1]
				return


if __name__ == '__main__':
	verify_password({'min_length': 1, 'max_length': 2}, verify_function)
