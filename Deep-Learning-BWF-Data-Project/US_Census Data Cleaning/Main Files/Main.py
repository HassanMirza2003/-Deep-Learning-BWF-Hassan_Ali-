import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('merged.csv')

#Splitting into Men And  Women coloumn
df[['Men', 'Women']] = df['GenderPop'].str.split('_', expand=True)

df['Men'] = df['Men'].str.rstrip('M')
df['Women'] = df['Women'].str.rstrip('F')

#converting Datatypes of Men and Women
df['Men'] = pd.to_numeric(df['Men'])
df['Women'] = pd.to_numeric(df['Women'])
print(df[['Men', 'Women']].dtypes)


#Checking for Any missing value
#print(df['Women'].isnull())

#replacing it with the Totalpop-men
df['Women'] = df['Women'].fillna(df['TotalPop'] - df['Men'])
print(df['Women'].isnull().sum())
#print(df['Women'])

#plotting Scatter
plt.scatter(df['Women'], df['Income'])
plt.xlabel('Women')
plt.ylabel('Income')
plt.title('Women vs Income')
#plt.show()

duplicate_rows = df[df.duplicated()]
df.drop_duplicates(inplace=True)
# Check if the duplicate rows were dropped
if not df[df.duplicated()].empty:
    print("Duplicate rows found after dropping duplicates")
else:
    print("No duplicate rows found after dropping duplicates")

#Again making scatterplot After cleaning the data
plt.scatter(df['Women'], df['Income'])
plt.xlabel('Women')
plt.ylabel('Income')
plt.title('Women vs Income')
#plt.show()

#print(df.columns)

df.drop_duplicates(inplace=True)

# Replace the percentage signs in the columns with empty strings, and convert the columns to float
df['Hispanic'] = df['Hispanic'].str.replace('%', '').astype(float)
df['White'] = df['White'].str.replace('%', '').astype(float)
df['Black'] = df['Black'].str.replace('%', '').astype(float)
df['Native'] = df['Native'].str.replace('%', '').astype(float)
df['Asian'] = df['Asian'].str.replace('%', '').astype(float)
df['Pacific'] = df['Pacific'].str.replace('%', '').astype(float)

# Fill in the NaN values in the columns with the state's average for that column
df['Hispanic'].fillna(df['Hispanic'].mean(), inplace=True)
df['White'].fillna(df['White'].mean(), inplace=True)
df['Black'].fillna(df['Black'].mean(), inplace=True)
df['Native'].fillna(df['Native'].mean(), inplace=True)
df['Asian'].fillna(df['Asian'].mean(), inplace=True)
df['Pacific'].fillna(df['Pacific'].mean(), inplace=True)

# Create a histogram for each race category
plt.figure(figsize=(10,10))

plt.subplot(321)
plt.hist(df['Hispanic'], bins=20)
plt.xlabel('Percentage of Hispanic Population')
plt.ylabel('Number of States')
plt.title('Histogram of Percentage of Hispanic Population')

plt.subplot(322)
plt.hist(df['White'], bins=20)
plt.xlabel('Percentage of White Population')
plt.ylabel('Number of States')
plt.title('Histogram of Percentage of White Population')

plt.subplot(323)
plt.hist(df['Black'], bins=20)
plt.xlabel('Percentage of Black Population')
plt.ylabel('Number of States')
plt.title('Histogram of Percentage of Black Population')

plt.subplot(324)
plt.hist(df['Native'], bins=20)
plt.xlabel('Percentage of Native Population')
plt.ylabel('Number of States')
plt.title('Histogram of Percentage of Native Population')

plt.subplot(325)
plt.hist(df['Asian'], bins=20)
plt.xlabel('Percentage of Asian Population')
plt.ylabel('Number of States')
plt.title('Histogram of Percentage of Asian Population')

plt.subplot(326)
plt.hist(df['Pacific'], bins=20)
plt.xlabel('Percentage of Pacific Population')
plt.ylabel('Number of States')
plt.title('Histogram of Percentage of Pacific Population')

plt.tight_layout()
plt.show()