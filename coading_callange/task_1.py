#-------------------------------------------------------------------------#
#   scripted on Jun 2, 2022                                               |
#   by, Nabin Paudel                                                      |
#-------------------------------------------------------------------------#


def calculate(x, y, op):
    """actuall calculation happens here"""
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y
    elif op == "mod":
        result = x % y
    elif op == "power":
        result = x**y

    print("Your result is:", result)


def display_operators_info(x, y):
    """displays operators option to user"""
    print(f""" 
        '+' to add {x} and {y}
        '-' to subtract {y} from {x}
        '*' to multiply {x} by {y}
        '/' to divide {x} by {y}
        'mod' to get reminder after division of {x} by {y}
        'power' to get product after {x} to the power {y}
            """)


def main():
    print("\n"+"====="*5)

    inp_x = int(input("Enter the first number:"))  # input 1
    inp_y = int(input("Enter the second number:"))  # input 2

    print("Enter a operator accordingly:-")

    display_operators_info(inp_x, inp_y)  # function call <-

    inp_op = input("\nOperator:")  # input 3

    calculate(inp_x, inp_y, inp_op)  # function call <-


if __name__ == "__main__":
    main()
