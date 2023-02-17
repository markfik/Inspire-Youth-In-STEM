#program to print the squares and cubes of numbers.
'''
for i in range(0,10):
    print("squares",i**2)


    print("-----------------------------------------------------------")
'''
'''
for x in range(0,10):
    print ("cubes",x **3) 

    
    print("------------------------------------------------------")
'''

    # y = 5x^3 + 2x^2 + 8x + 9
    #-----------------------------------

from tabulate import tabulate
head = (['X','solution'])
for x in range(0,10):
    diff = ("x:" +str(x) + "5x^3 + 2x^2 + 8x +9:",str(5*(x**3) + 2*(x**2) + 8*(x) + 9))
    my_table =(['mark','1'])

print(tabulate(diff,headers=head,tablefmt="grid"))

'''
for x in range(0,10):
    print(tabulate("x:"+str(x) +"5x^3 + 2x^2 + 8x + 9:",str(5*(x**3) + 2*(x**2) + 8*(x) + 9),tabletmt="grid"))

'''