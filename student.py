import pandas as pd
# 1 . Create Dataframe of 5 students
data = {
    "name": ["Ram" , "Shyam" , "Gita" , "Adarsh"],
    "score": [10 , 20 , 30 , 40]

}

df = pd.DataFrame(data)
#2 . Print highest score
top_score = df["score"].max()
print(f"Top Score is : {top_score}")
#3 . Add passed column and count passes
df["passed"] = df["score"] >= 20
num_passed = df["passed"].sum()
print(f"Passed:{num_passed}")