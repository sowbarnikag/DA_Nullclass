<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
import re


ist = pytz.timezone("Asia/Kolkata")
hour = datetime.now(ist).hour

if not (16 <= hour < 18):
    print("⏰ This graph is available only between 4 PM and 6 PM IST.")
    exit()

df = pd.read_csv("google_play_store_apps.csv")

df['Size'] = df['Size'].str.replace('M', '', regex=False)
df = df[df['Size'].str.contains(r'^\d+(\.\d+)?$', na=False)]
df['Size'] = df['Size'].astype(float)

df = df[
    (df['Rating'] >= 4.2) &
    (~df['App'].str.contains(r'\d', regex=True)) &
    (df['Category'].str.startswith(('T', 'P'))) &
    (df['Reviews'] > 1000) &
    (df['Size'].between(20, 80))
]

df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')
df = df.dropna(subset=['Last Updated'])
df['Month'] = df['Last Updated'].dt.to_period('M').astype(str)

df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True).astype(int)

grouped = df.groupby(['Month', 'Category'])['Installs'].sum().unstack(fill_value=0)
grouped = grouped.sort_index()
cumulative = grouped.cumsum()

translations = {
    "Travel & Local": "Voyage et Local",
    "Productivity": "Productividad",
    "Photography": "写真"
}
cumulative.rename(columns=translations, inplace=True)
growth = cumulative.pct_change()
highlight = (growth > 0.25).any(axis=1)

plt.figure(figsize=(12,6))
colors = plt.cm.tab20.colors

for i, col in enumerate(cumulative.columns):
    alpha = 0.9 if highlight.any() else 0.6
    plt.fill_between(
        cumulative.index,
        cumulative[col],
        label=col,
        alpha=alpha,
        color=colors[i % len(colors)]
    )

plt.title("Cumulative Installs Over Time by Category")
plt.xlabel("Month")
plt.ylabel("Total Installs")
plt.legend(loc="upper left")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
=======
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
import re


ist = pytz.timezone("Asia/Kolkata")
hour = datetime.now(ist).hour

if not (16 <= hour < 18):
    print("⏰ This graph is available only between 4 PM and 6 PM IST.")
    exit()

df = pd.read_csv("google_play_store_apps.csv")

df['Size'] = df['Size'].str.replace('M', '', regex=False)
df = df[df['Size'].str.contains(r'^\d+(\.\d+)?$', na=False)]
df['Size'] = df['Size'].astype(float)

df = df[
    (df['Rating'] >= 4.2) &
    (~df['App'].str.contains(r'\d', regex=True)) &
    (df['Category'].str.startswith(('T', 'P'))) &
    (df['Reviews'] > 1000) &
    (df['Size'].between(20, 80))
]

df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')
df = df.dropna(subset=['Last Updated'])
df['Month'] = df['Last Updated'].dt.to_period('M').astype(str)

df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True).astype(int)

grouped = df.groupby(['Month', 'Category'])['Installs'].sum().unstack(fill_value=0)
grouped = grouped.sort_index()
cumulative = grouped.cumsum()

translations = {
    "Travel & Local": "Voyage et Local",
    "Productivity": "Productividad",
    "Photography": "写真"
}
cumulative.rename(columns=translations, inplace=True)
growth = cumulative.pct_change()
highlight = (growth > 0.25).any(axis=1)

plt.figure(figsize=(12,6))
colors = plt.cm.tab20.colors

for i, col in enumerate(cumulative.columns):
    alpha = 0.9 if highlight.any() else 0.6
    plt.fill_between(
        cumulative.index,
        cumulative[col],
        label=col,
        alpha=alpha,
        color=colors[i % len(colors)]
    )

plt.title("Cumulative Installs Over Time by Category")
plt.xlabel("Month")
plt.ylabel("Total Installs")
plt.legend(loc="upper left")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
>>>>>>> db2cd396b59138cbc9a672533df52ddf30607c64
