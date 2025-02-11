import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from extract_text import extract_text_from_pdf

# Load PDF text
pdf_text = extract_text_from_pdf(r"data\thehindu.pdf")

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
text_chunks = text_splitter.split_text(pdf_text)

# Initialize embedding model
embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Initialize and persist ChromaDB
vector_store = Chroma(
    collection_name="dcurrent_affairs",
    embedding_function=embedding_model,
    persist_directory="../db"
)
vector_store.add_texts(texts=text_chunks)
vector_store.persist()

if __name__ == "__main__":
    print("Vector store initialized and data added.")