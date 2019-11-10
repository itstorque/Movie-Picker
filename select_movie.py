#!/usr/bin/env python3

import sys
import random

def random_n_list(movie_list, count=1):

	if count < 1: return movies

	return random.sample(movie_list, count)

def create_list(content, seperator="\n"):

	return content.split(seperator)

if __name__ == "__main__":

	file = open(sys.argv[1], 'r')

	how_many = int(sys.argv[2])

	file_content = file.read()

	movie_list = create_list(file_content)

	print(random_n_list(movie_list, how_many))
