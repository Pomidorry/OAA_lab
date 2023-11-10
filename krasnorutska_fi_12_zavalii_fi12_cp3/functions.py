from colorama import Fore, Style
from forming_dict_of_words import *

mycollections = {}

def create(collection_name):
    if collection_name not in mycollections:
        mycollections[collection_name] = []
        print(Fore.GREEN + f'Collection {collection_name} has been created')
        print(Fore.GREEN + f'Number of collections: {len(mycollections)}')
        print(Style.RESET_ALL, end='')
    else:
        print(Fore.RED + 'Collection with that name already exists!')
        print(Style.RESET_ALL, end='')

def insert(collection_name, param):
    if collection_name in mycollections:
        table=mycollections.get(collection_name)
        table.append(param)
        print(Fore.GREEN + f'Document has been added to {collection_name} {mycollections}')
    else:
        print(Fore.YELLOW + f'Document {collection_name} not found')
    print(Style.RESET_ALL, end='')

def print_index(collection_name):
    if collection_name in mycollections:
        inverted_index = build_inverted_index(collection_name, mycollections[collection_name])
        print(f'Інвертований індекс для колекції "{collection_name}":')

        for word, doc_positions in inverted_index.items():
           print(f'"{word}":')
           for doc_id, positions in doc_positions:
              positions_str = ', '.join(map(str, positions))
              print(f'  d{doc_id} -> [{positions_str}]')
    else:
        print(f'Колекція "{collection_name}" не знайдена в інвертованому індексі')
    print(Style.RESET_ALL, end='')

def clear():
    print('\033c')