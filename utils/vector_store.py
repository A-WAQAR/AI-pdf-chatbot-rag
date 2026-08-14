# import faiss
# import numpy as np


# def build_index(embeddings):
#     vectors = np.array(embeddings).astype("float32")
#     dimension = vectors.shape[1]
#     index = faiss.IndexFlatL2(dimension)
#     index.add(vectors)
#     return index




from langchain_community.vectorstores import FAISS
def build_vector_store(chunks, embedding_model): 
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    return vectorstore
