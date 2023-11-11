from colorama import Fore, Style

mycollections = {}
inverted_indexes = {}

def build_inverted_index(collection_name, documents):
    inverted_index = {} if collection_name not in inverted_indexes else inverted_indexes[collection_name]
    unique_words = sorted(list(set(documents.split())))
    
    doc_index = mycollections[collection_name].index(documents)

    for word in unique_words:
        if word in inverted_index:
            inverted_index[word].append((doc_index+1, [index+1 for index, value in enumerate(documents.split()) if value == word]))
        else:
            inverted_index[word] = [(doc_index+1, [index+1 for index, value in enumerate(documents.split()) if value == word])]
        
    inverted_indexes[collection_name] = inverted_index

def create(collection_name):
    if collection_name not in mycollections:
        mycollections[collection_name] = []
        print(Fore.GREEN + f'Collection "{collection_name}" has been created')
        print(Fore.GREEN + f'Number of collections: {len(mycollections)}')
    else:
        print(Fore.YELLOW + 'A collection with the same name already exists.')
    print(Style.RESET_ALL, end='')

def insert(collection_name, param):
    if collection_name in mycollections:
        table = mycollections.get(collection_name)
        table.append(param)
        build_inverted_index(collection_name, param)
        print(Fore.GREEN + f'Document has been added to "{collection_name}" collection.')
    else:
        print(Fore.YELLOW + f'Collection "{collection_name}" not found.')
    print(Style.RESET_ALL, end='')

def print_index(collection_name):
    if collection_name in mycollections:
        print(Fore.GREEN + f'Inverted Index for collection "{collection_name}":')
        print()
        for word, indexes in inverted_indexes[collection_name].items():
                print(f'"{word}":')
                for elem in indexes:
                    print(f'd{elem[0]} -> {elem[1]}')
        print()
    else:
        print(Fore.YELLOW + f'Collection "{collection_name}" not found.')
    print(Style.RESET_ALL, end='')

def search_lite(collection_name, param):
    print('List of available documents:', *mycollections[collection_name])
    print(Style.RESET_ALL, end='')

def search(collection_name, param):
    print(param)
    print(Style.RESET_ALL, end='')

def show():
    for keys, items in mycollections.items():
        print(f'Collection "{keys}":')
        for i, d in enumerate(items):
            print(f'doc{i}: "{d}"')