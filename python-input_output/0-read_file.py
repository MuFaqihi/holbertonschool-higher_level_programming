#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file and prints its content.

    Args:
        filename (str): The name of the file to be read.

    Notes:
    - Uses 'with' to ensure the file is closed properly.
    - Assumes the file exists and is readable.
    """

    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end='')
