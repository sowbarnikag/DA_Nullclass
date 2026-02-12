import pandas as pd
apps_df=pd.read_csv("E:\\nullclass\\googleplaystore.csv")
reviews_df=pd.read_csv("E:\\nullclass\\googleplaystore_user_reviews.csv")
print(apps_df.head())
print(reviews_df.head())
#pd.read_csv():csv files
#pd.read_execel():excel files
#pd.read_sql():sql databases
#pd.read_json():json files
#df.isnull():missing values
#df.dropna():removes rows and colums that contain the missing values
#df.fillna():fills missing values
#df.duplicates():identifies duplicates
#df.drop_duplicates():removes duplicate rows
#step 2::::data cleaning
apps_df=apps_df.dropna(subset=["Rating"])
for column in apps_df.columns:
    apps_df[column].fillna(apps_df[column].mode()[0],inplace=True)
apps_df.drop_duplicates(inplace=True)
apps_df=apps_df[apps_df['Rating']<=5]
reviews_df.dropna(subset=['Translated_Review'],inplace=True)
#convert the installs column to numeric by removing comma
apps_df['Installs']=apps_df['Installs'].str.replace(',','').str.replace('+',"").astype(int)
apps_df['Price']=apps_df['Price'].str.replace('$','').astype(float)
print(apps_df.dtypes)
#convert price column to numeric after removing $
merged_df=pd.merge(apps_df,reviews_df,on="App",how="inner")
print(merged_df.head())


#data transformation
apps_df['Reviews']=apps_df['Reviews'].astype(int)
print(apps_df['Reviews'])
 
import numpy as np
def convert_size(size):
    if 'M' in size:
        return float(size.replace('M',''))
    elif 'k' in size:
        return float(size.replace('k',''))/1024
    else:
        return np.nan
apps_df['Size']=apps_df['Size'].apply(convert_size)
print(apps_df)

#lograrithmic
apps_df['Log_Installs']=np.log(apps_df['Installs'])
apps_df['Reviews']=apps_df['Reviews'].astype(int)
apps_df['Log_Reviews']=np.log(apps_df['Reviews'])
print(apps_df.dtypes)


def rating_group(rating):
    if rating>=4:
        return 'Top rated app'
    elif rating>=3:
        return 'Above average'
    elif rating>=2:
        return 'Average'
    else:
        return 'below average'
apps_df['Rating_group']=apps_df['Rating'].apply(rating_group)

#revenue column
apps_df['Revenue']=apps_df['Price']*apps_df['Installs']
