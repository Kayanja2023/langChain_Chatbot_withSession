## [RaD-GP-C25-P-I4] Unleashing Generative AI with LangChain: Building an Intelligent Chatbot with Buffer Memory

## Requirements 
This project requires a comprehensive exploration of the LangChain framework, including its architecture, components, and application in Generative AI development. Key deliverables include a detailed research summary, the development of a context-aware chatbot utilizing buffer memory, and a fully documented GitLab repository containing all source code and supporting materials. Additionally, a 20-minute presentation is required to demonstrate the chatbot’s functionality and to communicate the research findings, implementation approach, and practical use of LangChain in language model-driven applications. Evaluation will be based on research quality, technical implementation, documentation, and presentation delivery
## Overview

This project demonstrates the use of the **LangChain framework** to develop a context-aware chatbot powered by large language models (LLMs). The chatbot utilizes **buffer memory** to maintain conversational history, enabling more natural, coherent, and contextually relevant interactions.


---

## Objectives

1. Conduct comprehensive research on the LangChain framework and its components.
2. Explore its core abstractions, modular architecture, and integration patterns.
3. Develop a functional chatbot using LangChain, featuring conversational memory.
4. Document all findings and implementation steps in a structured format.
5. Deliver a final presentation including a live demo and summary of key takeaways.

---
## File Structure
``` pycon
langchain-chatbot-project/
├── chatbot.py                       # Entry point script that runs the chatbot
│
├── chains/                          # Contains logic for chain creation
│   ├── __init__.py        # Sets up ConversationalRetrievalChain or ConversationChain
│   └── conversation_chain.py          # Loads vector store and OpenAI embeddings
│
├── memory/                          # Handles memory and persistence
│   ├── memory_manager.py            # Initializes ConversationBufferMemory
│   └── persistence.py               # Saves and loads long_chat_history to disk
│
├── prompts/                         # All prompt templates for chat style and system messages
│   └── templates.py                 # Defines prompt templates used in the chain
│
├── config/                          # API key management and environment setup
│   └── config.py                    # Loads .env and environment variables
│
├── data/                            # Local data storage
│   ├── chroma/                      # Directory for persisted Chroma vector DB (if using RAG)
│   └── history_logs.json            # Saved long-term chat history
│
├── docs/                            # Research and documentation
│   ├── langchain-framework-summary.pdf
│   └── architecture-diagram.png
│
├── presentation/                    # Demo slide deck and presentation script
│   ├── langchain-demo-slides.pptx
│   └── demo-script.md
│
├── tests/                           # Unit tests for chains, memory, etc.
│   └── test_chatbot.py
│
├── .env                             # Your actual environment variables (ignored in .gitignore)
├── .env.example                     # Example environment variable file
├── .gitignore                       # Ensures secrets and data folders aren't pushed
├── README.md                        # Setup, usage, and technical overview
├── requirements.txt                 # List of Python dependencies
└── project_reference.txt            # Metadata or reference info (RaD-GP-C25-P-I4)

```


## Features

- Real-time user interaction via command-line or web interface (Streamlit/Gradio).
- Buffer memory to store and reference previous dialogue turns.
- Modular LangChain components: LLM wrappers, Chains, Memory, Prompt Templates.
- Structured documentation on LangChain's design and use cases.
- Secure handling of API keys using environment variables.

---

## Installation & Setup

### 1. Clone Repository
```bash
git clone https://gitlab1a.prod.eu-west-1.aws.clickatell.com/andile.lwanga/rad-gp-c25-p-i4
```
### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```
### 3.Install Dependancies
``
pip install -r requirements.txt
``
### 4. Configuire Environment Variables
````bash
OPENAI_API_KEY=your_openai_api_key

````
## How to Run
```bash
python src/chatbot.py
```

## Tech Stack

- **Language**: Python 3.x
- **Framework**: [LangChain](https://www.langchain.com/)
- **LLM Provider**: OpenAI / Hugging Face
- **Interface**: CLI or Web (Streamlit)
- **Memory**: `ConversationBufferMemory`


---