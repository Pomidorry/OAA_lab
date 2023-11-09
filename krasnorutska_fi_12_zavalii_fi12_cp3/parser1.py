import re
from colorama import Fore, Style
from forming_dict_of_words import *
mycollections = {}
commands = ['create', 'insert', 'print_index', 'search']

def read():
    read_command = []

    while True:
        try:
            line = ' '.join(re.split(r'\s+', input().strip()))
        except EOFError:
            return EOFError, None, None

        if ';' in line:
            read_command.append(line + ' ')
            break
        else:
            read_command.append(line) 

        if 'exit' in line:
            return 'exit', None, None
    
    pattern = r'(\w+)\s+(\w+)\s*([^;]*)'
    match = re.match(pattern, ''.join(read_command))

    try:
        command = match.group(1)  
        coll_name = match.group(2) 
        param = match.group(3).strip() if match.group(3) is not None else None
    except AttributeError: 
        return 'Invalid syntax', None, None  
    except Exception as e:
        return str(e), None, None

    return command.lower() if command.lower() in commands else f'Command "{command}" is not defined', coll_name, param
    
    
def create(collection_name):
    table=[]
    mycollections[collection_name]=table
    print(Fore.GREEN + f'Collection {collection_name} has been created')
    print(Style.RESET_ALL, end='')
    print(len(mycollections))

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

def search(collection_name, param):
    print(Fore.GREEN + f'Search function')
    print(Style.RESET_ALL, end='')

def invalid_syntax():
    print(Fore.RED + 'Invalid syntax')
    print(Style.RESET_ALL, end='')


if __name__ == "__main__":
    while True:
        command, coll_name, param = read()
        
        match command:
            case 'exit':
                break
            case 'create':
                if param == '':
                    create(coll_name)
                else:
                    invalid_syntax()
            case 'insert':
                if param != '':
                    insert(coll_name, param)
                else:
                    invalid_syntax()
            case 'print_index':
                if param == '':
                    print_index(coll_name)
                else:
                    invalid_syntax()
            case 'search':
                if param != '':
                    search(coll_name, param)
                else:
                    invalid_syntax()
            case _:
                print(Fore.RED + f'{command}')
                print(Style.RESET_ALL, end='')