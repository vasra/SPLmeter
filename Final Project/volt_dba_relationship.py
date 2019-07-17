# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 18:11:41 2019

@author: proskos
"""

import re
from matplotlib import pyplot as plt


def read_values_from_file():
    file_path = "C:\\Users\\proskos\\Downloads"
    file_name = "values.txt"
    regexp = r"(\d+|\d+.\d+)\s+(\d+|\d+.\d+)"

    volt_lst = []
    volt_lst_append = volt_lst.append
    dba_lst = []
    dba_lst_append = dba_lst.append

    with open('\\'.join([file_path, file_name]), 'r') as input_file:
        for line in input_file:
            match = re.search(regexp, line)
            if match:
                volt_lst_append(float(match.group(1)))
                dba_lst_append(float(match.group(2)))

    # Plot of file value pairs.
    plt.plot(volt_lst, dba_lst)
    plt.title("Voltage-loudness plot")
    plt.xlabel("V")
    plt.ylabel("dbA")
    plt.show()


if __name__ == "__main__":
    read_values_from_file()
