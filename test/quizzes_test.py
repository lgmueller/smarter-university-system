import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        self.assertTrue(True, 'Example assertion.')

    def test_expose_failure_02(self):
        self.assertTrue(False)

    def test_expose_failure_03(self):
        self.assertTrue(False)   
        

if __name__ == '__main__':
    unittest.main()