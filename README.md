# CSV Data Cleaner 🧹🐍

A Python-based data cleaning tool that automatically processes CSV and Excel files, handles common data-quality problems, and generates a cleaned output file and cleaning report.

## 📸 Demo

![CSV Data Cleaner Demo](project-demo.png)

## ✨ Features

* 📄 Supports CSV and Excel (`.xlsx`) files
* 🧹 Removes duplicate rows
* 🔢 Handles missing numeric values using column averages
* 📝 Handles missing text values
* 📧 Detects invalid email addresses
* 🧽 Removes unnecessary spaces from text data
* 📊 Generates a detailed cleaning report
* 💾 Automatically saves the cleaned dataset
* 🛡️ Handles invalid file paths
* 🛡️ Handles unsupported file types
* 🛡️ Handles empty files and files with no data rows

## 🛠️ Technologies Used

* Python
* Pandas
* OpenPyXL
* VS Code

## 📂 Project Structure

```text
CSV_Data_Cleaner/
│
├── data_cleaner.py
├── customers.csv
├── customers_cleaned.csv
├── customers_cleaning_report.txt
├── README.md
│
└── Testing/
```

## 🚀 How to Use

1. Make sure Python is installed.
2. Install the required libraries:

```bash
pip install pandas openpyxl
```

3. Run the program:

```bash
python data_cleaner.py
```

4. Enter the path of your CSV or Excel file when prompted.

Example:

```text
C:\Users\emanf\OneDrive\Documents\Python Projects\CSV_Data_Cleaner\customers.csv
```

5. The program automatically cleans the data and creates:

* A cleaned data file
* A data cleaning report

## 📊 Example

For the included sample dataset:

```text
Original rows: 7
Final rows: 6
Duplicates removed: 1
Missing values handled: 2
Invalid emails found: 0
```

The cleaned file and report are generated automatically in the same folder as the input file.

## 🎯 Purpose

This project was created as part of my Python learning journey to practice real-world data processing, file handling, validation, and automation using Python.

## 👩‍💻 Author

**Eman Fatima**

Aspiring Computer Science student and Python learner.

GitHub: [emans-codes](https://github.com/emans-codes)

