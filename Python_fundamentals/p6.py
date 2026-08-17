#multiples of 3 from range 1 to 50 skipped 15
for i in range(1,51): 
    if(i==15):
        continue
    if(i%3==0):
        print(i)


#a and b two numbers find first number which is divisible by both in the range of 1 to 1000

a=int(input("enter a number: "))
b=int(input("enter a number: "))
for i in range(2,1000):
    if(a%i==0 and b%i==0):
        print(i)
        i+=1
        break
