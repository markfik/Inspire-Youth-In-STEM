
def factorial(n):
    for i in range(0,n):
        m = reversed(i)
        fact_n = (n*(n-m))
        print(fact_n)

factorial(4)
'''
#write a program to calculate the simple interest
p = input("enter the principal amount:")
r =input("enter the rate:")
t =input("enter the time duration:")
simple_interest = int(p)*int(r)*int(t)
print("The simple interest is",simple_interest)'''