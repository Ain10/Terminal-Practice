#Problem 1
num1, num2 = input("Enter 1st Number: "),input("Enter 2nd Number: ")
print(f"{num1} duplicated {num2} times is: {num1 * int(num2)}")

#Problem 2
height = int(input("Enter desired height: "))
print("+","="*10,"+\n",("+"+" "*10+"+\n")*(height-2), "+","="*10,"+",sep="")

#Problem 3
num1, num2 = input("Enter 1st Number: "),int(input("Enter 2nd Number: "))
print(f"The sum of all three numbers are {int(num1 * num2) + num2 + (num2 * 6)}.")

#Problem 4
firstnum, secondnum = int(input("Enter First Number: ")), float(input("Enter Second Number: "))
print("First Number: %.2f, Second Number: %d" % (firstnum, secondnum))
print(f"First Number: {firstnum:.2f}, Second Number: {secondnum:.0f}")

#Problem 5
separator = input("Input separator character/s: ")
ending = input("Input ending character/s: ")
print("I","love","Python", sep=separator*2, end=ending)
