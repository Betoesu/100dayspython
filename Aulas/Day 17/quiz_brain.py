class Quiz:
    def __init__(self, list):
       self.number = 0
       self.list = list
       self.score = 0

    def still_has_questions(self):
        return self.number < len(self.list)
            
    def next_question(self):
        current_question = self.list[self.number]
        self.number += 1
        player_answer = input(f"Q.{self.number}: {current_question.text} (True/False)?: ")
        self.check_answer(current_question.answer,player_answer)

    def check_answer(self,correct_answer,player_answer):
        if player_answer.lower() == correct_answer.lower():    
            print("You got ir right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}")
        print(f"Your corrent score is: {self.score}/{self.number}\n")
