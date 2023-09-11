def preprocess_text(text): #Function for basice text processing.
    import string
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def build_inverted_index(documents):
    inverted_index = {}
    for doc_id, doc in enumerate(documents):
        doc = preprocess_text(doc)
        terms = doc.split()
        for term in terms:
            if term not in inverted_index:
                inverted_index[term] = []
            if doc_id not in inverted_index[term]:
                inverted_index[term].append(doc_id)
    return inverted_index

def search_inverted_index(inverted_index, query):
    query = preprocess_text(query)
    terms = query.split()
    result = set()
    for term in terms:
        if term in inverted_index:
            result.update(inverted_index[term])
    return result

# Sample collection of documents
documents = [
    "The quick brown fox jumps over the lazy dog.",
    "The lazy dog slept in the sun.",
    "The quick brown fox is a clever animal."
]

# Building the inverted index
inverted_index = build_inverted_index(documents)

# Search using the inverted index
query = "lazy dog"
search_results = search_inverted_index(inverted_index, query)

# Displaying the search results
print("Search Results for Query:", query)
for doc_id in search_results:
    print("Document ID:", doc_id, "->", documents[doc_id])
