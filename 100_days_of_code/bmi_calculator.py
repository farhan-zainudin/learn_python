# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# print(type(height))
# print(type(weight))

bmi = int(weight) / float(height)**2
# bmi = int(weight) / (float(height) * float(height))

print(int(bmi))
