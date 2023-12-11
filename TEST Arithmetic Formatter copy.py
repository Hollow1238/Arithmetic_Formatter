import math

list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def get_equation_elements(equation_string):
    first_number = str(equation_string[:equation_string.index(' ')])
    second_number = str(equation_string[equation_string.index(' ') + 3:])
    operator = equation_string[equation_string.index(' ') + 1]
    return first_number , second_number , operator

def correct_input(problems):
    acceptable = ('0','1','2','3','4','5','6','7','8','9','+','-',' ')

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
        
def formatting(problems,show_answers):
    top = []
    bottom = []
    dashes = []
    answers = []
    buffer_1 = []
    buffer_2 = []
    buffer_3 = []
    for problem in problems:
        elements_of_equation = get_equation_elements(problem)
        answers.append(str(calculations(problem)))
        length_num1 = len(elements_of_equation[0])
        length_num2 = len(elements_of_equation[1])
        operator = elements_of_equation[2]

        if length_num1 >= length_num2:
           dashes.append('-'*(length_num1 + 2))
           buffer_1.append(' ' * 2 )
           buffer_2.append(operator + ' ' *(length_num1 - length_num2 + 1) )
        else:
            dashes.append('-'*(length_num2 + 2))
            buffer_1.append(' ' * (length_num2 - length_num1 + 2))
            buffer_2.append(operator + ' ')
        


        top.append(elements_of_equation[0])
        bottom.append(elements_of_equation[1])
        for i in range(len(dashes)-1):
            buffer_3.append(' ' * (len(dashes[i]) - len(str((calculations(problem))))))

    for i in range(len(top)):
        top[i] = buffer_1[i] + top[i]

    for i in range(len(bottom)):
        bottom[i] = buffer_2[i] + bottom[i]

    for i in range(len(answers)):
        answers[i] = buffer_3[i] + answers [i]
'''
    print(answers)
    if show_answers == True:
        print(
        '    '.join(top) + '\n' + 
        '    '.join(bottom) + '\n' + 
        '    '.join(dashes) + '\n' +
        '    '.join(answers)
        )
    else:
        print(
            '    '.join(top) + '\n' + 
            '    '.join(bottom) + '\n' + 
            '    '.join(dashes)
        )
'''
def main(problems,show_answers):
    correct_input(problems)

#main(list)

def test(problems, boolean):
    formatting(problems, boolean)

test(list, True)