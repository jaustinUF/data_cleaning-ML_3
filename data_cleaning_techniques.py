import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
import random
import string
import warnings
# warnings.filterwarnings('ignore')

# set display properties
pd.set_option('display.width', None)        # No wrapping of lomg lines
pd.set_option('display.max_columns', None)  # Display all columns with not folding

def inspect(dataframe):
    print(f"Inspection information for {dataframe.attrs['name']}:")
    print(f'Head(): \n{dataframe.head()}\n*   *   *   *   *')
    print(f'Tail(): \n{dataframe.tail()}\n*   *   *   *   *')
    print(f'Shape: \n{dataframe.shape}\n*   *   *   *   *')
    print(f'Describe(): \n{dataframe.describe()}\n*   *   *   *   *')
    print(f'Info:')
    print(f'{dataframe.info()}\n*   *   *   *   *')

# load data into dataframe
df = pd.read_csv('cleaned_dataset.csv')     # dataset
df.attrs['name'] = "df"                     # name dataframe for 'inspect' function
# inspect(df)
##-> Standardize dataset and data
# standardize column names: lower case, space-to-underscore, then remove remaining whitespace Iif any)
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace(r'\W', '', regex=True)
# print(df.city.value_counts(dropna=False))   # check for non-standard data formats
# print(df.city.unique())                     # both these work but previous clearer
df.city = df.city.str.lower()               # all lower case
df.gender = df.gender.str.upper().str[0]    # all upper-case first letter
# print(df.head())
# standardized <-##
##-> Data Types
# 'date_of_joining' is type object, should be datetime
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
df['date_of_joining'] = pd.to_datetime(df['date_of_joining'], format='%Y-%m-%d')
# use .astype() if .to_type not available
# Data Types <-##

##-> Remove Duplicates
# print(f'number of duplicated rows: {df.duplicated().sum()}')
# print(f"Duplicated rows: {df[df.duplicated(keep='last')]}")
df = df.drop_duplicates()                   # keeps first (default)
# print(f'Duplicated rows (after drop_duplicates()): {df.duplicated().sum()}')
# Remove Duplicates <- ##

##-> Missing Values
# print(df.isnull().sum())                  # count missing values per column
#        missing values in 'income' and 'city'
# impute 'income' with mean, since it is type number
mean_income = df.income.mean()
df['income'] = df['income'].fillna(mean_income) # fill NA/NaN values with value or some method (see doco)
# 'city' is categorical without a clear majority value, so impute with 'Unknown'
df['city'] = df['city'].fillna('Unknown')
# Missing Values <- ##

##-> Handle Outliers
# print(df.describe())   # by default only does numeric types; 'include=' to see other types
# 'income' shows mean = ~80K, with max of 300K ... suspect outlier(s)
'''plt.figure(figsize=(8,4))                   # visualize: boxplot and histogram
plt.subplot(1, 2, 1)
sns.boxplot(df.income)
plt.subplot(1, 2, 2)
sns.histplot(df.income)
plt.tight_layout()
plt.show()'''
# remove outliers above 200000
df = df.loc[df.income <= 200000] # remove outlier
# print(df.income.sort_values(ascending=False).head()) # 'income' values sorted in descending order.
# Handle Outliers <- ##

##-> String Editing/Manipulation
# documentation: .str methods: https://pandas.pydata.org/docs/user_guide/text.html
#   ChatGPT: Pandas Series and .str accessor; https://chatgpt.com/c/dbd7464c-b71a-4e25-a849-982f5ac9c175


# dataset problem: in 'email_postal' column, email and zip merged
# plan: split 'email_postal' into three new columns: user, email, zip
# str.split: https://blog.hubspot.com/website/pandas-split-string
#   ChatGPT: Regex, extract, split; https://chatgpt.com/c/34033d5e-4343-4673-a690-562952221714
df[['email', 'postal']] = df['email_postal'].str.split(',', expand=True)
df['name'] = df['email'].str.extract(r'^(.*)@').astype('string')
df.drop(columns='email_postal', inplace=True)
# inspect(df)
# String Editing/Manipulation <- ##

##-> Encoding Categorical Data
# visualize categorical data: 'education' and 'city'
'''plt.figure(figure=(10, 2))
plt.subplot(121)
sns.countplot(df, x='education')
plt.xticks(rotation=45)

plt.subplot(122)
sns.countplot(df, x='city')
plt.xticks(rotation=45)
plt.show()'''
# visualize end #
# add column with education encoded as integer
label_enc = LabelEncoder()
label_enc.fit(['Associate','Bachelor', 'Master', 'PhD'])
df['education_enc'] = label_enc.transform(df['education'])
# add boolean columns for each city
ohe = OneHotEncoder()                       # add boolean columns for each city
ohe.fit(df[['city']])
# print(ohe.categories_)                      # categories (unique city names)
ohe_columns = ohe.get_feature_names_out(['city'])
# print(ohe_columns)                          # 'city_' + categories (city names)
df_enc = pd.DataFrame(ohe.transform(df[['city']]).toarray(), columns=ohe_columns)
# print(df_enc.head(20))                      # dataframe of OneHot encoded columns
df = df.join(df_enc)                        # join columns by index; based on .merge, which is more versatile
# print(df.head(20))
# Encoding Categorical Data <- ##

##-> Normalize (Scale) Data
# LR model using income and age to predict happiness
# print(df[['income', 'age', 'happiness_score']].head(20)) # income and age have different scales (as would be expected)
'''features_to_scale = ['income', 'age']
scaler = StandardScaler()
df_scaled = df.copy()                       # scale copy not original
df_scaled[features_to_scale] = scaler.fit_transform(df_scaled[features_to_scale]) #scale
print(df_scaled[['income', 'age', 'happiness_score']].head(5)) # check scaled df
sns.pairplot(df_scaled[['income', 'age', 'happiness_score']])
plt.show()'''
# Normalize (Scale) DataNormalize (Scale) Data <- ##

##-> Feature Engineering
# Enhance model performance by creating or transforming features to better represent the underlying patterns in the dat
# Extracting year, month, day from datetime
df['year'] = df['date_of_joining'].dt.year
df['month'] = df['date_of_joining'].dt.month
df['day'] = df['date_of_joining'].dt.day
# print(df[['date_of_joining', 'year', 'month', 'day']].head()) # new columns (features) for year, month, day
# Binning income groups
sns.histplot(df.income)
# plt.show()
# Collect 'income' data into bins in new df column 'income_groups' (similar to visual histogram ).
# define bin labels
labels = [f'{i//1000}-{(i+20000)//1000}K' for i in range(0, 120000, 20000)]
labels[-1] = '100K+'
# bin edges
bins = np.arange(0, 120001, 20000)
# Bin 'income' values into discrete intervals: 'income_groups'
df['income_groups'] = pd.cut(df['income'], bins=bins, labels=labels, right=False)
print(df[['income', 'income_groups']].head())
# Feature Engineering <- ##

# **** Do README.md *****

