from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_text(self, texts):
        """
        Convert a list of text strings into vector embeddings
        """
        return self.model.encode(texts).tolist()
