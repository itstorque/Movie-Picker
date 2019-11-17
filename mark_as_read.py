#!/usr/bin/env python3

import sys
from constants import *

def get_confirmation(movie_name):

    confirmation_message = lambda name: "Mark '" + name + "' as watched? [y/n] > "

    x = input(confirmation_message(movie_name))

    while not x in {"y", "n", "Y", "N", "yes", "no", "Yes", "No"}:

        x = input(confirmation_message(movie_name))

    return "y" in x.lower()

if __name__ == "__main__":

    file_path = DEFAULT_FILE

    movies_to_replace = sys.argv[1:]

    if "-f" in movies_to_replace:

        file_index = movies_to_replace.index("-f") + 1

        file_path = movies_to_replace[file_index]

        movies_to_replace.pop(file_index)

        movies_to_replace.pop(file_index-1)

    file = open(file_path, "r")

    data = file.read().split("\n")

    for line_number, line in enumerate(data):

        if any(list(map(lambda x: x.lower().replace("_", " ") in line.lower(), movies_to_replace))):

            if get_confirmation(line):

                data[line_number] = "* " + line

    file.close()

    file = open(file_path, "w")
    file.write('\n'.join(data))
    file.close()
