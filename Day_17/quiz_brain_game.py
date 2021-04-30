from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for k in question_data:
    q_text = k["text"]
    q_ans = k["answer"]
    question_bank.append(Question(q_text,q_ans))

quiz = QuizBrain(question_bank)
while quiz.is_still_have_questions():
    quiz.next_question()

print("Hurray ! You have completed the Game !")
print(f"Your final score is {quiz.score} / {len(quiz.question_list)}")