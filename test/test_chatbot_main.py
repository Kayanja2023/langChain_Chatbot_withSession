import unittest
from chatbot import handle_query  # Function being tested

class TestChatbotCLI(unittest.TestCase):
    """
    Unit test for the chatbot's user query interface via handle_query().
    Verifies response structure and behavior.
    """

    def test_handle_query_returns_valid_response(self):
        """
        Sends a basic user input to the chatbot and verifies the response:
        - It must be a string
        - It should not be empty
        """
        # Act: Send input and receive response
        response = handle_query("What is artificial intelligence?", session_id="test-session-456")

        # Assert: Response must be a non-empty string
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

# Enables direct test execution from command line
if __name__ == "__main__":
    unittest.main()
