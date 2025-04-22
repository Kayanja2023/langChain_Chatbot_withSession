# chains/conversation_chain.py
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

# 1. Define the system + user prompt structure with history
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful, context-aware assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# 2. Configure the LLM (GPT-4 Turbo)
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)

# 3. Bind the prompt to the LLM pipeline
chain = prompt | llm

# 4. In-memory store to simulate per-session chat history
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 5. Create the Runnable chain with memory integration
chatbot_chain = RunnableWithMessageHistory(
    chain,
    lambda session_id: get_session_history(session_id),
    input_messages_key="input",
    history_messages_key="history"
)
