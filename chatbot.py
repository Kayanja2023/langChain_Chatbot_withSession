from chains.conversation_chain import create_conversation_chain
from memory.persistence import load_long_chat_history, save_long_chat_history

def main():
    conversation = create_conversation_chain()
    long_chat_history = load_long_chat_history()

    print("🤖 Chatbot is ready! Type 'exit' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            save_long_chat_history(long_chat_history)
            break
        response = conversation.predict(input=user_input)
        print(f"Bot: {response}")
        long_chat_history.append(("User", user_input))
        long_chat_history.append(("AI", response))

if __name__ == "__main__":
    main()
