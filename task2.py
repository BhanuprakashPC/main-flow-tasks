import pandas as pd

# Load the CSV file into a Pandas DataFrame
file_path = '01.Data Cleaning and Preprocessing.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Filtering data based on a condition (example: select rows where column 'A' > 10)
if 'A' in df.columns:
    filtered_df = df[df['A'] > 10]
    print("\nFiltered DataFrame where 'A' > 10:")
    print(filtered_df)

# Handling missing values
# Option 1: Fill missing values with a specified value (e.g., fill with 0)
df_filled = df.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_filled)

# Option 2: Drop rows with missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)

# Calculating summary statistics
print("\nSummary statistics of the DataFrame:")
print(df.describe())
