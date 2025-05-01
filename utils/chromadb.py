import chromadb
import uuid

def store_embeddings_in_chroma(embedded_data, metadata, collection_name="resumes"):
    # Initialize the Chroma client
    client = chromadb.PersistentClient(path="vectorstore")
    
    # Create or get the collection
    collection = client.get_or_create_collection(name=collection_name)
    
    embeddings = [embedded_data] if not isinstance(embedded_data, list) else embedded_data
    
    # Generate a unique user ID for the document
    user_ids = [str(uuid.uuid4())] 
    
    # Add documents to the collection
    collection.add(
        embeddings=embeddings,
        metadatas=[metadata], 
        ids=user_ids 
    )

    print(f"Successfully stored 1 document in ChromaDB.")
