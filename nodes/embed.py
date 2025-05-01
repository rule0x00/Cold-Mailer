from llama_index.core.schema import Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from utils.chromadb import store_embeddings_in_chroma
import os

from dotenv import load_dotenv

load_dotenv()

def embed_document(chunked_documents: list[str], metadata: dict, model_name: str = os.getenv("MODEL_NAME")):
    """
    Embed documents using a HuggingFace embedding model supported by LlamaIndex and store embeddings in ChromaDB.

    Args:
        chunked_documents (List[str]): List of chunked text strings.
        metadata (dict): A dictionary with additional metadata for each document.
        model_name (str): Name of the HuggingFace embedding model.

    Returns:
        None: The function stores the embeddings and metadata in ChromaDB.
    """
    # Initialize the embedding model
    embed_model = HuggingFaceEmbedding(model_name=model_name)

    for doc_text in chunked_documents:
        # Generate the embedding for each chunk of text
        embedding = embed_model.get_text_embedding(doc_text)

        store_embeddings_in_chroma(embedding, metadata )

    print(f"Successfully stored embeddings for {len(chunked_documents)} chunks in ChromaDB.")
