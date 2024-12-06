import pandas as pd

# Load the Excel file
xls = pd.ExcelFile(r'C:/Users/Ndosi/Desktop/Ntando/New/data.xls', engine='xlrd')

# Create a dictionary to hold the sorted data for each sheet
sorted_data = {}

# Define the columns to keep
columns_to_keep = ['Date', 'Nedbank Eswatini', 'Royal Swazi Sugar', 'SWD Empowerment Limited', 
                   'SWAPROP', 'Greystone', 'SBC Limited', 'Inala Capital Limited', 
                   'NPC Limited', 'FNB Limited']

# Iterate through each sheet in the Excel file
for sheet_name in xls.sheet_names:
    # Load the sheet into a DataFrame
    df = pd.read_excel(xls, sheet_name=sheet_name, engine='xlrd')
    
    # Check if the required columns are in the DataFrame
    if all(col in df.columns for col in columns_to_keep):
        # Keep only the specified columns
        df = df[columns_to_keep]
        
        # Convert the 'Date' column to datetime format
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        
        # Sort the DataFrame by the 'Date' column
        df_sorted = df.sort_values(by='Date')
        
        # Store the sorted DataFrame in the dictionary
        sorted_data[sheet_name] = df_sorted
    else:
        print(f"Sheet '{sheet_name}' does not contain the required columns.")

# Check if there is any sorted data to save
if sorted_data:
    # Save the sorted data to a new Excel file
    with pd.ExcelWriter(r'C:/Users/Ndosi/Desktop/Ntando/New/data_sorted.xls', engine='openpyxl') as writer:
        for sheet_name, df_sorted in sorted_data.items():
            df_sorted.to_excel(writer, sheet_name=sheet_name, index=False)
    print("The data has been sorted and saved to 'data_sorted.xls'.")
else:
    print("No sheets contained the required columns. No file was saved.")