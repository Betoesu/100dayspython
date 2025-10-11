from question_model import Text
from data import question_data
from quiz_brain import Quiz
question_bank = []
for q in question_data:
    question = q["question"]
    answer = (q["correct_answer"])
    new_question = Text(question,answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
print("You've got completed the quizz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")