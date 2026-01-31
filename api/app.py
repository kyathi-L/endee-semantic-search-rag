from fastapi import FastAPI
from pydantic import BaseModel
from rag.rag_pipeline import RAGPipeline

# --------------------------------------------------
# FastAPI App Initialization
# --------------------------------------------------
app = FastAPI(
    title="Endee Semantic Search & RAG API",
    description="Semantic Search and RAG system using Endee as the vector database",
    version="1.0.0"
)

# --------------------------------------------------
# Initialize RAG Pipeline
# --------------------------------------------------
rag = RAGPipeline()

# Sample documents (used for demo & evaluation)
documents = [
    "Artificial Intelligence enables machines to think and learn from data",
    "Vector databases store embeddings and enable similarity-based search",
    "Retrieval Augmented Generation combines document retrieval with text generation"
]

# Ingest documents on startup
rag.ingest_documents(documents)

# --------------------------------------------------
# Request Model
# --------------------------------------------------
class QueryRequest(BaseModel):
    query: str

# --------------------------------------------------
# API Endpoints
# --------------------------------------------------
@app.get("/")
def root():
    return {
        "message": "Endee Semantic Search & RAG API is running successfully"
    }

@app.post("/search")
def semantic_search(request: QueryRequest):
    """
    Perform semantic search using vector similarity
    """
    results = rag.semantic_search(request.query)
    return {
        "query": request.query,
        "results": results
    }

@app.post("/ask")
def ask_question(request: QueryRequest):
    """
    Answer a question using Retrieval Augmented Generation (RAG)
    """
    answer = rag.answer_question(request.query)
    return {
        "query": request.query,
        "answer": answer
    }
