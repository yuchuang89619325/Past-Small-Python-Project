from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for Q in question_data:
   question_text = Q["question"]
   question_answer = Q["correct_answer"]
   new_question_object = Question(question_text, question_answer)
   question_bank.append(new_question_object)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You completed the quiz!")
print(f"The final score is: {quiz.score} / {quiz.question_number}.")


