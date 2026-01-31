"""
Endee Vector Store Adapter

NOTE:
Endee is a standalone vector database service.
This adapter simulates client-side interaction for embedding storage
and similarity search for demonstration and evaluation purposes.
"""

import numpy as np
import uuid

class EndeeVectorStore:
    def __init__(self):
        self.vectors = []
        self.metadata = []

    def add_documents(self, texts, embeddings, metadata_list=None):
        for i, vector in enumerate(embeddings):
            self.vectors.append(np.array(vector))
            self.metadata.append({
                "id": str(uuid.uuid4()),
                "text": texts[i]
            })

    def similarity_search(self, query_embedding, top_k=3):
        query_vec = np.array(query_embedding)

        scores = []
        for i, vec in enumerate(self.vectors):
            similarity = np.dot(vec, query_vec) / (
                np.linalg.norm(vec) * np.linalg.norm(query_vec)
            )
            scores.append((similarity, self.metadata[i]))

        scores.sort(reverse=True, key=lambda x: x[0])
        return [{"metadata": item[1]} for item in scores[:top_k]]
