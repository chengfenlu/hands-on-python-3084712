import pandas as pd

# 1. Creating a Pandas Series (a 1-dimensional labeled array)
data = [10, 20, 30, 40, 50]
index = ['A', 'B', 'C', 'D', 'E']
series = pd.Series(data, index=index)

print("Pandas Series:")
print(series)
print("\nElement at index 'C':", series['C'])
print("\nSlicing the Series:", series[1:4])

# 2. Creating a Pandas DataFrame (a 2-dimensional labeled data structure)
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}
df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

# 3. Basic DataFrame Operations
print("\nFirst 2 rows of the DataFrame:")
print(df.head(2))

print("\nLast row of the DataFrame:")
print(df.tail(1))

print("\nInformation about the DataFrame:")
print(df.info())

print("\nDescriptive statistics of numerical columns:")
print(df.describe())

# 4. Selecting Data in a DataFrame
print("\nSelecting the 'Name' column:")
print(df['Name'])

print("\nSelecting multiple columns:")
print(df[['Name', 'Age']])

print("\nSelecting rows using .loc (label-based indexing):")
print(df.loc[1])  # Row with index 1 (Bob)

print("\nSelecting rows using .iloc (integer-based indexing):")
print(df.iloc[0]) # First row (Alice)

print("\nSelecting a specific cell:")
print(df.loc[2, 'City'])  # City of the row with index 2 (Charlie)
print(df.iloc[3, 2])      # City in the 4th row and 3rd column (Tokyo)

# 5. Filtering Data
print("\nFiltering DataFrame for people older than 25:")
older_than_25 = df[df['Age'] > 25]
print(older_than_25)

print("\nFiltering DataFrame for people living in 'London':")
london_residents = df[df['City'] == 'London']
print(london_residents)

# 6. Adding a New Column
df['Salary'] = [60000, 75000, 55000, 80000]
print("\nDataFrame with 'Salary' column added:")
print(df)

# 7. Grouping Data
grouped_by_city = df.groupby('City')
print("\nAverage age per city:")
print(grouped_by_city['Age'].mean())

# 8. Reading Data from a CSV file (assuming you have a 'data.csv' file)
# To run this part, you would need a CSV file named 'data.csv'
# For example, 'data.csv' could contain:
# Name,Age,City,Salary
# Eve,23,Berlin,58000
# Frank,35,Sydney,90000
#
# try:
#     df_from_csv = pd.read_csv('data.csv')
#     print("\nDataFrame read from CSV:")
#     print(df_from_csv)
# except FileNotFoundError:
#     print("\n'data.csv' not found, skipping CSV reading example.")

# 9. Writing Data to a CSV file
# df.to_csv('output.csv', index=False) # Saves the DataFrame to 'output.csv' without the index

print("\nExample finished.")
