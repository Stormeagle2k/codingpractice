#Write a calculator which must accept 3 imputs. The imputs are the first number,
#the operator, and the second number. The program should output the result of the calculation.
calculator = input("calculation")
calculator = int(calculator)
sign = input("what operator would you like to use")
calculator2 = input("What is the second number?")
calculator2 = int(calculator2)
if sign == "+":
    output = calculator + calculator2
elif sign == "-":
    output = calculator - calculator2
elif sign == "*":
    output = calculator * calculator2
elif sign == "/":
    output = calculator / calculator2
else:
    output = "You messed up"
print(output)
