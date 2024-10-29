#prgram to calculate the BMI
#weight/height in meters squared.

weight=int(input("Enter your weight in kgs: "))
height=float(input("Enter your height in m: "))

BMI=weight/height **2

print("Your BMI is", round(BMI, 2))