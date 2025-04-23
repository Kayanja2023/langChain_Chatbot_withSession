# Load Environment Variables
from dotenv import load_dotenv
load_dotenv()

"""
Loads credentials and sensitive variables (e.g., OpenAI API key)
from a local .env file into environment variables.
"""

# 1. Import LangChain Modules
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

"""
Imports LangChain components:
- ChatOpenAI: wrapper for OpenAI's GPT model
- ChatPromptTemplate: defines structured prompts with dynamic input
- MessagesPlaceholder: injects prior history into prompt flow
- RunnableWithMessageHistory: adds memory context to a chain
- InMemoryChatMessageHistory: tracks dialogue during session
"""

# 2. Prompt Template Configuration
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful, context-aware assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

"""
Defines the format of the chat prompt:
- System message defines assistant behavior.
- `history` variable injects previous exchanges.
- `{input}` placeholder is filled with the user's current query.
"""

# 3. Language Model Initialization
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)

"""
Initializes GPT-3.5-turbo with moderate creativity.
"""

# 4. Core Chain Composition (Prompt → LLM)
chain = prompt | llm

"""
Chains the prompt and LLM into a runnable pipeline.
"""

# 5. Memory Store for Session Memory
session_store = {}

def get_session_history(session_id: str):
    """
    Ensures the same memory object is reused for each session.
    This allows multi-turn context retention across a session's lifetime.
    """
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

# 6. Chatbot Chain with Session-Based Buffer Memory
chatbot_chain = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=get_session_history,  # Returns memory scoped to session_id
    input_messages_key="input",               # Must match input placeholder in prompt
    history_messages_key="history"            # Must match MessagesPlaceholder key
)

"""
Creates a memory-enabled chatbot chain.
- Memory is retained per session using a dictionary-based store.
- Buffer memory is preserved during program runtime (but not persisted across restarts).
"""
