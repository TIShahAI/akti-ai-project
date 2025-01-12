import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings


def pdf_database(question):
    file_path="pdf"
    pdf_files =[os.path.join(file_path,f) for f in os.listdir(file_path) if f.endswith(".pdf")]

    pages =[]
    for i in pdf_files:
        loader = PyPDFLoader(i)
        for page in loader.load():
            pages.append(page)

    vector_store = InMemoryVectorStore.from_documents(pages,OpenAIEmbeddings())
    documents = vector_store.similarity_search(question)
    return " ".join([page.page_content for page in documents])
