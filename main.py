import pandas as pd

# --- File Path ---
# For local file:
# file_path = 'C:/Users/YourName/Documents/data.xlsx'

# Show all columns in output
pd.set_option('display.max_columns', None)

# OR for direct online URL (e.g., from OneDrive, Dropbox)
file_path = "https://docs.google.com/spreadsheets/d/1yKx5o5sU47jmB8xXFkccDursyd5atwyk/export?format=xlsx"


# --- Load the Excel file ---
df = pd.read_excel(file_path ,engine='openpyxl')

# --- Search for a row by ID ---
search_id = 'PRAD001'  # replace with the actual ID you're searching for

# Replace 'ID' with the actual column name of the ID column
result = df[df['PR No'] == search_id]

# --- Print the result ---
if not result.empty:
    print("Matching row found:")
    
    print(result)
else:
    print("ID not found.")


