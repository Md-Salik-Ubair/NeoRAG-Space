class TextChunker:
    def __init__(self, chunk_size: int = 600, chunk_overlap: int = 120):
        """
        AI Framework Chunker Blueprint.
        Defines how raw documents are sliced into contextual windows.
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.processed_chunks = []  # Final payload: [{'text': chunk, 'metadata': ...}]

    def split_documents(self, raw_documents: list) -> list:
        """
        Takes the raw payload list from Phase 1 and splits every node 
        into smaller overlapping semantic blocks.
        """
        self.processed_chunks = []  # Resetting storage

        for doc in raw_documents:
            text = doc["text"]
            metadata = doc["metadata"]
            
            start = 0
            text_length = len(text)
            
            # Sliding window algorithm
            while start < text_length:
                # Determining the end of the current chunk window
                end = start + self.chunk_size
                chunk_text = text[start:end]
                
                # Making a naye structured node with combined text and inherited metadata
                self.processed_chunks.append({
                    "text": chunk_text.strip(),
                    "metadata": metadata.copy()  # Preserving source tracking details
                })
                
                # Moving the window forward by subtracting the overlap
                start += (self.chunk_size - self.chunk_overlap)
                
                # Handling infinite loop safety condition if size configuration goes wrong
                if self.chunk_size <= self.chunk_overlap:
                    break
                    
        print(f"[SUCCESS] Successfully generated {len(self.processed_chunks)} chunks from raw files.")
        return self.processed_chunks