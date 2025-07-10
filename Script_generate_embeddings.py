# 📦 Embedding + Vector Store Setup for Miami 21 Zoning Knowledge

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
import os

# STEP 1: Load markdown chunks
md_path = "Miami21_RAG_KnowledgeChunks.md"
with open(md_path, 'r', encoding='utf-8') as f:
    raw = f.read()

chunks = raw.split("### Zoning Category: ")
documents = []
for chunk in chunks:
    if chunk.strip():
        header = chunk.split("\n")[0].strip()
        content = "### Zoning Category: " + chunk.strip()
        documents.append(Document(page_content=content, metadata={"id": header}))

# STEP 2: Initialize OpenAI embedding model
embedding = OpenAIEmbeddings(model="text-embedding-3-small")  # Low-cost model

# STEP 3: Create or load Chroma vector store
vectordb = Chroma.from_documents(
    documents=documents,
    embedding=embedding,
    persist_directory="miami21_vectorstore"
)

vectordb.persist()
print("✅ Vector store created and saved at ./miami21_vectorstore")
