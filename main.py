# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
t = lower_case_name1.count("t") +lower_case_name2.count("t")
r = lower_case_name1.count("r") + lower_case_name2.count("r")
u = lower_case_name1.count("u") +lower_case_name2.count("u")
ee = lower_case_name1.count("e") + lower_case_name2.count("e")

true_total = t+r+u+ee

l = lower_case_name1.count("l") + lower_case_name2.count("l")
o = lower_case_name1.count("o") + lower_case_name2.count("o")
v = lower_case_name1.count("v") + lower_case_name2.count("v")
e = lower_case_name1.count("e") + lower_case_name2.count("e")

love_total = l + o + v + e 

total_score= str(true_total)+ str(love_total)

total_as_int= int(total_score)

if total_as_int < 10 or total_as_int> 90: 
    print(f"Your score is {total_as_int}, you go together like coke and mentos.")

elif   40 < total_as_int < 50 :
    print(f"Your score is {total_as_int}, you are alright together.")

else :
    print(f"Your score is {total_as_int}.")

