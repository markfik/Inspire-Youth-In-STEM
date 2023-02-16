'''
sum = 0
for i in range(0,10):
    print(i)
    sum = sum + i 
    print(sum)
    product = 1
    for x in range(1,10):
        product = product * x
        print(product)

 #factorial.
 # 6! = 6*5*4*3*2*1
 # write a program to list all the odd numbers from  1-100 
 # write a program to list all the even numbers from 1-100   
 #write a program to list all the prime numbers from 1-100
#odd numbers
odd = 0
for d in range(0,100):
    num = odd != 2
    odd = num / d
    print(odd)
    # fing the difference between a compiler and interpreter.
    #write a program to list all odd numbers from 1-100
    '''
'''
print("***The values below are odd numbers***")
for odd_numbers in range(1,101):
    if(odd_numbers%2 != 0):
        print(odd_numbers)
'''

print("the numbers below are even numbers.")
for even_numbers in range(1,101):
    even_number = even_numbers%2 == 0
    print(even_number)
