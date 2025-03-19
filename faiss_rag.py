import faiss
import numpy as np
import os
import re
from sentence_transformers import SentenceTransformer

# Load Sentence Transformer Model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Read "The Gift of the Magi" Markdown file and preprocess text
def load_story():
    with open("The Gift of Magi.md", "r", encoding="utf-8") as f:
        text = f.read()

    # Remove Markdown syntax like headers, bold, and lists
    text = re.sub(r"#.*", "", text)  # Remove headers
    text = re.sub(r"\*\*.*?\*\*", "", text)  # Remove bold text
    text = re.sub(r"\*.*?\*", "", text)  # Remove italicized text
    text = re.sub(r"\[.*?\]\(.*?\)", "", text)  # Remove hyperlinks
    text = re.sub(r"[-*_]", "", text)  # Remove bullet points

    # Split text into paragraphs (using double newlines)
    chunks = text.split("\n\n")
    
    # Clean up spaces and remove empty lines
    return [chunk.strip() for chunk in chunks if chunk.strip()]

# Load the story into chunks
documents = load_story()
dimension = 384  # Embedding dimension

# Initialize FAISS index
faiss_index = faiss.IndexFlatL2(dimension)

# File to save the FAISS index
faiss_file = "faiss_magi.bin"

# Create or load FAISS index
if os.path.exists(faiss_file):
    faiss_index = faiss.read_index(faiss_file)
    print("FAISS index loaded from file.")
else:
    print("Creating FAISS index...")
    document_embeddings = embedding_model.encode(documents)
    faiss_index.add(np.array(document_embeddings))  # Add embeddings to FAISS index
    faiss.write_index(faiss_index, faiss_file)
    print("FAISS index created and saved.")

def search_rag(query):
    """Search FAISS for the most relevant document."""
    query_embedding = embedding_model.encode([query])
    D, I = faiss_index.search(np.array(query_embedding), k=1)  # Search top 1 result
    
    if I[0][0] >= len(documents):
        return "No relevant document found."
    
    return documents[I[0][0]]  # Return the most relevant document

# Uncomment below to test manually
# if __name__ == "__main__":
#     while True:
#         user_input = input("Enter your query (or type 'exit'): ")
#         if user_input.lower() == "exit":
#             break
#         response = search_rag(user_input)
#         print("RAG Response:", response)
