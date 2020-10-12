import pandas as pd 

ds = pd.read_csv("owid-covid-data.csv")

print(ds.columns)

ds_ir = ds.loc[ds["location"] == "Iran"]

print(ds_ir["total_deaths"].sum())