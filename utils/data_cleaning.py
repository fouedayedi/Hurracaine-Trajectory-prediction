import pandas as pd

class DataCleaning:
    def __init__(self, dataframe):
        self.df = dataframe

    def drop_na_columns(self):
        """Drops columns containing any NaN values"""
        self.df.dropna(axis=1, inplace=True)
        return self.df

csv_file = '../Dataset/Saved_files/hurricane_data.csv'

na_values = ["999"]
csv_file = '../Dataset/Saved_files/hurricane_data.csv'
data = pd.read_csv(csv_file, na_values=na_values)
cleaner = DataCleaning(data)
cleaned_df = cleaner.drop_na_columns()

# Check the first few rows of the cleaned DataFrame
print(cleaned_df.head())
