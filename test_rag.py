from rag.rag_pipeline import RAGPipeline

docs = [
    "Artificial Intelligence enables machines to think",
    "Vector databases store embeddings for similarity search",
    "RAG combines retrieval with generation"
]

rag = RAGPipeline()
rag.ingest_documents(docs)

print(rag.semantic_search("What is a vector database?"))
print("\n")
print(rag.answer_question("Explain RAG"))
