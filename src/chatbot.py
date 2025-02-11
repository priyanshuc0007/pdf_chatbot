import os
from langchain.chains import ConversationalRetrievalChain
from langchain_groq import ChatGroq
from vector_store import vector_store
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0.1)

# Create retrieval chain
retrieval_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vector_store.as_retriever(top_k=3),
    return_source_documents=True
)
conversation_history = []

def get_response(user_query):
    response = retrieval_chain({
        "question": user_query,
        "chat_history": conversation_history
    })
    conversation_history.append((user_query, response['answer']))
    return response['answer']