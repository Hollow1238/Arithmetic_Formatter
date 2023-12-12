def arithmetic_arranger(problems, answers=False):
  first_operand = []
  second_operand = []
  operator = []

  for problem in problems:
    components = problem.split()
    first_operand.append(components[0])
    second_operand.append(components[2])
    operator.append(components[1])

  # Checks len/number of problems
  if len(problems) > 5:
    return "Error: Too many problems."

  # Checks operator for + or -
  for symbol in operator:
    if symbol != '+' and symbol != '-':
      return 'Error: Operator must be ' '+' ' or ' '-' ' .'

  # Checks for only digits in operands
  for i in range(len(first_operand)):
    if first_operand[i].isdigit == False or second_operand[i].isdigit == False:
      return 'Error: Numbers must only contain digits.'

  # Checks operands length
  for i in range(len(first_operand)):
    if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
      return 'Error: Numbers cannot be more than four digits.'

  top_row = []
  bottom_row = []
  dashes = []
  answer_row = []

  for i in range(len(first_operand)):
    if len(first_operand) >= len(second_operand):
      dashes.append('-' * ((len(first_operand)) + 2))
      top_row.append(' ' * (len(dashes[i]) - len(first_operand[i])) +
                     first_operand[i])
      bottom_row.append(operator[i] + ' ' *
                        (len(dashes[i]) - len(second_operand[i]) - 1))
    else:
      dashes.append('-' * ((len(second_operand)) + 2))
      top_row.append(' ' * (len(dashes[i]) - len(first_operand[i])) +
                     first_operand[i])
      bottom_row.append(operator[i] + ' ' *
                        (len(dashes[i]) - len(second_operand[i]) - 1))

  for i in range(len(first_operand)):
    if operator[i] == '+':
      answer_row.append(int(first_operand[i]) + int(second_operand[i]))
    else:
      answer_row.append(int(first_operand[i]) - int(second_operand[i]))

  arranged_problems = '    '.join(top_row) + '\n' + '    '.join(
      bottom_row) + '\n' + '    '.join(dashes) + '\n'
  arranged_problems_solved = '    '.join(top_row) + '\n' + '    '.join(
      bottom_row) + '\n' + '    '.join(dashes) + '\n' + '    '.join(answer_row)

  if answers == True:
    return arranged_problems_solved
  else:
    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))