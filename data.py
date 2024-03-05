import pandas as pd
import datetime as dt
import numpy as np

def superstore():

    df = pd.read_csv("Orders.csv", encoding='latin-1')



    df['Order Date'] = pd.to_datetime(df["Order Date"])

    df['Ship Date'] = pd.to_datetime(df["Ship Date"])


    #print(df["Ship Days"].tail(8))

    df["Revenue"] = df["Sales"] * df["Quantity"]



    df["Margin"] = 100 * ((df["Revenue"] - df["Sales"]) / df["Revenue"])



    df['Ship Days'] = (df['Ship Date'] - df['Order Date'])/ np.timedelta64(1, 'D')

    df['Ship Days'] = df['Ship Days'].fillna("Order incomplete")



    ret = pd.read_csv("Returns.csv")

    df["Order Returned"] = "No"

    r = ret["Order ID"].unique()


    df.loc[df["Order ID"].isin(r), "Order Returned"] = "Yes"

    #df["Shipping TAT"] = "N/A"
  
    #df.loc[df["Ship Days"] == 0, "Shipping TAT"] = "Same DAY"
    #df.loc[df["Ship Days"] >= 1.0, "Shipping TAT"] = "First Class"
    #df.loc[df["Ship Days"] >= 3.0, "Shipping TAT"] = "Second Class"
    #df.loc[df["Ship Days"] >= 6.0, "Shipping TAT"] = "Standard Class"

    shipdaylist = df["Ship Days"].unique()
    shipdaylist = shipdaylist.tolist()
    shipdaylist.remove("Order incomplete")

    def tat(x):
        if x == "Order incomplete":
            return 'N/A'
        elif x == 0:
            return "Same day"
        elif x >=1 and x < 3:
            return "First Class"
        elif x >=3 and x < 6:
            return "Second Class"
        else:
            return "Standard Class"

    df["Shipping TAT"] = df["Ship Days"].apply(tat)
    #return print(df["Shipping TAT"].unique())
    
    return df
superstore()

df = superstore()








