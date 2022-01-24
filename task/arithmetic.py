import random


class Calculator:

    def __init__(self):
        self.x = None
        self.y = None
        self.z = None
        self.sign = None
        self.answer = None
        self.dlevel = None
        self.dlevel_descr = {1: "simple operations with numbers 2-9", 2: "integral squares of 11-29"}
        self.n_right = 0
        self.n_all = 0

    def select_difficulty(self):
        while True:
            print("Which level do you want? Enter a number:")
            print("1 - simple operations with numbers 2-9")
            print("2 - integral squares of 11-29")
            level = input()
            if level.isdigit() and int(level) in [1, 2]:
                self.dlevel = int(level)
                break
            else:
                print("Incorrect format.")

    def generate_data(self):
        if self.dlevel == 1:
            self.x = random.randint(2, 9)
            self.y = random.randint(2, 9)
            self.sign = random.choice("+-*")
        elif self.dlevel == 2:
            self.z = random.randint(11, 29)
            self.sign = '^'

    def make_operation(self):
        if self.sign == "+":
            return self.x + self.y
        elif self.sign == "-":
            return self.x - self.y
        elif self.sign == "*":
            return self.x * self.y
        elif self.sign == "^":
            return self.z ** 2

    def get_answer(self):
        while True:
            answer = input()
            if answer.lstrip('-').isdigit():
                self.answer = int(answer)
                break
            else:
                print("Incorrect format.")

    def check_answer(self):
        result = self.make_operation()
        if self.answer == result:
            print("Right!")
            self.n_right += 1
            self.n_all += 1
        else:
            print("Wrong!")
            self.n_all += 1

    def result_output(self):
        str_1 = f"Your mark is {self.n_right}/5."
        print(str_1)

    def save_result(self):
        str_2 = "Would you like to save the result? Enter yes or no."
        print(str_2)
        choice = input()
        if choice in ['yes', 'YES', 'y', 'Yes']:
            username = input("What is your name?\n")
            with open("results.txt", "a", encoding="UTF-8") as file:
                line = f"{username}: {self.n_right}/5 in level {self.dlevel} ({self.dlevel_descr[self.dlevel]})."
                file.write(line)
            print("The results are saved in 'results.txt'.")


def main():
    my_calc = Calculator()
    my_calc.select_difficulty()
    while my_calc.n_all < 5:
        my_calc.generate_data()
        if my_calc.dlevel == 1:
            print(my_calc.x, my_calc.sign, my_calc.y, sep=' ')
        elif my_calc.dlevel == 2:
            print(my_calc.z)
        my_calc.get_answer()
        my_calc.check_answer()
    my_calc.result_output()
    my_calc.save_result()


if __name__ == '__main__':
    main()
