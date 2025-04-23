import unittest
from chains.conversation_chain import chatbot_chain  # Import chain with memory integration

class TestChatbotChain(unittest.TestCase):
    """
    Unit tests for validating the LangChain pipeline using chatbot_chain.
    """

    def test_chain_generates_response(self):
        """
        Validates that chatbot_chain.invoke() returns a valid response object:
        - Uses a sample input string
        - Provides a required session ID for memory context
        - Asserts that the response contains non-empty content
        """

        # Arrange: Sample input and config with session ID
        input_data = {"input": "Tell me a programming joke"}
        config = {"configurable": {"session_id": "test-session-001"}}

        # Act: Invoke the chatbot chain
        result = chatbot_chain.invoke(input_data, config=config)

        # Assert: The result must contain a non-empty content attribute
        self.assertTrue(hasattr(result, "content"))
        self.assertGreater(len(result.content), 0)

# Enables running this test file independently
if __name__ == "__main__":
    unittest.main()
