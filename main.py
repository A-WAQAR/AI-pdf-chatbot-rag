from fastapi import FastAPI
from api.routes import router
from utils.pdf_loader import load_pdf
from utils.splitter import split_docs
from utils.embeddings import get_embedding_model
from utils.vector_store import build_vector_store

vectorstore_obj = None

def init_vector_store():
    global vectorstore_obj
    docs = load_pdf("data/sample.pdf")
    chunks = split_docs(docs)
    embeddings = get_embedding_model()
    vectorstore_obj = build_vector_store(chunks, embeddings)
    return vectorstore_obj

def create_app():
    
    app = FastAPI(
        title="pdf rag chatbot is running"
    )
    init_vector_store()

    app.include_router(router)
    return app
app = create_app()


