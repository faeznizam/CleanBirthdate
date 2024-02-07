import pandas as pd
import datetime
import os

# function to validate national id
def validate_nat_id(national_id):
  # remove empty spaces between digit
  national_id = national_id.replace(" ", "")

  # add hypen to 12 digit number
  if len(national_id) == 14:
    return national_id
  elif len(national_id) == 12:
    national_id = f"{national_id[:6]}-{national_id[6:8]}-{national_id[8:]}"
  else:
    return None

  return national_id

# function to calculate birthdate
def calculate_birthdate(national_id):
  if national_id is None:
    return None

  year = national_id[0:2]
  month = national_id[2:4]
  day = national_id[4:6]

  current_year = datetime.datetime.now().year % 100

  # determine the century based on last 2 digit in year
  if int(year) <= current_year:
    century = 20
  else:
    century = 19

# check if day between 1-31 only and handle ValueError
  try:
      if int(day) >= 1 and int(day) <= 31:
        birthdate = f"{century}{year}-{month}-{day}"
      else:
        return None
  except ValueError:
      birthdate = None

  return birthdate

# function to calculate age
def calculate_age(birthdate):
  # check birthdate
  if birthdate is None:
    return None

  current_year = datetime.datetime.now().year
  birth_year = int(birthdate[:4])
  age = current_year - birth_year

  return age

def filter_dataframe(df):
    filter_condition = (
        ((df['National ID'].astype(str).str.len() == 12) | (df['National ID'].astype(str).str.len() == 14)) &
        df['National ID'].notna() &
        (df['National ID'] != '')
    )
    filtered_df = df[filter_condition].copy()
    return filtered_df


def main():
    # get file from folder
    folder_path = r'C:\Users\mfmohammad\OneDrive - UNICEF\Documents\Data Cleaning\2024\Feb\7'

    file_name = 'Donor Without Age and Birthdate.xlsx'

    # combine folder path and file name
    file_path = os.path.join(folder_path, file_name)

    # manipulate file
    df = pd.read_excel(file_path)

    filter_df = filter_dataframe(df)

    filter_df['National ID'] = filter_df['National ID'].apply(validate_nat_id)
    filter_df['Birthdate'] = filter_df['National ID'].apply(calculate_birthdate)
    filter_df['Age'] = filter_df['Birthdate'].apply(calculate_age)

    df.loc[filter_df.index, ['Birthdate', 'Age']] = filter_df[['Birthdate', 'Age']]

    df[['National ID', 'Birthdate', 'Age']]

    # rename file with new name
    current_filename = file_name[:-5]
    new_file_name = f'{current_filename} - Edited.xlsx'

    # build output file path
    new_file_path = os.path.join(folder_path, new_file_name)

    df.to_excel(new_file_path, index = False)

    # successfull attempt prompt
    print(f'File {new_file_name} been saved in the folder')

if __name__ == "__main__":
  main()