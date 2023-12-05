#!/usr/bin/python3
""" Save Json file """
import json


def save_to_json_file(my_obj, filename):
    """ Save Json file """
    with open(filename, "w") as j:
        json.dump(my_obj, j)
