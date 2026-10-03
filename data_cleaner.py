import pandas as pd
import os
file_path = input("Enter the CSV or Excel file path: ").strip('"')

file_extension = os.path.splitext(file_path)[1].lower()


print("\nStarting data cleaning...")
print("--------------------------")

try:

    if file_extension == ".csv":

        data = pd.read_csv(file_path)

    elif file_extension == ".xlsx":

        data = pd.read_excel(file_path)

    else:

        print("Unsupported file type. Please use a CSV or Excel file.")
        exit()

except FileNotFoundError:

    print("File not found. Please check the file path and try again.")
    exit()

except pd.errors.EmptyDataError:

    print("The file is empty. Please provide a file containing data.")
    exit()
    
if data.empty:

    print("The file contains no data rows. Please provide a file containing data.")
    exit()

data.columns = data.columns.str.strip()
original_rows = len(data)

missing_values = data.isnull().sum().sum()

invalid_emails = 0

if "Email" in data.columns:
    emails = data["Email"].astype(str).str.strip()
    invalid_emails = (~emails.str.contains(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", regex=True, na=False)).sum()

for column in data.select_dtypes(include="str").columns:
    data[column] = data[column].str.strip()

duplicates_removed = data.duplicated().sum()
data = data.drop_duplicates()

numeric_columns = data.select_dtypes(include="number").columns

for column in numeric_columns:
    data[column] = data[column].fillna(data[column].mean())

for column in numeric_columns:
    if data[column].dropna().apply(float.is_integer).all():
        data[column] = data[column].astype(int)

text_columns = data.select_dtypes(include="str").columns

for column in text_columns:
    data[column] = data[column].fillna("Unknown")        

data = data.reset_index(drop=True)

final_rows = len(data)
total_columns = len(data.columns)


print("Original rows:", original_rows)
print("Final rows:", final_rows)
print("Duplicates removed:", duplicates_removed)
print("Missing values handled:", missing_values)
print("Invalid emails found:", invalid_emails)

report_file = os.path.splitext(file_path)[0] + "_cleaning_report.txt"

with open(report_file, "w") as report:
    report.write("DATA CLEANING REPORT\n")
    report.write("====================\n")
    report.write(f"Original rows: {original_rows}\n")
    report.write(f"Final rows: {final_rows}\n")
    report.write(f"Columns processed: {total_columns}\n")
    report.write(f"Duplicates removed: {duplicates_removed}\n")
    report.write(f"Missing values handled: {missing_values}\n")
    report.write(f"Invalid emails found: {invalid_emails}\n")

print("Cleaning report saved as:", report_file)

output_file = os.path.splitext(file_path)[0] + "_cleaned" + file_extension


if file_extension == ".csv":
    data.to_csv(output_file, index=False)

elif file_extension == ".xlsx":
    data.to_excel(output_file, index=False)

print("\nCleaning completed successfully!")
print("-------------------------------")
print("Cleaned file saved as:", output_file)



