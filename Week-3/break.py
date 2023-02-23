
num = 0
while (num < 10):
    print(num)
    if (num == 5):
        break
    print("breaking at five")
    num += 1


#write a program that solves quadratic equations y = -b +
#uing for loop draw a diamond,trangle,pascals trangle

#pascals triangle
'''
num = 1
while (num < 10):
    if (num == 10):
        break
    num +=1

    for x in range(0,10):
        print('1',num,"1")
        '''
        

import math

a = int(input("Enter the first coefficient: "))
b = int(input("Enter the second coefficient: "))
c = int(input("Enter the constant: "))
s1 = ((-b + math.sqrt(b*2 - 4*a*c))/(2*a))
s2 = math(-b - math.sqrt(b*2 - 4*a*c))/(2*a)
print("The answers for {}x*2 + {}x + {} are {} and {}.".format(a,b,c,s1,s2))
'''
#using a for loop draw a diamond
R = int(input("Enter the range: "))
for diamond in range(R):
    print("  " * (R - diamond), " *" * (2 * diamond +1))
for diamond in range(R-2,-1,-1):
    print("  " * (R - diamond), " *" * (2 * diamond +1))

print("-----------------------------------------")

#using a for loop draw a triangle
for diamond in range(R):
    print("  " * (R - diamond), " *" * (2 * diamond +1))

print("------------------------------------------")
'''


'''

#using a for loop draw pascals triangle
for i in range(1, R+1):
	for j in range(0, R-i+1):
		print(' ', end='')

	# first element is always 1
	C = 1
	for j in range(1, i+1):

		# first value in a line is always 1
		print(' ', C, sep='', end='')

		# using Binomial Coefficient
		C = C * (i - j) // j
	print()

'''
