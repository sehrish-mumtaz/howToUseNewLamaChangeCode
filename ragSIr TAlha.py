# 1st prompt what is RAG (retrieval augmented generation) what are the main component of Rag? i am a beginner having no knowlegde about rag. act as an expert and give me answer according to it
# 2nd prompt i want to built a simple RAg based application. give me complete code. i donot have access to paid APIs. use open source model for it. i am going to use groq Api key to intereact with the llm here are the documentation for the groq. i will be running the codes on google colab
# 1st code of rag in google colab of streamlit
# Step 1: Install necessary packages (Run this in Colab or your local environment first)
!pip install faiss-cpu sentence-transformers groq streamlit pymupdf
# 2nd code of rag in google colab about streamlit
# Step 2: Import libraries
import os
import numpy as np
import faiss
import fitz  # PyMuPDF
import streamlit as st
from sentence_transformers import SentenceTransformer
from groq import Groq

# Step 3: Initialize the Groq client
os.environ["GROQ_API_KEY"] = "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"  # Replace with your actual Groq API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Step 4: Define a function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Step 5: Initialize SentenceTransformer model and FAISS index
model = SentenceTransformer('all-MiniLM-L6-v2')
documents = []  # Initialize empty list for documents

# Step 6: Define RAG function
def retrieve_and_generate(query, documents, document_embeddings, index):
    # Convert query to embedding
    query_embedding = model.encode([query])

    # Retrieve similar documents
    _, indices = index.search(query_embedding, k=2)  # Retrieve top 2 similar docs
    retrieved_text = " ".join([documents[idx] for idx in indices[0]])
    
    # Generate response using Groq LLM
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Based on the following information: {retrieved_text}, answer the question: {query}"
            }
        ],
        model="llama3-8b-8192"
    )
    
    return chat_completion.choices[0].message.content

# Step 7: Streamlit App
def main():
    st.title("PDF-based RAG Chatbot")

    # PDF upload and extraction
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
    if pdf_file:
        st.write("Extracting text from PDF...")
        extracted_text = extract_text_from_pdf(pdf_file)
        documents.append(extracted_text)  # Append extracted text to documents list

        # Generate document embeddings and FAISS index
        document_embeddings = model.encode(documents)
        index = faiss.IndexFlatL2(document_embeddings.shape[1])
        index.add(np.array(document_embeddings))

    # Query input
    user_query = st.text_input("Enter your query:")
    if st.button("Generate Response") and user_query and documents:
        response = retrieve_and_generate(user_query, documents, document_embeddings, index)
        st.write("### Generated Response:")
        st.write(response)

# Run the Streamlit app (won't work in Colab, but allows testing code functionality)
if __name__ == "__main__":
    main()

# 3rd prompt i am creating a pdf question answer chatbot i will upload a pdf file the application will process the pdf file now implement the Rag in this application give me complete code i will be running the codes on google colab. i donot have access to paid APIs use open source model for it. i am going to use groq Api key to intereact, here are the documentation for the groq.


