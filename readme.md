# 🧠 RAG-Powered Chatbot for Current Affairs 📚  

A Retrieval-Augmented Generation (RAG) chatbot designed to help students stay updated with the latest current affairs. This chatbot processes PDFs containing current events, extracts key information, and provides insightful responses using a Large Language Model (LLM).  

## 🚀 Features  

- 📄 **PDF Processing:** Automatically extracts and processes text from current affairs PDFs.  
- 🔍 **Retrieval-Augmented Generation (RAG):** Enhances chatbot responses with real-time retrieval from the uploaded documents.  
- 💡 **Intelligent Summarization:** Provides concise summaries of key topics.  
- 🗂️ **Efficient Query Handling:** Understands and answers student queries based on the latest current affairs.  
- 🖥️ **User-Friendly Interface:** gradio-based interactive UI for seamless experience.  

## 🛠️ Tech Stack  

- **Python** (Core logic)  
- **LangChain** (For RAG implementation)  
- **OpenAI / Hugging Face LLMs** (For generating responses)  
- **FAISS / ChromaDB** (For efficient document retrieval)  
- **PyMuPDF / PDFPlumber** (For PDF text extraction)  
- **gradio** (For interactive UI)  

## 📦 Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/pdf_chatbot.git
   cd pdf_chatbot
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the chatbot:  
   ```bash
    run app.py
   ```  

## 🎯 How It Works  

1. **Upload PDF(s)** – Add current affairs PDFs to the chatbot.  
2. **Indexing** – The system processes and stores document embeddings.  
3. **Ask Questions** – Query the chatbot about specific topics.  
4. **Get AI-Powered Responses** – The chatbot retrieves relevant info and generates insightful answers.  

## 📸 Screenshots  

(Add screenshots of your chatbot interface here.)  

## 📌 Future Enhancements  

- ✅ Add support for multiple document formats.  
- ✅ Improve retrieval accuracy using advanced embeddings.  
- ✅ Integrate real-time news APIs for dynamic updates.  

## 🏆 Contributing  

Contributions are welcome! Feel free to submit issues or pull requests to improve the chatbot.  

## 📜 License  

This project is open-source under the **MIT License**.  
