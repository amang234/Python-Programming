Num1 = int(input("Enter a Number: "))
Num2 = int(input("Enter another Number: "))

operator = input("Enter the operator: ")

match operator:
    case "+":
        print("Sum is",Num1+Num2)
    case "-":
        print("Difference is",Num1-Num2)
    case "*":
        print("Product is",Num1*Num2)
    case "//":
        print("Quotient is",Num1//Num2)
    case "/":
        print("Division is",Num1/Num2)
    case _:
        print("Enter a valid operator")