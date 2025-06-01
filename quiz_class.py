import random
  
class Quiz:
    def __init__(self, filename):
        self.questions = self.load_questions(filename)

    def load_questions(self, filename):
        questions = []
        with open(filename, 'r') as file:
            for line in file:
                if ';' in line:
                    question_text, correct_answer = line.strip().split(';')
                    questions.append(Question(question_text, correct_answer))
        return questions

    def quiz_user(self):
        score = 0
        total = len(self.questions)

        random.shuffle(self.questions)

        for question in self.questions:
            print("\nQuestion:", question.question_text)
            user_answer = input("Your answer: ")

            if question.check_answer(user_answer):
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect! The correct answer is: {question.correct_answer}")

        print(f"\n🎯 Quiz finished! Your score: {score}/{total}")