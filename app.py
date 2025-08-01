from calc_func import do_addition, do_subtraction, do_division
from multiply import do_multiplication


def main():
    print("Welcome to the Calculator App!")
    # Additional code for the calculator functionality goes here
    """
    Select the function from given options:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    """
    input_choice = input("Please enter your choice (1 or 2 or 3 or 4): ")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if input_choice == '1':
        result = do_addition(a, b)
    elif input_choice == '2':
        result = do_subtraction(a, b)
    elif input_choice == '3':
        result = do_multiplication(a, b)
    elif input_choice == '4':
        result = do_division(a, b)
    else:
        print("Invalid choice")
        return
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
