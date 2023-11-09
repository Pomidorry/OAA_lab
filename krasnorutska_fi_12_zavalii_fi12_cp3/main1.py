from forming_dict_of_words import *
# Приклад використання
list_of_collections = list()
a="Це перший документ."
documents = [
    "Це перший документ.",
    "Це другий документ.",
    "А це третій документ.",
    "Це також перший документ."
]
collections = {'aoa': ['"Це перший документ."', '"Це другий документ."']}
inv_idx= build_inverted_index('aoa', documents)

# Виведемо результат
print(inv_idx)


