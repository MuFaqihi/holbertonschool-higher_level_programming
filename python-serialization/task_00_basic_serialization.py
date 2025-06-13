#!/usr/bin/python3
"""
Create a basic serialization module
that adds functionality to serialize a Python
dictionary to a JSON file and deserialize
the JSON file to recreate the Python dictionary.
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a dictionary into JSON format and saves it to a file.

    Args:
        data (dict): Dictionary to be serialized.
        filename (str): Name of the output file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file.

    Args:
        filename (str): Name of the input file.

    Returns:
        dict: Dictionary containing the deserialized data.
    """
    with open(filename, 'r') as file:
        return json.load(file)
