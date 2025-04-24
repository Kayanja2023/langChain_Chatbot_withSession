"""
chatbot.py

Launches an interactive CLI chatbot using LangChain + OpenAI with buffer memory.
"""

from dotenv import load_dotenv
load_dotenv()

from chains.conversation_chain import chatbot_chain

def handle_query(user_input: str, session_id: str = "default-session") -> str:
    """
    Invokes the chatbot chain with the user's input and session ID.

    Args:
        user_input (str): The user's message.
        session_id (str): A session identifier for tracking memory context.

    Returns:
        str: The chatbot's generated reply.
    """
    response = chatbot_chain.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": session_id}}  # Required for buffer memory
    )
    return response.content


if __name__ == "__main__":
    print("🤖 Chatbot is ready. Type 'exit' to quit.\n")

    session_id = "user-session-001"  # #Persistent ID for session memory

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("👋 Ending session. Goodbye!")
            break

        response = handle_query(user_input, session_id=session_id)
        print(f"Bot: {response}\n")
