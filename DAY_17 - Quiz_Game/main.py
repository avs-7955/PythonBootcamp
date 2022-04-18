from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(ques_bank=question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz...!!!!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
