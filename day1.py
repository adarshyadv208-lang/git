# case,  Whitespace ,  and Transformations
text = "Hello , World!"
print(text.upper()) # "HELLO, WORLD!"
print(text.strip()) # "Hello , World!"
print(text.replace("World " , "python")) # "Hello , Python! "

# Lists and Joining
words = text. strip().split(",") # [ 'Hello' , 'World!' ] 
print( ",".join(["apple", "banana"]
                  