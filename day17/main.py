from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for q in question_data:
    text = q['text']
    answer = q['answer']
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")