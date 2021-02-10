from typing import List


def arithmetic_arranger(problems: List[str], show_result=False) -> str:
    # Check for correct number of problems
    if len(problems) > 5:
        return "Error: Too many problems."
    # Initiate variables for each row strings
    top_number_str, bottom_number_str, dash_str, result_str = "", "", "", ""
    # Iterate over each problems
    for problem in problems:
        top_number, operator, bottom_number = problem.split()
        top_number_len, bottom_number_len = len(top_number), len(bottom_number)
        # TODO: Make new function for input validation. def validate_input(problem)
        # Check if each operands are less or equal to four digits in width
        if top_number_len > 4 or bottom_number_len > 4:
            return "Error: Numbers cannot be more than four digits."
        # Check if both operands are digits
        if not top_number.isdigit() or not bottom_number.isdigit():
            return "Error: Numbers must only contain digits."
        # Check for appropriate operators
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        # Arrange the width of each column
        if top_number_len >= bottom_number_len:
            column_width = top_number_len + 2
        else:
            column_width = bottom_number_len + 2

        # Add columns to the string
        top_number_str += f'{top_number:>{column_width}}    '
        bottom_number_str += (f'{operator:<} '
                              f'{bottom_number:>{column_width - 2}}    '
                              )
        dash_str += f'{"-" * column_width:>{column_width}}    '
        # TODO: Make function def show_result(problem)
        if show_result:
            # Compute result
            if operator == "+":
                result = int(top_number) + int(bottom_number)
            else:
                result = int(top_number) - int(bottom_number)
            result_str += f'{result:>{column_width}}    '

    arranged_problems = (
        f'{top_number_str.rstrip()}\n'
        f'{bottom_number_str.rstrip()}\n'
        f'{dash_str.rstrip()}'
    )
    if show_result:
        arranged_problems += f'\n{result_str.rstrip()}'

    return arranged_problems
    