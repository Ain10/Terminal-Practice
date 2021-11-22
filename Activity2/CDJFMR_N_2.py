# Problem 1
char, num = input("Enter a character: "), int(input("Enter a number: "))
for i in range(1, num):
    print(i * char)
for i in range(num, 0, -1):
    print(i * char)

# Problem 2
num = int(input("Enter a number: "))
ans = 0
for i in range(num):
    ans += (i ** 3)
print(f"The sum of all cubes is {ans}.")

# Problem 3
num = int(input("Enter a number: "))
ans = 1
for i in range(1, num):
    if(num <= 0):
        break
    for j in range(1, i+1):
        print(ans, end="")
        ans += 1
        num -= 1
        if(num <= 0):
            break
    print()

# Problem 4
num, odd, avg = "a", 0, 0
while(num != 0):
    num = int(input(f"Enter a number, 0 to exit: "))
    if(num % 2 == 1):
        odd += num
        avg += 1
print(f"The sum of all odd numbers is {odd}.")
print(f"The average of all odd numbers is {odd/avg}.")
print(f"The square root of the sum of all odd numbers is {odd**0.5:.2f}.")

# Problem 5
num, rows = int(input("Enter a number: "))+1, 0
for i in range(1, num):
    if(i < num):
        rows += 1
        num -= i
print(f"The height of the pyramid is {rows}.")
