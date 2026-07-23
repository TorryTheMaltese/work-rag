from sentence_transformers import SentenceTransformer # type: ignore

model = SentenceTransformer('BAAI/bge-m3')


def create_embedding(text: str) -> list[float]:
    embedding = model.encode(text)
    return embedding.tolist()
