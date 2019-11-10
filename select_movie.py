#!/usr/bin/env python3

import sys
import random

DEFAULT_FILE = "./deep_list.txt"

class TooManyArguments:
	def __init__(self):
		Exception.__init__(self)

def random_n_list(movie_list, count=1):

	if count < 1: return movies

	return random.sample(movie_list, count)

def create_list(content, seperator="\n"):

	universe = [i for i in content.split(seperator) if i.replace(" ", "") != ""]

	return universe

if __name__ == "__main__":

	if len(sys.argv) == 3:

		if sys.argv[2].isdigit():

			file_path = sys.argv[1]

			how_many = int(sys.argv[2])

		elif sys.argv[1].isdigit():

			file_path = sys.argv[2]

			how_many = int(sys.argv[1])

		else:

			raise TooManyArguments

	elif len(sys.argv) == 2:

		arg_val = sys.argv[1]

		if arg_val.isdigit():

			file_path = DEFAULT_FILE

			how_many = int(arg_val)

		else:

			file_path = arg_val

			how_many = 1

	elif len(sys.argv) == 1:

		file_path = DEFAULT_FILE

		how_many = 1

	else:

		raise TooManyArguments

	file_content = open(file_path, 'r').read()

	movie_list = create_list(file_content)

	print(random_n_list(movie_list, how_many))
