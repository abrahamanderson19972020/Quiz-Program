
class QuizBrain:
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_number = 0
        self.user_score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}: (True/False) >>>")
        self.check_answer(user_answer,current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it. Your answer is correct.")
            self.user_score += 1
        else:
            print("Your answer is wrong!")
        print(f"Correct answer is {correct_answer}")
        print(f"Your current score is {self.user_score}/{self.question_number}")
        print("\n")
        if self.question_number == len(self.question_list):
            print("You have completed the Quiz")
            print(f"Your final score is {self.user_score}/{self.question_number}")


