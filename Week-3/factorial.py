'''
def factorial(i):
    for x in range(1,i+1):
        i *=x
        print(i)

factorial(int(input("enter the number:")))

factorial(input("enter the number"))
#write a program to calculate the simple interest
def simple_interest(p,r,t):
    simple_interest =(p*(r/100)*t)
    print(simple_interest)

simple_interest(2000,12,5)

#factorial of (n)
def factorial(n):
    if n < 0:
        print("No factorial for negative numbers")
    else:
        return n * factorial(n-1)
        
num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
'''
'''
start_num = 1200
count_by = 4
end_num = 144
break_num = start_num
while break_num<end_num:
    result =break_num +count_by

else:
    result =("Oops! Looks like your start value is greater than the end value. Please try again.")

print(result)
'''
'''
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
index = 0
for headline in headlines:
        news_ticker =headline[index] + " "
        if len(news_ticker) >= 140:
                break
        print("the headline is 140 characters")
        
        elif(len(news_ticker) + len(headline[index] ))
'''