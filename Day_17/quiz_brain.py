class QuizBrain:

    def __init__(self, qs_list):
        self.question_no = 0
        self.question_list = qs_list
        self.score = 0

    def is_still_have_questions(self):
        return self.question_no != len(self.question_list)

    def next_question(self):
        curr_qs = self.question_list[self.question_no]
        self.question_no += 1
        user_ans = input(f"Q.{self.question_no} {curr_qs.text} (True/False) ? : ")
        self.check_answer(user_ans, curr_qs.answer)

    def check_answer(self,u_ans,c_ans):
        if u_ans.lower() == c_ans.lower():
            self.score+=1
            print("You got it right Buddy! ")
        else:
            print("Ohh noo. Its wrong buddy!")
        print(f"The correct answer is {c_ans}")
        print(f"Your current score is {self.score}/ {self.question_no}  \n")

