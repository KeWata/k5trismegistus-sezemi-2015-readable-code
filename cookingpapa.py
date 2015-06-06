__author__ = 'keigo'

import sys
import csv


def load_recipe_data(csv_name):

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


def print_recipe_all(recipe_list):
    for recipe in recipe_list:
        print(recipe['recipe_id'] + ': ' + recipe['recipe_name'])


def print_recipe_by_id(recipe_list, wanted_id):
    for recipe in recipe_list:
        if wanted_id == recipe['recipe_id']:
            print(recipe['recipe_id'] + ': ' + recipe['recipe_name'])


if __name__ == '__main__':
    recipe_csv = sys.argv[1]
    if len(sys.argv) == 3:
        wanted_recipe_id = sys.argv[2]
    else:
        wanted_recipe_id = None

    recipe_list = load_recipe_data(recipe_csv)

    if wanted_recipe_id:
        print_recipe_by_id(recipe_list, wanted_recipe_id)
    else:
        print_recipe_all(recipe_list)