import random
from question_model import Question
from quiz_brain import QuizBrain
from quiz_data import question_data, question_data_api

question_bank = []


for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

for question in question_data_api:
    question_bank.append(Question(question['question'], question['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!!!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
