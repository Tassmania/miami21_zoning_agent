# 🤖 rag_agent.py — Retrieve Relevant Chunks + GPT Completion


# from langchain.vectorstores import Chroma
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma


# Load vector store
embedding = OpenAIEmbeddings(model="text-embedding-3-small")
vectordb = Chroma(persist_directory="miami21_vectorstore", embedding_function=embedding)

# LLM setup (OpenAI)
llm = ChatOpenAI(model="gpt-4", temperature=0)

SYSTEM_PROMPT = """
You are a zoning compliance advisor trained on the City of Miami’s Miami 21 zoning code.
Answer precisely based only on retrieved context. Do not speculate.
When responding, clarify whether the use is allowed by right, warrant, or exception,
and quote relevant rule, table, or supplemental regulation.
"""

def query_zoning(question: str, zone_code: str) -> str:
    try:
        zone_key = zone_code.strip().upper().replace(" ", "")  # Normalize

        # Search top 3 matching chunks
        results = vectordb.similarity_search(zone_key, k=3)
        context = "\n---\n".join([doc.page_content for doc in results])

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=f"Context:\n{context}\n\nUser Question: {question}")
        ]

        reply = llm(messages).content
        return reply

    except Exception as e:
        return f"❌ Error during zoning query: {e}"
