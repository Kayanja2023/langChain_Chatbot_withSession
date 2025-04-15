from langchain.prompts import PromptTemplate

def get_prompt():
    template = """
    The following is a friendly conversation between a human and an AI assistant.
    The assistant is helpful, creative, and provides relevant answers based on past context.

    {history}
    Human: {input}
    AI:"""
    return PromptTemplate(input_variables=["history", "input"], template=template)
