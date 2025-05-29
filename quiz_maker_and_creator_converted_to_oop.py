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
class Quiz:
    def __init__(self, filename):
        self.questions = self.load_questions(filename)
    
    def load_questions(self, filename):
        # load questions from a file
        questions = []
        with open(filename, 'r') as file:
            for line in file:
                question_text, correct_answer = line.strip().split(';')
                questions.append(Question(question_text, correct_answer))
        return questions
    
    def quiz_user(self):
        # conduct the quiz with the user
        question = random.choice(self.questions)
        print("Question: " + question.question_text)
        user_answer = input("Your answer: ")

        if question.check_answer(user_answer):
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is: {question.correct_answer}")

def main():
    quiz = Quiz('quiz_program.txt')  
    quiz.quiz_user()


if __name__ == "__main__":
    main()