## Data Cleaning Techniques (ML_3), finished 6/7/2024
This project has two python scripts:
- 'generate&inspect_dataset.py': build a dataset from random choice and selection, 100 rows by 9 columns (features), and save the data in the file 'cleaned_dataset.csv'
- 'data_cleaning_techniques.py': read file into the dataset 'df' and perform the various operations listed below.
#### Techniques and issues covered
- Standardization
- Data Types
- Duplicates
- Missing Values
- Outliers
- String Manipulation/editing
- Categorical Data
- Normalize (Scale) Data
- Feature Engineering
### Basic data cleaning
#### Standardize dataset and data
- column names: lower case, space-to-underscore, remove whitespace
- 'city': lower-case
- 'gender': first letter only, upper-case
#### Data type: 'date_of_joining' to type datetime
#### Remove Duplicates
- df.duplicated(keep='last')    # to see
- df.duplicated().sum()         # to count
- df.drop_duplicates()          # to drop
#### Missing Values
- impute 'income' with income mean (since it's numeric)
- impute 'city' with 'Unknown' (since it's categorical)
#### Outliers
- boxplot and histplot to visualize
- remove outlier
- list 'income' values sorted in descending order
#### String Editing/Manipulation (see data_cleaning_techniques.py for notes and doco URLs)
- email and zip code merged in 'email_postal'
- str.split to split into two columns: 'email' and 'postal'
- str.extract to extract copy of first part of 'email' into new column 'name'
- drop 'email_postal'
### Advanced Data Processing
#### Categorical Data
- 'education': label encoded
  - sklearn 'LabelEncoder'
  - transforms (adds new column) in df
- 'city': oneHot encoded
  - sklearn 'OneHotEncoder'  (could use pd.get_dummies )
  - creates bool column for each city in temp dataframe
  - join temp dataframe to df
#### Normalize (Scale) Data
- want  tu use income and age to predict happiness
- income and age scale differs (as one would expect)
- use StandardScaler to scale
#### Feature Engineering
- add 'year', 'month', 'day' columns (features) from 'date_of_joining' column
- group 'income' data in new column 'income_groups' (similar to histogram)

### Generate simple data set (generate&inspect_dataset.py)
- (103 x 9) with missing data, outliers, and duplicates.
- note 'Gender' and 'City' have consistencies (multiple formats)
- create function with dataframe inspection methods
- save dataset to csv file ('cleaned_dataset') for later convenience
- as test:
  - load csv file into dataset
  - name dataset
  - inspect dataset

Adapted from 'Advanced Data Cleaning Techniques"
https://colab.research.google.com/drive/14t-s8cR_p4K2cOaOxEmdfqPoH8jJvhEM#scrollTo=dNRdvmYTO0ek



