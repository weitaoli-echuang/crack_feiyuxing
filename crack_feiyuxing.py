#!/usr/bin/env python
# coding:utf-8
# By eathings
import sys
import string
import itertools

__author__ = 'VDTConstructor'


def get_strings(secret_min=1, secret_max=2):
	# chars = string.printable[:10]
	# chars = string.printable[:-9]
	chars = string.printable[:62]
	print chars
	strings = []
	for x in itertools.product(chars, repeat=5):
		''.join(x)

	for i in xrange(secret_min, secret_max + 1):
		strings.append((itertools.product(chars, repeat=i),))
	return itertools.chain(*strings)


def make_dict():
	f = open(file, 'a')
	for x in list_str:
		for y in x:
			f.write("".join(y))
			f.write('\n')
	f.close()
	print 'Done'


def write_dict_for_crack():
	global min, max, list_str, file
	while True:
		if len(sys.argv) == 4:
			try:
				min = int(sys.argv[1])
				max = int(sys.argv[2])
			except:
				print "wrong"
				sys.exit(0)
		if min <= max:
			list_str = get_strings()
			file = sys.argv[3]
			make_dict()
			sys.exit(0)


if __name__ == '__main__':
	# write_dict_for_crack()
	get_strings(1, 2)

