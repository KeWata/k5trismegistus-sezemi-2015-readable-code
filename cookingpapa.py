__author__ = 'keigo'

import sys
import csv


def load_recipe_csv(csv_name):

    recipe_list = []
    reader = csv.reader(open(csv_name, mode='r', encoding='utf-8'))
    header = next(reader)

    for row in reader:
        recipe = {
            'recipe_id': row[0],
            'recipe_name': row[1],
        }
        recipe_list.append(recipe)

    return recipe_list


def print_recipe(recipe_list):
    for recipe in recipe_list:
        print(recipe['recipe_id'] + ': ' + recipe['recipe_name'])


if __name__ == '__main__':
    recipe_csv = sys.argv[1]
    recipe_list = load_recipe_csv(recipe_csv)
    print_recipe(recipe_list)