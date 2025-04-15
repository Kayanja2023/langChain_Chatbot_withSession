from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from memory.memory_manager import get_buffer_memory
from prompts.templates import get_prompt
from config.config import load_api_keys

def create_conversation_chain():
    load_api_keys()
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
    memory = get_buffer_memory()
    prompt = get_prompt()
    return ConversationChain(llm=llm, prompt=prompt, memory=memory, verbose=True)
