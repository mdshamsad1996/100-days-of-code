from data import question_data;
from question_model import Question;
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))

quize = QuizBrain(question_bank)

while quize.still_has_a_question():
    quize.next_question()

print("You've completed the quiz")
print(f"Your final score was {quize.score}/{quize.question_number}")
