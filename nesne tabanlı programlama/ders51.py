# Question
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def check_answer(self, answer):
        return self.answer == answer

# Ouiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_question(self):
        return self.questions[self.question_index]
    
    def display_question(self):
        question = self.get_question()
        print(f"Soru {self.question_index + 1}: {question.text}")

        for q in question.choices:
            print("-"+ q)

        answer = input("Cevap :")
        self.guess(answer)
        self.load_Question()

    def guess(self, answer):
        question = self.get_question()

        if question.check_answer(answer):
            self.score += 1
        self.question_index += 1

    def load_Question(self):
        if len(self.questions) == self.question_index:
            self.show_score()
        else:
            self.display_progress()
            self.display_question()

    def show_score(self):
        print("Score :", self.score)

    def display_progress(self):
        total_question = len(self.questions)
        question_number = self.question_index + 1

        if question_number > total_question:
            print("Quiz bitti")
        else:
            print(f"Question {question_number} of {total_question}".center(100,"*"))

q1 = Question("En iyi programlama dili hangisidir ?", ["C#", "Python", "Java", "Javascript"], "Python")
q2 = Question("En popüler programlama dili hangisidir ?", ["C#", "Java", "Javascript", "Python"], "Python")
q3 = Question("En çok kazandıran programlama dili hangisidir ?", ["Java", "C#", "Python", "Javascript"], "Python")
q4 = Question("En çok sevilen programlama dili hangisidir ?", ["Java", "C#", "Python", "Javascript"], "Python")
q5 = Question("En kolay programlama dili hangisidir ?", ["Java", "C#", "Python", "Javascript"], "Python")
questions =[q1,q2,q3,q4,q5]
quiz = Quiz(questions)
quiz.load_Question()
# question =quiz.get_question
# print(question.text)
# print(q1.check_answer("Python"))
# print(q2.check_answer("C#"))