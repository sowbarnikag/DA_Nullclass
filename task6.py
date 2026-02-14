<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
ist = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(ist)
hour = current_time.hour
if not (18 <= hour < 21):
    print("⏰ This graph is available only between 6 PM and 9 PM IST.")
    exit()
df = pd.read_csv("googleplaystore.csv")
df['Installs'] = df['Installs'].astype(str)
df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True)
df = df[df['Installs'].str.isnumeric()]
df['Installs'] = df['Installs'].astype(int)
df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')
df = df.dropna(subset=['Last Updated'])
df['Month'] = df['Last Updated'].dt.to_period('M').astype(str)
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
df = df.dropna(subset=['Reviews'])
df = df[
    (df['Reviews'] > 500) &
    (df['Category'].str.startswith(('E', 'C', 'B'))) &
    (~df['App'].str.lower().str.startswith(('x', 'y', 'z'))) &
    (~df['App'].str.contains('S', case=False))
]
df['Category'] = df['Category'].replace({
    "Beauty": "सौंदर्य",       # Hindi
    "Business": "வணிகம்",     # Tamil
    "Dating": "Partnersuche"  # German
})

grouped = df.groupby(['Month', 'Category'])['Installs'].sum().unstack(fill_value=0)
grouped = grouped.sort_index()
growth = grouped.pct_change()
plt.figure(figsize=(12, 6))

for category in grouped.columns:
    plt.plot(grouped.index, grouped[category], label=category)
    for i in range(1, len(grouped)):
        if growth[category].iloc[i] > 0.20:
            plt.fill_between(
                grouped.index[i-1:i+1],
                grouped[category].iloc[i-1:i+1],
                alpha=0.25
            )

plt.xlabel("Month")
plt.ylabel("Total Installs")
plt.title("Trend of Total Installs Over Time by App Category")
plt.legend()
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
=======
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
ist = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(ist)
hour = current_time.hour
if not (18 <= hour < 21):
    print("⏰ This graph is available only between 6 PM and 9 PM IST.")
    exit()
df = pd.read_csv("googleplaystore.csv")
df['Installs'] = df['Installs'].astype(str)
df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True)
df = df[df['Installs'].str.isnumeric()]
df['Installs'] = df['Installs'].astype(int)
df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')
df = df.dropna(subset=['Last Updated'])
df['Month'] = df['Last Updated'].dt.to_period('M').astype(str)
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
df = df.dropna(subset=['Reviews'])
df = df[
    (df['Reviews'] > 500) &
    (df['Category'].str.startswith(('E', 'C', 'B'))) &
    (~df['App'].str.lower().str.startswith(('x', 'y', 'z'))) &
    (~df['App'].str.contains('S', case=False))
]
df['Category'] = df['Category'].replace({
    "Beauty": "सौंदर्य",       # Hindi
    "Business": "வணிகம்",     # Tamil
    "Dating": "Partnersuche"  # German
})

grouped = df.groupby(['Month', 'Category'])['Installs'].sum().unstack(fill_value=0)
grouped = grouped.sort_index()
growth = grouped.pct_change()
plt.figure(figsize=(12, 6))

for category in grouped.columns:
    plt.plot(grouped.index, grouped[category], label=category)
    for i in range(1, len(grouped)):
        if growth[category].iloc[i] > 0.20:
            plt.fill_between(
                grouped.index[i-1:i+1],
                grouped[category].iloc[i-1:i+1],
                alpha=0.25
            )

plt.xlabel("Month")
plt.ylabel("Total Installs")
plt.title("Trend of Total Installs Over Time by App Category")
plt.legend()
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
>>>>>>> db2cd396b59138cbc9a672533df52ddf30607c64
plt.show()