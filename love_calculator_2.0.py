# PROTOTYPE
# a = 'chukwu ikechukwu john'
# b = 'amarachi solace anyanwu'
# c = a + b
# t = 0
# m = 0
#
# for letter in c:
#     if letter == "t" or letter == "r" or letter == "u" or letter == "e":
#         t += 1
# for letter in c:
#     if letter == "l" or letter == "o" or letter == "v" or letter == "e":
#         m += 1
# print(f"{t}{m}%")

# MAIN LOVE CALCULATOR CODE

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is your name? \n").lower()

name_sum = name1 + name2
true = name_sum.count('t') + name_sum.count('r') + name_sum.count('u') + name_sum.count('e')
love = name_sum.count('l') + name_sum.count('o') + name_sum.count('v') + name_sum.count('e')

true_love = int(str(true) + str(love))

if (true_love < 10) or (true_love > 90):
    print(f"Your score is {true_love}, you go together like bread and tea.")
elif (true_love >= 40) and (true_love <= 50):
    print(f"Your score is {true_love}, you are alright together")
else:
    print(f"Your score is {true_love}.")


