
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
        #if len(number1) or len(number2) > 4:
        print(len(number1),len(number2))

correct_input(list)