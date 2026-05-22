class TextChunker:
    def __init__(self, chunk_size: int = 600, chunk_overlap: int = 120):
        """
        AI Framework Chunker Blueprint.
        Defines how raw documents are sliced into contextual windows.
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.processed_chunks = []  # Final payload list structure

    def split_documents(self, raw_documents: list) -> list:
        """
        Takes the raw payload list from Phase 1 and splits every node 
        into smaller overlapping semantic blocks.
        """
        self.processed_chunks = []  # Resetting local storage matrix

        for doc in raw_documents:
            text = doc["text"]
            metadata = doc["metadata"]
            
            start = 0
            text_length = len(text)
            
            # Sliding window core algorithm mapping character streams
            while start < text_length:
                # Determining the end of the current chunk window
                end = start + self.chunk_size
                chunk_text = text[start:end]
                
                # Appending a structured node with inherited tracking attributes
                self.processed_chunks.append({
                    "text": chunk_text.strip(),
                    "metadata": metadata.copy()  # Preserving metadata file trace tags safely
                })
                
                # Moving the sliding character loop pointer forward via offset threshold
                start += (self.chunk_size - self.chunk_overlap)
                
                # Infinite loop execution protection handler
                if self.chunk_size <= self.chunk_overlap:
                    break
                    
        print(f"[SUCCESS] Successfully generated {len(self.processed_chunks)} chunks from raw files.")
        return self.processed_chunks