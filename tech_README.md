
Create features:    df['new_feature'] = df['col1'] / df['col2']

Log transformation:	np.log1p(), np.log()

Binning:		    pd.cut(), pd.qcut()

Date time:		    df['year'] = pd.to_datetime(df['date_column']).dt.year

Value mapping:		mapping = {'Low' : 0, 'High': 1}, df['mapped'] = df['feature'].map(mapping)

#### Normalize/Scale methods
- MinMaxScaler: scales the data to a specified range, typically between 0 and 1. (value – min)/{max-min)
  - preserves the original distribution of the data while ensuring that all features are within the specified range.
- StandardScaler:  removes mean and scales to unit variance … results in mean = 0 and SD = 1. (for Gaussian distributions)    
- Normalizer: scales each data point independently based on sum of squares of each column (feature).

#### Encoding Categorical Data
LabelEncoder: for ordinal categorical data (order or ranking among categories)
- education levels "high school," "college," and "graduate" encoded as 0, 1, and 2.
OneHotEncoder: Each category represented by binary column (1/True/presence of the category; 0/False/absence.
- for nominal categorical data with no inherent order among categories; suitable when number of categories is small.
TargetEncoder: for high-cardinality categorical features (large number of unique categories)
- encode based on relationship with the target variable.
- replace each category with the mean of the target variable for that category. 

Missing Values
(good discussion of imputation)

Note: the Colab notebook is the tutorial; contains a lot of (good) notes!

My copy: My Drive > Colab Notebooks > data-cleaning-techniques.ipynb

Adapted from 'Advanced Data Cleaning Techniques"
https://colab.research.google.com/drive/14t-s8cR_p4K2cOaOxEmdfqPoH8jJvhEM#scrollTo=dNRdvmYTO0ek
See also https://www.w3schools.com/python/pandas/pandas_cleaning.asp