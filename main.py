import calculator

selection = int(input("\nSelect your calculator operation: \
                       \n1. Addition \
                       \n2. Subtraction \
                       \n3. Multiplication \
                       \n4. Division \n"))

num1 = int(input("\nProvide your first value: "))
num2 = int(input("\nProvide your second value: "))

if selection == 1:
    print(calculator.add(num1,num2))

if selection == 2:
    print(calculator.subtract(num1,num2))

if selection == 3:
    print(calculator.multiply(num1, num2))

if selection == 4:
    print(calculator.divide(num1,num2))
