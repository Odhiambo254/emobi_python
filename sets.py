#program to check student performance.

marks=int(input("Enter your marks: "))

#loop
if 100 >= marks >= 80:
    print("you have an A")
elif  79 >= marks >=60:
    print("you have an B")
elif marks <=59 and marks>=40:
    print("you have an C")
elif marks <=39 and marks>=0:
    print("you have an D")
else:
    print("you have an F")
