import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import pytz
df = pd.read_csv("googleplaystore.csv")
df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')
# Size to MB
def size_to_mb(size):
    if 'M' in str(size):
        return float(size.replace('M', ''))
    elif 'k' in str(size):
        return float(size.replace('k', '')) / 1024
    else:
        return None
df['Size_MB'] = df['Size'].apply(size_to_mb)
df['Android_Ver_Num'] = df['Android Ver'].str.extract('([0-9\\.]+)')
df['Android_Ver_Num'] = pd.to_numeric(df['Android_Ver_Num'], errors='coerce')
df['App_Length'] = df['App'].astype(str).apply(len)
df['Price'] = df['Price'].str.replace('$', '', regex=False)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Revenue'] = df['Installs'] * df['Price']
filtered_df = df[
    (df['Installs'] >= 10000) &
    (df['Revenue'] >= 10000) &
    (df['Android_Ver_Num'] > 4.0) &
    (df['Size_MB'] > 15) &
    (df['Content Rating'] == 'Everyone') &
    (df['App_Length'] <= 30)
]
top_categories = (
    filtered_df
    .groupby('Category')['Installs']
    .sum()
    .sort_values(ascending=False)
    .head(3)
    .index
)
final_df = filtered_df[filtered_df['Category'].isin(top_categories)]
chart_df = final_df.groupby(['Category', 'Type']).agg({
    'Installs': 'mean',
    'Revenue': 'mean'
}).reset_index()
ist_time = datetime.now(pytz.timezone('Asia/Kolkata'))
current_hour = ist_time.hour

if 13 <= current_hour < 14:
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=chart_df['Category'] + " (" + chart_df['Type'] + ")",
        y=chart_df['Installs'],
        name='Average Installs',
        yaxis='y1'
    ))
    fig.add_trace(go.Scatter(
        x=chart_df['Category'] + " (" + chart_df['Type'] + ")",
        y=chart_df['Revenue'],
        name='Average Revenue',
        yaxis='y2',
        mode='lines+markers'
    ))
    fig.update_layout(
        title='Average Installs vs Revenue (Free vs Paid Apps)',
        yaxis=dict(title='Average Installs'),
        yaxis2=dict(
            title='Average Revenue',
            overlaying='y',
            side='right'
        ),
        xaxis_title='Category (App Type)',
        legend=dict(x=0.01, y=0.99)
    )

    fig.show()
else:
    print(" This graph is available only between 1 PM and 2 PM IST.")
