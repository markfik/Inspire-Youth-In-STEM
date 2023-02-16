names = ["mark", "john", "april", "jean", "sharon", "maryanne", "adrian","eunice"]
#accessing items in a list.
print(names)
print(names[0])
print(names[-1])
print(names[2])
print(names[0:3])
fruits =["mangoes", "oranges", "watermelon", "passion", "guava", "banana", "apples"]
print(fruits[3])
print(fruits[0:-1])
print("my favourite fruit is",fruits[1])
print("my favourite fruit is",fruits[1] . upper())
#adding two lists
vegetables =["kales","cabbage","spinach","managu","onions","carrots","brocolli"]
stationary = ["pens","ink","paper","glue","scissoers","stapler"]
shoppings = vegetables + stationary
print(shoppings)
print(shoppings[5])
for vegetable in vegetables:
    print(vegetable)
for shopping in shoppings:
    print(shopping)
print("my name is "+ names[0]+ " and my favourite fruit is "+fruits[2])
