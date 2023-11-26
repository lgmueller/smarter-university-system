import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
    
    def test_expose_failure_01(self):
        '''
        Error in generation of quiz ID because system is not able to convert the input datatype 
        (Ex. none, bool, any other type) into string 
        '''
        self.ctrl.clear_data()
        # this will fail at line 63 in quizzes_controller.py, Causes type error
        quiz_id = self.ctrl.add_quiz(None, 'this is quiz 1', '2023 09 13', '2023 09 5')
        self.assertIsNone(quiz_id,'Quiz id cannot be generated as None type cannot be converted to string')
       
      
    def test_expose_failure_02(self):
        """
        Function call input arguments missing 
        """
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz('Title of Quiz2', 'this is quiz 2', '2023 10 30', '2023 10 1')
        # this will fail at line 29 in quizzes_test.py, causes TypeError in QuizzesController.add_question()
        ques_id = self.ctrl.add_question(quiz_id, 'Title of Ques 2-1')
        ans_id = self.ctrl.add_answer(ques_id,'this is ans yes to ques2-1',is_correct=True)
        self.assertIsNone(ans_id, 'Answers are not created, too many arguments')

      
    def test_expose_failure_03(self):
        '''
        Function call input arguments extra
        '''
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz('Title of Quiz3', 'this is quiz 3', '2023 11 30', '2023 11 1')
        ques_id = self.ctrl.add_question(quiz_id, 'Title of Ques 3-1', 'details of ques 3-1')
        # this fails at line 42 in quizzes_test.py, causes TypeError in QuizzesController.add_answer()
        self.ctrl.add_answer(ques_id,'this is ans yes to ques3-1', None, None)

if __name__ == '__main__':
    unittest.main()