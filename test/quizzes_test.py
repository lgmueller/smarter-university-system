import unittest
from datetime import datetime

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
        self.ctrl.clear_data()
        qid = self.ctrl.add_quiz('quiz1', 'text', datetime(2023, 1, 13), datetime(2023, 10, 5))

        self.ctrl.add_question(qid, 'title', 'text')
        self.ctrl.print_quiz(qid)
        self.assertTrue(True, 'Example assertion.')

    def test_expose_failure_02(self):
        self.contr2 = QuizzesController
        self.assertTrue(True)

    def test_expose_failure_03(self):
        self.assertTrue(True)   
        

if __name__ == '__main__':
    unittest.main()