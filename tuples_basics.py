#1 . Creation and types
fruits = ("apple" , "banana" , "cherry" , "dryfruit")
single = (10,) # comma required for single item 
mixed = ("Adarsh", 18 , "Developer")

#2 . Accessing and slicing
print(fruits[0], fruits[-1]) #apple , dryfruit
print(fruits[0:2])#apple , banana

#3.Unpacking
name , age , role = mixed
print(f"{name} is {age} as {role}")

#4 . operations and methods
nums = (4 , 2, 7 , 2)
print("Count of 2 :", nums.count(2)) #2
combined = fruits + ("Mango",) 
print("Total items : ", len(combined)) #5

#5 . Nested Tuples
nested = ("point" , (3 , 4))
print("X:", nested[1][0])





