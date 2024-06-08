import numpy as np
import pandas as pd
import random
import string

# set display properties
pd.set_option('display.width', None)  # No wrapping of lomg lines
pd.set_option('display.max_columns', None)  # Display all columns with not folding

##-> data generation
# generate email address/zip code lists to be used in data set ('Email_Postal') generation
emails = [f'{"".join(random.choices(string.ascii_lowercase, k=4))}({i})@somewhere.com' for i in range(100)]
zips = [f'{np.random.randint(10000, 99999)}' for _ in range(100)]
# generate data set (dictionary)
data = {
    'ID': range(1, 101),
    'Age': [random.choice([25, 30, 35, 40, 45, 50, 60, 70]) for _ in range(100)],
    'Gender': [random.choice(['M', 'F', 'Male', 'Female', 'male', 'female']) for _ in range(100)],
    'Income': [random.choice([30000, 50000, 70000, 90000, 110000, np.nan]) for _ in range(100)],
    'Date of Joining': pd.date_range(start='1/1/2020', periods=100, freq='D').strftime('%Y-%m-%d').tolist(),
    'City': [random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New york', 'los angeles', 'chicago', 'HOUSTON', 'phoenix', np.nan]) for _ in range(100)],
    'Happiness Score': [random.choice([50, 60, 70, 80, 90, 100, 150, 200]) for _ in range(100)],
    'Email_Postal': [f"{random.choice(emails)},{random.choice(zips)}" for _ in range(100)],
    'Education': [f"{random.choice(['Associate','Bachelor', 'Master', 'PhD'])}" for _ in range(100)]
}
df = pd.DataFrame(data)                                          # convert dictionary to pandas dataframe
# add outliers
outlier_indices = random.sample(range(len(df)), 2)              # two (random) integers from  range len(df)
# .loc doco: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
# locate data elements in rows with 'outlier_indices' indices and column label 'Income'
df.loc[outlier_indices, 'Income'] = df.loc[outlier_indices, 'Income'] * 10  # multiply located elements by 10
# add duplicate rows
dup_indices = random.sample(range(len(df)), 3)                  # three (random) integers from  range len(df)
df = pd.concat([df, df.loc[dup_indices]], ignore_index=True)    # append three existing rows to create duplicates
# data set generated <-##

def inspect(dataframe):
    print(f"Inspection information for {dataframe.attrs['name']}:")
    print(f'Head(): \n{dataframe.head()}\n*   *   *   *   *')
    print(f'Tail(): \n{dataframe.tail()}\n*   *   *   *   *')
    print(f'Shape: \n{dataframe.shape}\n*   *   *   *   *')
    # Describe: only numeric types by default; 'include=' to see other types
    print(f'Describe(): \n{dataframe.describe()}\n*   *   *   *   *')
    print(f'Info:')
    print(f'{dataframe.info()}\n*   *   *   *   *')

# df.to_csv('cleaned_dataset.csv', index=False)                # saved after generation
'''df1 = pd.read_csv('cleaned_dataset.csv')                       # retrieved as test
df1.attrs['name'] = "df1"                                       # test dataframe named
inspect(df1)  '''                                                  # inspect dataframe
