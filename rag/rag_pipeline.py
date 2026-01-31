from embeddings.embedder import Embedder
from endee_store.vector_store import EndeeVectorStore

class RAGPipeline:
    def __init__(self):
        self.embedder = Embedder()
        self.store = EndeeVectorStore()

    def ingest_documents(self, texts):
        embeddings = self.embedder.embed_text(texts)
        self.store.add_documents(texts, embeddings)

    def semantic_search(self, query, top_k=3):
        query_embedding = self.embedder.embed_text([query])[0]
        results = self.store.similarity_search(query_embedding, top_k)
        return [r["metadata"]["text"] for r in results]

    def answer_question(self, question):
        retrieved_docs = self.semantic_search(question)
        context = "\n".join(retrieved_docs)

        # Simple RAG-style response (LLM placeholder)
        answer = f"""
Answer generated using retrieved context:

Context:
{context}

Question:
{question}

Answer:
Based on the above documents, the answer is related to vector databases, AI, and RAG concepts.
"""
        return answer.strip()
