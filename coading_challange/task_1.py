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

    result =  "{:.2f}".format(result)

    print(f"{x} {op} {y} = {result}")



def display_operators_info():
    """displays operators option to user"""
    print(f""" 
        '+' to add 
        '-' to subtract 
        '*' to multiply
        '/' to divide 
        'mod' to get reminder
        'power' to product of power
            """)


def main():
    print("\n"+"====="*5)
    display_operators_info()  # function call <-

    inp_op = input("\nSelect an Operator:")  # input 3
    
    inp_x = int(input("Enter the first number:"))  # input 1
    inp_y = int(input("Enter the second number:"))  # input 2

    print("Enter a operator accordingly:-")


    calculate(inp_x, inp_y, inp_op)  # function call <-


if __name__ == "__main__":
    main()
