#Difference between print and return
#print
def add(a , b):
    print(a + b)

result = add(5 , 3)
print(result) 
#8 
#none
#why none because print display 8 but function don't return anything

#return
def add(a , b):
    return(a + b)

result = add(5 , 3)
print(result)

