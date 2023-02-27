#write a program that calculates 16% tax on income ranging between 100k to 150k

#19% tax if income is between 150k to 300k
#30% tax if income is above 300k
#5% tax if income is less 100k

#print gross income and net income
'''
gross_income = int(input("enter your income:")) 
if (gross_income >= 100000)& (gross_income <= 150000):
    net_income = 0.84*int(gross_income)
    print("your net income is {} an d your gross income is {} 0".format(int(net_income),gross_income))

if(gross_income >=150000) & (gross_income <= 300000):
    net_income1 = 0.81*int(gross_income)
    print("your net income is {} and your gross income is {} 1".format(int(net_income1),gross_income))

if(gross_income >=300000):
    net_income2 = 0.7*int(gross_income)
    print("your net income is {} and your gross income is {} 2".format(int(net_income2),gross_income))

if(gross_income <= 100000) & (gross_income >= 1):
    net_income3 = 0.95*int(gross_income)
    print("your net income is {} and your gross income is {} 3".format(int(net_income3),gross_income))
'''
gross_income =int(input("enter your gross salary"))
tax_groupa = (gross_income*0.05)
tax_groupb = (gross_income*0.16)
tax_groupc = (gross_income*0.19)
tax_groupd = (gross_income*0.30)

if gross_income <= 100000:
    print("gross income",gross_income)
    print("taxa=",tax_groupa)
    print("net income",gross_income- tax_groupa)

elif (gross_income >100000) & (gross_income < 120000):
    print("gross income",gross_income)
    print("taxb=",tax_groupb)
    print("net income",gross_income- tax_groupb)

elif(gross_income > 150000) & (gross_income < 300000):
    print("gross income",gross_income)
    print("taxc=",tax_groupc)
    print("net income",gross_income -tax_groupc)

elif(gross_income > 1) & (gross_income < 100000):
     print("gross income",gross_income)
     print("taxd =",tax_groupd)
     print("net income",gross_income -tax_groupd)
