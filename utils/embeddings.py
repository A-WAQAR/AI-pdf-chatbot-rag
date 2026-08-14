# from sentence_transformers import SentenceTransformer

# def create_embeddings(text):
#     model = SentenceTransformer("all-MiniLM-L6-V2")
#     embeddings = model.encode(text)
#     return  embeddings 
# print(create_embeddings("what is machine learning"))



from langchain_huggingface import HuggingFaceEmbeddings
# def get_embedding_model(text):
#     model = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-V2")
#     embeddings = model.embed_query(text)
#     return embeddings

# print(get_embedding_model("what is machine learning"))

def get_embedding_model():
    model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return model



