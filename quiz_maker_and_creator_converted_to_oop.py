import random

# create a class for questions
class Question:
    def __init__(self, question_text, correct_answer):
        self.question_text = question_text
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        # check if the user's answer is correct.
        return user_answer.strip().lower() == self.correct_answer.lower()
# create a class for quiz
# load questions from a file
# conduct the quiz with the user