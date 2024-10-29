"""while loop- ends when a condition is reached
for loop
if else loop

print true and false.
"""
num=int(input("Enter a number: "))

while num < 10:
    print( num)
    if num==2:
        break
    print(f"we arrived at {num}")
    num+=1

