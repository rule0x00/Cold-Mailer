from llama_index.readers.file import PDFReader

def parse_document(file_path: str):
    """
    Parse a single PDF resume file using LlamaIndex's PDFReader.
    
    Args:
        file_path (str): Path to the resume PDF file.
    
    Returns:
        List[Document]: A list of LlamaIndex Document objects.
    """

    print(f"file path is ", file_path)
    reader = PDFReader()
    documents = reader.load_data(file_path)
    return documents
