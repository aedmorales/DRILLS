import pandas as pd  
import random as r

df.insert(0, "ID", [i for i in range(len(df.index))])
df["Date"] = "META-" + df["Date"]
