# Problem 1
digit7=[["###","#","###","###","# #","###","###","###","###","###"],
        ["# #","#","  #","  #","# #","#  ","#  ","  #","# #","# #"],
        ["# #","#","###","###","###","###","###","  #","###","###"],
        ["# #","#","#  ","  #","  #","  #","# #","  #","# #","  #"],
        ["###","#","###","###","  #","###","###","  #","###","  #"]]
isValid=False
while(not isValid):
    number= input("Enter a number: ")
    if(number.isdigit() and int(number) >= 0):
        isValid = True
    else:
        print("Invalid input. ",end="")
for firstIndex in range(0,5):
    for secondIndex in number:
        print(digit7[firstIndex][int(secondIndex)], end=" ")
    print()

# Problem 2
isValid=False
#! CONDITIONS
while(not isValid):
    cipher = input("Please select [0]Cipher/[1]Decipher: ")
    if(cipher.isdigit() and cipher == "0" or cipher == "1"):
        isValid = True
    else:
        print("Invalid option. ",end=" ")
while(isValid):
    shift = input("Enter the number of shift (1-25): ")
    if(cipher.isdigit() and int(shift) > 0 and int(shift) < 26):
        isValid = False
    else:
        print("Invalid Shift. ",end=" ")
message = input("Enter the message: ")
cipheredMessage=""
# small character 97-122
# big characters 65-90
if(cipher=="0"):
    for i in message:
        if(not i.isalpha()):
            cipheredMessage+=i
            continue
        if(ord(i.upper())+int(shift))>= 91:
            cipheredMessage+=chr(ord(i.upper())+int(shift)-26)
            continue
        cipheredMessage+=chr(ord(i.upper())+int(shift))   
else:
    for i in message:
        if(not i.isalpha()):
            cipheredMessage+=i
            continue
        if(ord(i.upper())+int(shift))<= 65:
            cipheredMessage+=chr(ord(i.upper())-int(shift)+26)
            continue
        cipheredMessage+=chr(ord(i.upper())-int(shift))           
print(cipheredMessage)

# Problem 3
inp = input("Enter Word/s: ")
if(inp.lower().replace(" ", "") == inp.lower().replace(" ", "")[::-1] and inp != "" and inp != " "):
    print("It's a palindrome")
else:
    print("It's not a palindrome")

# Problem 4
firstInp, secondInp = input("Enter First String: "), input("Enter Second String: ")
first, second = sorted(firstInp.lower().replace(" ", "")), sorted(secondInp.lower().replace(" ", ""))
if(first == second):
    print("Anagrams")
else:
    print("Not anagrams")

# Problem 5
isValid=False
while(not isValid):
    inp = input("Enter Birthday: ")
    if(inp.isdigit() and len(inp) == 8 and int(inp)>0):
        isValid=True
    else:
        print("Invalid Birthday.",end=" ")
while(len(inp)!=1):
    sum = 0
    for i in inp:
        sum += int(i)
    inp=str(sum)
print(f"Digit of life is: {inp}")




