import unittest
from chains.conversation_chain import chatbot_chain

class TestChatbotChain(unittest.TestCase):
    """
    Unit tests for validating the LangChain pipeline using chatbot_chain.
    """

    def test_chain_generates_response(self):
        """
        Ensures that invoking chatbot_chain with input and session ID
        returns a valid response containing non-empty content.
        """
        # Arrange: Simulate a session and user input
        input_data = {"input": "Tell me a programming joke"}
        config = {"configurable": {"session_id": "test-session-001"}}

        # Act: Invoke the chain
        result = chatbot_chain.invoke(input_data, config=config)

        # Assert: Output should include a response with content
        self.assertTrue(hasattr(result, "content"))
        self.assertGreater(len(result.content), 0)

# Enable standalone execution
if __name__ == "__main__":
    unittest.main()
