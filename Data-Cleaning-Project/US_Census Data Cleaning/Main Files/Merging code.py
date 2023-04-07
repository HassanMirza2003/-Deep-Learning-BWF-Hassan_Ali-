import pandas as pd

# Create an empty list to store dataframes
dfs = []

# Loop through each CSV file and append its dataframe to the list
for i in range(10):
    filename = f"states{i}.csv"
    df = pd.read_csv(filename)
    dfs.append(df)

# Concatenate all dataframes in the list
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged dataframe as a new CSV file
merged_df.to_csv("merged.csv", index=False)
