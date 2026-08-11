#sum program => a,b => sum
a=int(input("Enter an integer number: "))
b=float(input("Enter a decimal number: "))

sum=a + b #Type conversion (implicit)
print("sum is:", sum)

sum_2=(a+int(b)) #Type casting (explicit)
print("sum is:", sum_2)