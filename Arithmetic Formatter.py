import math

list = ["32 + 698",'673 - 127']

def get_equation_elements(equation_string):

    first_number = int(equation_string[:equation_string.index(' ')])

    second_number = int(equation_string[equation_string.index(' ', equation_string.index(' ') + 1 ):])

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
        
        


#def formatting():



def main(problems):
    correct_input(problems)
    for problem in problems:
        calculations(problem)



#main(list)

