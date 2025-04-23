from langchain.prompts import PromptTemplate

def get_prompt():
    """
    Returns a reusable PromptTemplate for simulating a multi-turn conversation
    between a human and an AI assistant.

    Structure:
    - Static introduction defines the assistant’s tone and behavior
    - {history} placeholder inserts prior chat messages for memory context
    - {input} placeholder represents the user’s current message
    """

    # Define the template string with labeled dialogue structure
    template = """
    The following is a friendly conversation between a human and an AI assistant.
    The assistant is helpful, creative, and provides relevant answers based on past context.

    {history}
    Human: {input}
    AI:"""

    # Return a PromptTemplate instance configured with required input variables
    return PromptTemplate(
        input_variables=["history", "input"],
        template=template
    )
