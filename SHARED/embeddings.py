from sentence_transformers import SentenceTransformer
from modelscope import snapshot_download


model_name = snapshot_download("BAAI/bge-small-en-v1.5")
model = SentenceTransformer(model_name)

def generate_embedding(text):
    embedding = model.encode(
        text
    )

    vector=embedding.tolist()

    return vector