import pandas as pd

print(pd.__version__)

data = {
    "Name": ["Aditya", "Mithlesh", "Anita", "Adarsh"],
    "Age": [21, 36, 42, 18]
}

df = pd.DataFrame(data)

print(df)
print(df["Age"].mean())