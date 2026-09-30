import pandas as pd
#1. define a raw data dictionary
data = {
    "Name" : ["Aditya" , "Mithlesh" , "Anita" , "Adarsh"],
    "City" : ["Gaur" , "KTM" , "Gaur" , "KTM"],
    "Fruit" : ["Mango" , "Apple" , "cherry" , "Banana"],
    "Age" : [21 , 36 , 42 , 18]
}
#2 . Create a structure data frame 
df = pd.DataFrame(data)
#3. print dataframe and compute age
print(df)
print(df["Age"].mean())
print(df["Age"].median())



#3 . Load CSV files
df = pd.read_csv("category_performance_summary.csv")
print(df.shape)