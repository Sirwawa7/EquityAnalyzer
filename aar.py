import pandas as pd

# Load the Excel file
file_path = 'C:/Users/Ndosi/Desktop/Ntando/New/SharePrices.xlsx'
df = pd.read_excel(file_path)

# Remove the time part from the date column
df['Date'] = pd.to_datetime(df['Date']).dt.date

# Sort the data by date in ascending order
df_sorted = df.sort_values(by='Date', ascending=True)

# Save the sorted data to a new Excel file
sorted_file_path = 'C:/Users/Ndosi/Desktop/Ntando/New/Share Prices_Sorted.xlsx'
df_sorted.to_excel(sorted_file_path, index=False)

print(f"The data has been rearranged from the latest date and saved to {sorted_file_path}.")
