from embeddings.embedder import Embedder

embedder = Embedder()
vectors = embedder.embed_text(["Hello world", "AI and vector databases"])
print(len(vectors), len(vectors[0]))
