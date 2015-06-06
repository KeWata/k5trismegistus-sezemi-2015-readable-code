# -*- coding: utf-8 -*-
__author__ = 'keigo'

import sys
import csv


def load_recipe_data_from_a_file(csv_name):
    
    recipe_list = []
    reader = csv.reader(open(csv_name, mode='r'))
    header = next(reader)

    for idx, row in enumerate(reader):
        recipe = {
            'recipe_id': str(idx),
            'recipe_name': row[0],
            'recipe_URL' : row[1]
        }
        recipe_list.append(recipe)

    return recipe_list

def load_recipe_data_from_files(num_files = 3):
    base_file_name = 'recipe_utf'
    extension = '.csv'
    recipe_data = list()
    for i in range(num_files):
        data_file_name = base_file_name + str(i) + extension
        recipe_data.append(load_recipe_data_from_a_file(data_file_name))
    return recipe_data

def print_recipe_all(recipe_list):
    for recipe in recipe_list:
        print(recipe['recipe_id'] + ': ' + recipe['recipe_name'] + ': '+ recipe['recipe_URL'])


def print_recipe_by_id(recipe_list, wanted_id):
    for recipe in recipe_list:
        if wanted_id == recipe['recipe_id']:
            print(recipe['recipe_id'] + ': ' + recipe['recipe_name']+ ': '+recipe['recipe_URL'])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        wanted_recipe_id = sys.argv[1]
    else:
        wanted_recipe_id = None

    recipe_list = load_recipe_data_from_files()
    if wanted_recipe_id:
        print_recipe_by_id(recipe_list, wanted_recipe_id)
    else:
        print_recipe_all(recipe_list)


