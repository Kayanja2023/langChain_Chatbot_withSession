# chatbot.py

from chains.conversation_chain import chatbot_chain

def main():
    session_id = "default"  # can be replaced with a user/session ID
    print("\n🤖 Chatbot is ready (RunnableWithMessageHistory). Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("\n👋 Goodbye!\n")
            break

        response = chatbot_chain.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": session_id}}
        )
        print(f"Bot: {response.content}\n")

if __name__ == "__main__":
    main()
