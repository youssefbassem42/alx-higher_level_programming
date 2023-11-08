#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """multiply all elements by 2"""
    return {key: val * 2 for key, val in a_dictionary.items()}
