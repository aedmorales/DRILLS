import pandas as pd  
import random as r

df = pd.read_csv ("table1.csv").dropna()
df.insert(0, "ID", [i for i in range(len(df.index))])
df["Date"] = "META-" + df["Date"]
df.insert(2, "Dummy", [r.randint(0,1) for _ in range(len(df.index))])
print(df)

df.to_csv("table2.csv")  