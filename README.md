# Text Chunking using RecursiveCharacterTextSplitter 
Implemented document chunking using LangChain's RecursiveCharacterTextSplitter with configurable chunk size and overlap to improve retrieval quality in a RAG pipelin

# Embeddings
Implemented semantic text embeddings using the Sentence Transformers model (all-MiniLM-L6-v2) to convert document chunks into dense vector representations for efficient similarity search in a RAG pipeline.

# FAISS Vector Database
Built a semantic retrieval pipeline using FAISS by indexing dense document embeddings and performing efficient top-k similarity search to support a Retrieval-Augmented Generation (RAG) application.

# retrieval (LCEL + RAG)
Built a modular Retrieval-Augmented Generation (RAG) pipeline using LangChain's modern runnable architecture, integrating a retriever, prompt templates, an LLM, and output parsing for semantic question answering over PDF documents.

