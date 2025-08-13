from sentence_transformers import SentenceTransformer
from langchain_core.embeddings import Embeddings
from typing import List

class LocalEmbeddings(Embeddings):
    def __init__(self, model_name: str, from_local = False, emb_mod = None):
        if not from_local:
            self.model = SentenceTransformer(model_name)
        else:
            self.model = emb_mod

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self.model.encode(text).tolist() for text in texts]

    def embed_query(self, query: str) -> List[float]:
        return self.model.encode(query).tolist()