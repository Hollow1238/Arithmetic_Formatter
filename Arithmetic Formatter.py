import math

list = ["32 + 698",'673 - 127']

acceptable = {'0','1','2','3','4','5','6','7','8','9','+','-',' '}
def correct_input(problems):
    if len(problems) > 5:
        print("Error: Too many problems.")
    for problem in problems:
        op_index = problem.index(' ') + 1
        operator = problem[op_index]
        if operator not in acceptable:
            print('Error: Operator must be ''+'' or ''-''.')
        for element in problem:
            if element not in acceptable:
                print('Error: Numbers must only contain digits.')
        number1 = problem[:op_index - 1]
        number2 = problem[op_index + 2:]
        if len(number1) > 4 or len(number2) > 4:
            print('Error: Numbers cannot be more than four digits.')

def calculations(problems):
    for problem in problems:
        op_index = problem.index(' ') + 1
        operator = problem[op_index]
        number1 = int(problem[:op_index - 1])
        number2 = int(problem[op_index + 2:])
        if operator == '-':
            sum = number1 - number2
        else:
            sum = number1 + number2
        return sum



#def formatting():



#def main(list):
    correct_input(list)



#main(list)

print(calculations(list))
how does github work