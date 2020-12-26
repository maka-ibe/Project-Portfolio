class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        q_num = self.question_number
        q_list = self.question_list
        current_question = q_list[q_num]
        user_answer: str = input(f"Q.1: {current_question.text} (True/False)?")
        return user_answer
