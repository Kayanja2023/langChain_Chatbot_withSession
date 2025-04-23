import unittest
from langchain.prompts import PromptTemplate
from prompts.templates import get_prompt  # Function under test

class TestPromptTemplate(unittest.TestCase):
    """
    Unit tests for validating the LangChain prompt template generated
    by the get_prompt() function.
    """

    def test_prompt_structure(self):
        """
        Ensures the prompt returned by get_prompt():
        - Is a valid PromptTemplate object
        - Declares required input variables: 'history' and 'input'
        - Contains dialogue-like placeholders and labeling
        """

        # Act: Retrieve the prompt object
        prompt = get_prompt()

        # Assert: Confirm prompt type
        self.assertIsInstance(prompt, PromptTemplate)

        # Assert: Validate declared input variables
        self.assertIn("history", prompt.input_variables)
        self.assertIn("input", prompt.input_variables)

        # Assert: Check placeholder usage within the template
        self.assertIn("{history}", prompt.template)
        self.assertIn("{input}", prompt.template)

        # Assert: Simulated chat format (labels)
        self.assertIn("AI:", prompt.template)
        self.assertIn("Human:", prompt.template)

# Enables standalone execution of this test
if __name__ == "__main__":
    unittest.main()
