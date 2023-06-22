#**Age and Birthdate Calculation from IC Number**#
This repository contains a Python script that calculates the birthdate and age based on the IC (Identification Card) number in an Excel file. It utilizes the Google Colab platform for file upload and processing. The script is designed to handle IC numbers in the format "000000-00-0000".

##**Requirements**##
To run the script, you need to have the following libraries installed:

- google.colab for file upload functionality
- pandas for data manipulation and Excel file handling

##**Usage**##
1. Upload the Excel file containing the IC numbers to Google Colab.
2. Execute the script.
3. The script will process the IC numbers, calculate the birthdate and age, and update the respective columns in the Excel file.
4. The modified Excel file with updated birthdates and ages will be saved as "Result for masterfile.xlsx".
5. The file will be downloaded automatically.

Note: Ensure that the IC numbers in the file are in the format "000000-00-0000". Invalid or improperly formatted IC numbers will be skipped, and the corresponding cells will be left blank.
