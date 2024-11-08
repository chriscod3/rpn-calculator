# Name: Chris Atuti
# Student ID: 1001897232
# Submission Date: 11/08/2024
# Operating System: MacOS / Linux VE

import os


def evaluate_rpn(expression):
    stack = []
    for token in expression.strip().split():
        if token.isdigit():  # Token is a number
            stack.append(float(token))
        else:
            # Ensure there are at least two numbers to pop
            if len(stack) < 2:
                raise ValueError("Invalid RPN expression: not enough operands")

            num2 = stack.pop()
            num1 = stack.pop()

            # Perform the operation
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            elif token == '/':
                # Check for division by zero
                if num2 == 0:
                    raise ValueError("Division by zero")
                stack.append(num1 / num2)
            else:
                raise ValueError(f"Invalid operator: {token}")

    # Ensure there's exactly one item on the stack
    if len(stack) != 1:
        raise ValueError("Invalid RPN expression: too many operation")

    return stack[0]


def main():
    try:
        input_file = os.path.join(os.getcwd(), 'input_RPN.txt')

        # Check if file exists
        if not os.path.exists(input_file):
            print(f"Error: Cannot find input file at {input_file}")
            return

        # Read and process each line in the input file
        with open(input_file, 'r') as file:
            lines = file.readlines()

            # Check if file is empty
            if not lines:
                print("Error: input_RPN.txt is empty")
                return

            print("Processing expressions:")
            for i, line in enumerate(lines, 1):
                if line.strip():  # Only process non-empty lines
                    print(f"Expression {i}: {line.strip()}")
                    try:
                        result = evaluate_rpn(line)
                        print(f"Result {i}: {int(result) if result.is_integer() else result}")
                    except ValueError as e:
                        print(f"Error in expression {i}: {str(e)}")
                else:
                    print(f"Expression {i}: Empty line - skipping")
                print("-" * 40)

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()