# 0. Load Environment Variables
from dotenv import load_dotenv
load_dotenv()

""" 
Loads environment variables at runtime from a `.env` file.
This allows access to sensitive credentials like the OpenAI API key
without hardcoding them into the source.
"""

# 1. Import LangChain Modules
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

"""
Imports essential LangChain components:
- ChatOpenAI for model integration
- ChatPromptTemplate for formatting multi-turn prompts
- RunnableWithMessageHistory for managing in-session memory
- InMemoryChatMessageHistory for non-persistent message tracking
"""

# 2. Prompt Template Configuration
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful, context-aware assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

"""
Defines the prompt structure for the conversation.
- The system message sets the assistant’s tone and role.
- The history placeholder injects prior user/AI messages.
- The input placeholder dynamically inserts the current user query.
"""

# 3. Language Model Initialization
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)

"""
Initializes the language model (GPT-3.5-turbo) using LangChain's ChatOpenAI wrapper.
- Temperature is set to 0.7 for balanced creativity.
- Abstracts OpenAI's API into a standard LangChain-compatible interface.
"""

# 4. Core Chain Composition (Prompt + LLM)
chain = prompt | llm

"""
Chains the prompt and the language model.
This forms the base logic unit for processing input and generating AI responses.
"""

# 5. Runnable Chain with In-Memory Message History
chatbot_chain = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=lambda _: InMemoryChatMessageHistory(),
    input_messages_key="input",
    history_messages_key="history"
)

"""
Wraps the prompt→model chain with an in-session memory manager.
- Uses InMemoryChatMessageHistory to retain dialogue within the session.
- Does not persist memory between sessions.
- Requires a `session_id` to scope memory context when invoking.
"""
