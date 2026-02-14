<<<<<<< HEAD
import pandas as pd
import plotly.express as px
from datetime import datetime
import pytz
df = pd.read_csv("googleplaystore.csv")
df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

def size_to_mb(size):
    if 'M' in str(size):
        return float(size.replace('M', ''))
    elif 'k' in str(size):
        return float(size.replace('k', '')) / 1024
    else:
        return None

df['Size_MB'] = df['Size'].apply(size_to_mb)
df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')

filtered_df = df[
    (df['Rating'] >= 4.0) &
    (df['Size_MB'] >= 10) &
    (df['Last Updated'].dt.month == 1)
]
top_categories = (
    filtered_df
    .groupby('Category')['Installs']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .index
)

final_df = filtered_df[filtered_df['Category'].isin(top_categories)]
chart_df = final_df.groupby('Category').agg({
    'Rating': 'mean',
    'Reviews': 'sum'
}).reset_index()
ist_time = datetime.now(pytz.timezone('Asia/Kolkata'))
current_hour = ist_time.hour

if 15 <= current_hour < 17:
    fig = px.bar(
        chart_df,
        x='Category',
        y=['Rating', 'Reviews'],
        barmode='group',
        title='Average Rating and Total Reviews (Top 10 Categories)'
    )
    fig.show()
else:
    print("⏰ This graph is available only between 3 PM and 5 PM IST.")
=======
import pandas as pd
import plotly.express as px
from datetime import datetime
import pytz
df = pd.read_csv("googleplaystore.csv")
df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

def size_to_mb(size):
    if 'M' in str(size):
        return float(size.replace('M', ''))
    elif 'k' in str(size):
        return float(size.replace('k', '')) / 1024
    else:
        return None

df['Size_MB'] = df['Size'].apply(size_to_mb)
df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')

filtered_df = df[
    (df['Rating'] >= 4.0) &
    (df['Size_MB'] >= 10) &
    (df['Last Updated'].dt.month == 1)
]
top_categories = (
    filtered_df
    .groupby('Category')['Installs']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .index
)

final_df = filtered_df[filtered_df['Category'].isin(top_categories)]
chart_df = final_df.groupby('Category').agg({
    'Rating': 'mean',
    'Reviews': 'sum'
}).reset_index()
ist_time = datetime.now(pytz.timezone('Asia/Kolkata'))
current_hour = ist_time.hour

if 15 <= current_hour < 17:
    fig = px.bar(
        chart_df,
        x='Category',
        y=['Rating', 'Reviews'],
        barmode='group',
        title='Average Rating and Total Reviews (Top 10 Categories)'
    )
    fig.show()
else:
    print("⏰ This graph is available only between 3 PM and 5 PM IST.")
>>>>>>> db2cd396b59138cbc9a672533df52ddf30607c64
