# -------------------------------------
# PYTHON BASICS PRACTICE PROGRAM
# -------------------------------------

def main():

    # 1. Variables and Data Types
    name = "Pooja"
    age = 28
    height = 5.3
    is_learning_python = True

    print("Name:", name)
    print("Age:", age)
    print("Height:", height)
    print("Learning Python:", is_learning_python)

    # 2. Python Character Set (Strings)
    greeting = "Hello Python!"
    print("Greeting message:", greeting)

    # 3. Memory Concept
    x = 10
    y = x
    print("Value of x:", x)
    print("Value of y:", y)

    # 4. Type Function
    print("Type of name:", type(name))
    print("Type of age:", type(age))
    print("Type of height:", type(height))
    print("Type of is_learning_python:", type(is_learning_python))

    # 5. Expressions and Execution
    a = 10
    b = 3

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division a / b:", a / b)
    print("Floor Division a // b:", a // b)

    # 6. String Expressions
    text = "Hi "
    print("String repetition:", text * 3)

    first_name = "Pooja"
    last_name = "Thupakula"
    full_name = first_name + " " + last_name
    print("Full Name:", full_name)

    print("Repeat example:", "Python " * 4)

    # 7. Keywords Example
    number = 8

    if number > 5:
        print("Number is greater than 5")
    else:
        print("Number is small")

    # 8. Identifier Naming Rules
    student_name = "Rahul"
    _marks = 90
    totalMarks = 100

    print(student_name, _marks, totalMarks)

    # 9. Operators with Negative Numbers

    num1 = -10
    num2 = 3
    num3 = -3

    print("Negative numerator division:", num1 / num2)
    print("Negative numerator floor division:", num1 // num2)

    print("Negative denominator division:", 10 / num3)
    print("Negative denominator floor division:", 10 // num3)

    print("Both negative division:", num1 / num3)
    print("Both negative floor division:", num1 // num3)


# Program entry point
if __name__ == "__main__":
    main()