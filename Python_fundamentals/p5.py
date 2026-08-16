#even/odd number
num= int(input("Enter a number: "))
if num%2==0:
    print("Even number")
else:
    print("Odd number")


#table of a number
num=int(input("Enter a number: "))
for i in range(1,11):
    p=num*i
    i+=1
    print(p)


#factorial of a number
p=1
num=int(input("Enter a number: "))
for i in range(1,num+1):
    p=p*i
    i+=1
print(p)


#reverse a string 
s=input("Enter a string: ")
reverse_s= s[::-1]
print(reverse_s)

