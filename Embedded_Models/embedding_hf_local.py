from langchain_huggingface import HuggingFaceEmbeddings
# pip3 install sentence-transformers
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# text = "Delhi is the capital of India."
# vector = embedding.embed_query(text)
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]
vector = embedding.embed_documents(documents)

print(str(vector))
