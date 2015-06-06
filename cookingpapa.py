__author__ = 'keigo'

import sys
import csv


def load_recipe_csv(csv_name):
    reader = csv.reader(open(csv_name, mode='r', encoding='utf-8'))
    header = next(reader)

    for row in reader:
        print(row)


if __name__ == '__main__':
    recipe_csv = sys.argv[1]
    load_recipe_csv(recipe_csv)
