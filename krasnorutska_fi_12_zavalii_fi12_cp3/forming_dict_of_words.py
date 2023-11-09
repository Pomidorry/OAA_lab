from collections import defaultdict

def build_inverted_index(collection_name, documents):
    inverted_indexes = {}
    inverted_index = inverted_indexes.get(collection_name, defaultdict(list))

    for doc_id, doc_text in enumerate(documents):
        words = doc_text.split()
        for word in words:
            inverted_index[word].append((doc_id, [i for i, w in enumerate(words) if w == word]))

    inverted_indexes[collection_name] = inverted_index
    return dict(inverted_index)
