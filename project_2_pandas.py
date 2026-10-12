import pandas as pd
df = pd.read_csv("project_1.csv")
df.columns = df.columns.str.strip().str.lower()
print("Q1. Whats the average number of children?")
print("A.", df["children"].mean())
print("Q2. Whats the average household count?")
print("A.", df["household_size"].mean())
region_data = df.groupby("region")["children"].mean()
print("Q3. How does average number of children vary by region?")
print(region_data.round(2))
highest_name = region_data.idxmax()
lowest_name = region_data.idxmin()
print("Q4. Which region has the highest and Lowest number of children?")
print("Highest Average Children:", highest_name,
      "with", round(region_data.max(), 2))
print("Lowest Average Children:", lowest_name,
      "with", round(region_data.min(), 2))
education_data = df.groupby("education")[
    ["children", "household_size"]
].mean()

print("Q5. How do education groups differ in their average number of children And Household size")
print(education_data.round(2))
employment_data = df.groupby("employment")[
    ["children", "household_size"]
].mean()

print("Q6. How do employment groups differ in the average number of children and household size?")
print(employment_data.round(2))