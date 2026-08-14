import os
from langchain_groq import ChatGroq 
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
def run_rag(build_vector_store, question):

    retriever = build_vector_store.as_retriever(
        search_kwargs={"k":3}
    )

    prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Use only the following context.

Context:
{context}

Question:
{question}

Answer:
""")
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        groq_api_key=os.getenv("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")
    )

    chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    response = chain.invoke(question)
    return response
