import chromadb
from chromadb.config import DEFAULT_TENANT, DEFAULT_DATABASE, Settings

client = chromadb.PersistentClient(
    path="C:\\Users\\arpik\\PycharmProjects\\finance_demo\\chroma_db_test\\test_db",
    settings=Settings(),
    tenant=DEFAULT_TENANT,
    database=DEFAULT_DATABASE,
)

collection = client.get_collection('investopedia-documents')

# results = collection.query(
#         query_texts=["is bitcoin volatile"],
#         n_results=1,
#         # where={"metadata_field": "is_equal_to_this"}, # optional filter
#         # where_document={"$contains":"search_string"}  # optional filter
#     )
#
# print(f"-- results --\n{results}")

def filter_documents_by_distance(data, threshold=1.0):
    """
    Filters and returns document texts where the distance score is less than the specified threshold.
    Adds checks to handle empty documents and ensures correct list access.

    :param data: dict containing ids, distances, metadatas, embeddings, and documents.
    :param threshold: float, the maximum distance score to include the document.
    :return: list of texts of documents that meet the distance criterion.
    """
    filtered_documents = []

    # Check if the keys exist and contain data
    if 'distances' in data and 'documents' in data:
        # Process each pair of distances and document lists
        for doc_distances, doc_texts in zip(data['distances'], data['documents']):
            # Check that both distances and documents are lists and have the same length
            if isinstance(doc_distances, list) and isinstance(doc_texts, list) and len(doc_distances) == len(doc_texts):
                # Iterate over distances and corresponding texts
                for distance, text in zip(doc_distances, doc_texts):
                    # Ensure text is a string and distance is a valid number
                    if isinstance(text, str) and isinstance(distance, float) and distance < threshold:
                        filtered_documents.append(text)
            else:
                print("Mismatch in lengths of distances and texts or invalid types.")
    else:
        print("Required keys ('distances', 'documents') not found in data.")

    return filtered_documents



def get_relevant_docs(question_string, n_results):
    qlist = question_string.split()
    results = collection.query(
            query_texts=qlist,
            n_results=n_results,
            # where={"metadata_field": "is_equal_to_this"}, # optional filter
            # where_document={"$contains":"search_string"}  # optional filter
        )
    if len(results) > 0:
        print(results)
        return filter_documents_by_distance(results)
    else:
        return ''

# # Example dictionary
# data = {
#     'ids': [['doc494', 'doc495']],
#     'distances': [[1.3373252153396606, 1.438823938369751]],
#     'metadatas': [[{'source': 'https://www.investopedia.com/terms/b/bitcoin.asp'}, {'source': 'https://www.investopedia.com/terms/b/bitcoin-cash.asp'}]],
#     'embeddings': None,
#     'documents': [['DOC1_TEXT', 'DOC2_TEXT']]
# }
#
# # Apply the function
# filtered_docs = filter_documents_by_distance(data)
#
# print(filtered_docs)  # This will print an empty list as all distances are above 1
