## infosEAk Chatbot

### Overview
**infosEAk** is a proof-of-concept chatbot developed during Environics Analytics' first hackathon, IDEATE. This project won first place by showcasing a working solution within a tight two-working-day timeline.
The chatbot leverages internal employee documents and variable list information to provide concise and accurate responses. It uses the LangChain framework for document retrieval and processing and a simple tkinter-based user interface (UI) for user interaction.

### Features
- **Document Retrieval**: Parses and processes PDF documents to extract relevant information.
- **RAG (Retrieval-Augmented Generation) Chain**: Combines document context with user queries to generate accurate answers.
- **LangChain Integration**: Uses LangChain's tools for text splitting, embedding, and vector storage.
- **Custom Prompt**: Tailored prompt for concise and helpful responses.
- **User Interface**: A tkinter-based UI for interacting with the chatbot.

### Purpose
The goal of this project was to demonstrate the potential of deploying AI solutions within organizations. The chatbot serves as a practical example of how internal knowledge can be leveraged for quick and effective employee assistance.

### How It Works
1. **Load Environment Variables**: Retrieves API keys and other configuration settings.
2. **Document Loading**: Reads all PDFs from a specified directory.
3. **Preprocessing**: Cleans and splits the text into manageable chunks.
4. **Vectorization**: Converts text chunks into embeddings for efficient search.
5. **Chat Model**: Uses OpenAI's GPT model for natural language understanding and response generation.
6. **User Interaction**: Provides a simple UI where users can type queries and receive answers.

### Tech Stack
- **Python**: Core programming language.
- **LangChain**: Framework for document processing and retrieval.
- **tkinter**: Library for creating the UI.
- **Chroma**: Vector database for document embeddings.
- **OpenAI GPT**: Language model for generating responses.

### Running the Project
1. Clone this repository.
2. Install required dependencies: pip install langchain chromadb openai tkinter
3. Set up the environment variables in a .env file: OPENAI_API_KEY=your_openai_api_key_here
4. Run the chatbot: python infosEAk_chatbot.py

### Hackathon Results
This project was developed in under two days during the IDEATE hackathon and earned first place for delivering a functional proof of concept. It highlights the potential of AI-powered tools in enhancing organizational efficiency and innovation.
For more details about the hackathon, read the official blog post: https://environicsanalytics.com/en-ca/resources/blogs/ea-blog/2023/10/31/introducing-ideate-environics-analytics-first-hackathon .

### Future Enhancements
- **Deploy to Microsoft Teams**: Integrate the chatbot into Teams for broader accessibility.
- **Enhanced UI**: Replace tkinter with a modern web-based interface.
- **Additional Features**: Incorporate more advanced NLP features and support for other document types.

