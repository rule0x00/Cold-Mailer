from llama_index.core.node_parser import SentenceSplitter

def chunk_document(documents, chunk_size=512, chunk_overlap=50):
    """
    Chunk documents into smaller segments using LlamaIndex's TextSplitter.
    
    Args:
        documents (List[Document]): List of parsed documents.
        chunk_size (int): Max tokens per chunk.
        chunk_overlap (int): Overlap between chunks.
    
    Returns:
        List[Document]: Chunked documents.
    """

    splitter = SentenceSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = []
    for doc in documents:
        chunks.extend(splitter.split_text(doc.text))

    return chunks
