import unittest
from my_program import make_it_uppercase, get_first_word

class TestMyProgram(unittest.TestCase):
    def test_hello_world(self):
        result = make_it_uppercase("hello world")
        self.assertEqual(result, "HELLO WORLD")

    def test_first_word(self):
       sentence = "is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but al"
       result = get_first_word(sentence)
       self.assertEqual(result, 'is')
       
if __name__ == '__main__':
  unittest.main()

