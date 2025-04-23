from chains.conversation_chain import chatbot_chain

def handle_query(user_input: str, session_id: str = "default-session") -> str:
    """
    Handles user input and generates a response using the LangChain pipeline.

    Args:
        user_input (str): The user's message.
        session_id (str): A session identifier for tracking memory context.

    Returns:
        str: The chatbot's generated reply.
    """
    response = chatbot_chain.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": session_id}}  # Pass required session_id
    )
    return response.content


if __name__ == "__main__":
    print("🤖 Chatbot is ready. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Bot:", handle_query(user_input))
