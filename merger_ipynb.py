#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib

# Main program
def main():
    # Config: input python_ex???.py dir.
    target_dir = './self_taught/'
    
    cells = []
    for n in range(313):
        cells.append(import_file(target_dir + 'python_ex' + str(n) + '.py', n))

    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.6.8"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }
    
    with open("book.ipynb", "w", encoding="utf-8") as fp:
        json.dump(nb, fp)

import json
# Read a file and output HTML content part
def import_file(filename, n):
    # Read from file
    with open(filename, "r", encoding="utf-8") as fp:
        lines = fp.readlines()
    # Output file contetns
    cell = {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": lines }
    return cell


if __name__ == '__main__':
    main()
