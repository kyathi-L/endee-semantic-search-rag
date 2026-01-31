from embeddings.embedder import Embedder
from endee_store.vector_store import EndeeVectorStore

texts = [
    "Artificial Intelligence enables machines to think",
    "Vector databases store embeddings for similarity search",
    "RAG combines retrieval with generation"
]

embedder = Embedder()
vectors = embedder.embed_text(texts)

store = EndeeVectorStore()
store.add_documents(texts, vectors)

query = "What is a vector database?"
query_vector = embedder.embed_text([query])[0]

results = store.similarity_search(query_vector)

for r in results:
    print(r["metadata"]["text"])
