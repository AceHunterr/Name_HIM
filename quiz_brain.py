import random


class QuizBrain:
    def __init__(self, p_list):
        self.score = 0
        self.question_no = 0
        self.list_count = len(p_list)
        self.person_list = p_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        """Returns true if questions left"""
        return self.question_no < self.list_count

    def next_question(self) -> bool:
        """Get hold of the answer and the text and Returns the question text of the new question"""
        self.question_no += 1
        self.current_question = random.choice(self.person_list)
        self.p_name = self.current_question.name
        self.p_work = self.current_question.work
        self.person_list.remove(self.current_question)
        return self.p_work

    def check_answer(self, user_answer):
        """Returns True if answer is correct else False"""
        if user_answer == self.p_name:
            self.score += 1
            return True
        else:
            return False
