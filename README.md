# ***Data Cleaning using Python***
This repository contains a Python script that clean data. 
1. Determine gender based on last digit IC number.
2. Determine age and birthdate based on IC number. 

## Requirements
To run the script, you need to have the following libraries installed:

- google.colab for file upload functionality
- pandas for data manipulation and Excel file handling

## Usage
1. Upload the Excel file containing the IC numbers to Google Colab.
2. Execute the script.
3. The script will process the IC numbers, calculate the birthdate and age, and update the respective columns in the Excel file.
4. The modified Excel file with updated birthdates and ages will be saved as "Result for masterfile.xlsx".
5. The file will be downloaded automatically.

Note: Ensure that the IC numbers in the file are in the format "000000-00-0000". Invalid or improperly formatted IC numbers will be skipped, and the corresponding cells will be left blank.
