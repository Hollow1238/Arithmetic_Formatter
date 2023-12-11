import math

list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def get_equation_elements(equation_string):
    first_number = str(equation_string[:equation_string.index(' ')])
    second_number = str(equation_string[equation_string.index(' ', equation_string.index(' ') + 1 ):])
    operator = equation_string[equation_string.index(' ') + 1]

    return first_number , second_number , operator

def correct_input(problems):
    acceptable = {'0','1','2','3','4','5','6','7','8','9','+','-',' '}

    if len(problems) > 5:
        print("Error: Too many problems.")
        quit()

    for problem in problems:
        operator_index = problem.index(' ') + 1
        operator = problem[operator_index]

        if operator not in acceptable:
            print('Error: Operator must be ''+'' or ''-''.')
            quit()

        for element in problem:

            if element not in acceptable:
                print('Error: Numbers must only contain digits.')
                quit()

        number1 = problem[:operator_index - 1]
        number2 = problem[operator_index + 2:]

        if len(number1) > 4 or len(number2) > 4:
            print('Error: Numbers cannot be more than four digits.')
            quit()
        
def calculations(problem):
    elements_of_equation = get_equation_elements(problem)
    if elements_of_equation[2] == '+':
       sum = int(elements_of_equation[0]) + int(elements_of_equation[1])
    else:
       sum = int(elements_of_equation[0]) - int(elements_of_equation[1])
    return sum
        
def formatting(problem):
    elements_of_equation = get_equation_elements(problem)
    length_num1 = len(elements_of_equation[0])
    length_num2 = len(elements_of_equation[1])
    operator = elements_of_equation[2]
    num_of_dashes = 0
    if length_num1 >= length_num2:
        num_of_dashes = length_num1
    else:
        num_of_dashes = length_num2
    print('-'*(num_of_dashes + 2),length_num1,length_num2)
    




def main(problems,show_answers):
    correct_input(problems)
    for problem in problems:
        print(calculations(problem))



#main(list)

def test(problems):
    for problem in problems:
        formatting(problem)

test(list)