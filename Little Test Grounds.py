

list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def get_equation_elements(equation_string):
    first_number = str(equation_string[:equation_string.index(' ')])
    second_number = str(equation_string[equation_string.index(' ') + 3:])
    operator = equation_string[equation_string.index(' ') + 1]
    return first_number , second_number , operator

def formatting(problems):
    top = []
    bottom = []
    dashes = []
    for problem in problems:
        elements_of_equation = get_equation_elements(problem)
        top.append(elements_of_equation[0])
        bottom.append(elements_of_equation[1])
        length_num1 = len(elements_of_equation[0])
        length_num2 = len(elements_of_equation[1])
        operator = elements_of_equation[2]
        if length_num1 >= length_num2:
           dashes.append('-'*(length_num1 + 2))
        else:
            dashes.append('-'*(length_num2 + 2))
        

    print(
        '    '.join(top) + '\n' + 
        '    '.join(bottom)  + '\n' + 
        '    '.join(dashes)

    )

def test(problems):
    Re_Format(problems)



def Re_Format(problems):
    top = []
    bottom = []
    dashes = []
    buffer_1 = []
    buffer_2 = []
    for problem in problems:
        elements_of_equation = get_equation_elements(problem)
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
    for i in range(len(top)):
        top[i] = buffer_1[i] + top[i]
    for i in range(len(bottom)):
        bottom[i] = buffer_2[i] + bottom[i]

    print(
        '    '.join(top) + '\n' + 
        '    '.join(bottom) + '\n' + 
        '    '.join(dashes)


    )
    
    
       
test(list)