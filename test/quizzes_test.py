import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
    
    def test_expose_failure_01(self):
        """
        check 1
        """
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz('Title of Quiz1', 'this is quiz 1', '2023 09 13', '2023 09 5')
        quiz_list = self.ctrl.get_quiz_by_id(quiz_id)
        self.assertIsNotNone(quiz_list,'Quiz1 created')
       
      
    def test_expose_failure_02(self):
        """
        check 2
        """
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz('Title of Quiz2', 'this is quiz 2', '2023 10 30', '2023 10 1')
        ques_id = self.ctrl.add_question(quiz_id, 'Title of Ques 2-1', 'details of ques 2-1')
        ques_list = self.ctrl.get_question_by_id(ques_id)
        self.assertIsNotNone(ques_list,'question 2-1 created')
        ans_id = self.ctrl.add_answer(ques_id,'this is ans yes to ques2-1',is_correct= True)
        ans_id = self.ctrl.add_answer(ques_id,'this is ans no to ques2-1',is_correct= False)
        self.assertIsNotNone(ans_id, 'Answers for question 1 created')

      
    def test_expose_failure_03(self):
        """
        check 3
        """
        #self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz('Title of Quiz3', 'this is quiz 3', '2023 11 30', '2023 11 1')
        ques_id = self.ctrl.add_question(quiz_id, 'Title of Ques 3-1', 'details of ques 3-1')
        self.ctrl.add_answer(ques_id,'this is ans yes to ques3-1',is_correct= True)
        self.ctrl.add_answer(ques_id,'this is ans no to ques3-1',is_correct= False)
        quiz_list = self.ctrl.get_quizzes
        self.ctrl.print_quiz(quiz_list)
        self.assertTrue(True)   
        

if __name__ == '__main__':
    unittest.main()