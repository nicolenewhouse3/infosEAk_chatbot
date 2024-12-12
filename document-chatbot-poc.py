# infosEAk Chatbot
# Proof of Concept by Nicole Newhouse
# Description: A chatbot trained on employee documents and variable list information using LangChain and tkinter for the interface.

import dotenv
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import PromptTemplate
import os
import tkinter as tk

# Load environment variables
dotenv.load_dotenv("C:/Environics/chatbot.env.txt")
api_key = os.environ.get('OPENAI_API_KEY')

# Directory containing documents to train the chatbot
directory = "//willow/Users/Nicole Newhouse/Alldocs"

# Load and preprocess documents
loader = PyPDFDirectoryLoader(directory)
page_doc = loader.load()

# Minor cleaning to improve document readability
for doc in page_doc:
    doc.page_content = doc.page_content.replace('\n', ' \n ').replace('  ', ' ').replace('\n', '.')

# Split documents into manageable chunks for vectorization
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
splits = text_splitter.split_documents(page_doc)

# Create vectorstore for document retrieval
vectorstore = Chroma.from_documents(
    documents=splits, embedding=OpenAIEmbeddings(openai_api_key=api_key))
retriever = vectorstore.as_retriever()

# Load the chat model
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Define the prompt template
template = """
Use the following pieces of context to answer the question at the end. 
Use five sentences maximum and keep the answer as concise as possible.
    {context}
Question: 
    {question}
Helpful Answer:
"""
rag_prompt_custom = PromptTemplate.from_template(template)

# Define the retrieval-augmented generation (RAG) chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | rag_prompt_custom
    | llm
)

# Define the tkinter-based chatbot UI class
class ChatbotUI:
    def __init__(self, master):
        """Initialize the chatbot UI with tkinter components and layout."""
        self.master = master
        master.title("infosEAk")

        # Load and display the logo
        self.logo = tk.PhotoImage(
            file="//willow/marketing/Brand Assets/Logos/Environics Analytics/Environics-Analytics-Logo-75.png")
        self.logo_label = tk.Label(master, image=self.logo)
        self.logo_label.pack()

        # Chat display
        self.text = tk.Text(master)
        self.text.pack(expand=True, fill='both')

        # Input section
        self.bottom_frame = tk.Frame(master)
        self.bottom_frame.pack(side='bottom', fill='both', pady=5)
        
        self.entry = tk.Entry(self.bottom_frame, width=80)
        self.entry.pack(side='left', expand=True, fill='x', padx=(5, 0))
        self.entry.insert(0, "Type your question here")
        self.entry.config(fg='grey')
        self.entry.bind("<FocusIn>", self.on_entry_click)
        self.entry.bind("<FocusOut>", self.on_focusout)
        self.entry.bind("<Return>", self.ask_question)

        self.send_button = tk.Button(self.bottom_frame, text="Send", command=self.ask_question)
        self.send_button.pack(side='left', padx=(5, 5))

    def on_entry_click(self, event):
        """Handle entry focus event to clear placeholder text."""
        if self.entry.get() == "Type your question here":
            self.entry.delete(0, "end")
            self.entry.insert(0, '')
            self.entry.config(fg='black')

    def on_focusout(self, event):
        """Handle entry focus out event to restore placeholder text if empty."""
        if self.entry.get() == '':
            self.entry.insert(0, "Type your question here")
            self.entry.config(fg='grey')

    def ask_question(self, event=None):
        """Send user input to the chatbot model and display the response."""
        user_input = self.entry.get()
        self.text.insert(tk.END, "You: " + user_input + "\n")

        # Get response from the chatbot model
        response = self.get_response(user_input)
        response_text = response.text if hasattr(response, 'text') else str(response)
        formatted_response = response_text.replace("content='", '').replace("'\n", '')

        # Display bot response
        self.text.tag_configure('purple_font', foreground='purple')
        self.text.insert(tk.END, "infosEAk: " + formatted_response + "\n\n", 'purple_font')

        self.entry.delete(0, tk.END)

    def get_response(self, user_input):
        """Invoke the RAG chain to get a response for the user's question."""
        return rag_chain.invoke(user_input)

# Run the chatbot UI
if __name__ == "__main__":
    root = tk.Tk()
    chatbot_ui = ChatbotUI(root)
    root.mainloop()
