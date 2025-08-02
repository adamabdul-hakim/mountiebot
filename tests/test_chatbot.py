import unittest
from mountiebot.chatbot import bot_response

class TestMountieBot(unittest.TestCase):

    def test_known_input(self):
        response = bot_response("What is Berea's motto?")
        self.assertIn("MountieBot:", response)

    def test_empty_input(self):
        response = bot_response("")
        self.assertIn("MountieBot:", response)
        self.assertIn("please type something", response.lower())

    def test_unknown_input(self):
        response = bot_response("blarp xyzzy qwerton")
        self.assertIn("MountieBot:", response)
        self.assertIn("i'm not sure", response.lower())


if __name__ == '__main__':
    unittest.main()
