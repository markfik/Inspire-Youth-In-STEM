#write a program that calculates 16% tax on income ranging between 100k to 150k

#19% tax if income is between 150k to 300k
#30% tax if income is above 300k
#5% tax if income is less 100k

#print gross income and net income

income = input("enter your net income")
if income == '100,150':
    print("your average!",(0.84*int(income)))
elif income =='150,300':
    print("your medium!",(0.81*int(income)))

elif income =='300,1000':
    print("your rich!",(0.7*int(income)))

else:
    print("your poor!")
    
'''
season = 'winter'
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')
'''

