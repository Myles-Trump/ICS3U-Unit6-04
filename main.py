#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: June 2021
# This program uses a 2D array to store integers
#   from 1-50

import random


def sum_of_numbers(passed_in_2D_list, rows, columns):
    # this function finds the average of all the elements in the 2D array

    sum = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            sum += single_element
        total = sum / (rows * columns)

    return total


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    rows = int(input("How many row would you like: "))
    columns = int(input("How many columns would you like: "))

    for loop_counter_rows in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            a_random_number = random.randint(0, 10)
            temp_column.append(a_random_number)
            print("{0} ".format(a_random_number), end="")
        a_2d_list.append(temp_column)
        print("")

    sum = sum_of_numbers(a_2d_list, rows, columns)
    print("The average of all the numbers is: {0} ".format(sum))


if __name__ == "__main__":
    main()
