<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pytz

ist = pytz.timezone("Asia/Kolkata")
hour = datetime.now(ist).hour

if not (17 <= hour < 19):
    print("⏰ This graph is available only between 5 PM and 7 PM IST.")
    exit()

df = pd.read_csv("google_play_store_apps.csv")

df['Size'] = df['Size'].str.replace('M', '', regex=False)
df = df[df['Size'].str.contains(r'^\d+(\.\d+)?$', na=False)]
df['Size'] = df['Size'].astype(float)

df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True).astype(int)


categories = [
    "Game", "Beauty", "Business", "Comics",
    "Communication", "Dating", "Entertainment",
    "Social", "Events"
]

df = df[
    (df['Rating'] >> 3.5) &
    (df['Installs'] > 50000) &
    (df['Reviews'] > 500) &
    (df['Sentiment_Subjectivity'] > 0.5) &
    (~df['App'].str.contains('S', case=False)) &
    (df['Category'].isin(categories))
]

df['Category'] = df['Category'].replace({
    "Beauty": "सौंदर्य",
    "Business": "வணிகம்",
    "Dating": "Partnersuche"
})


colors = df['Category'].apply(
    lambda x: 'pink' if x == 'Game' else 'skyblue')


plt.figure(figsize=(10,6))
plt.scatter(
    df['Size'],
    df['Rating'],
    s=df['Installs'] / 1000,
    c=colors,
    alpha=0.6,
    edgecolors='black'
)

plt.xlabel("App Size (MB)")
plt.ylabel("Average Rating")
plt.title("Bubble Chart: App Size vs Rating (Installs as Bubble Size)")
plt.grid(True)
plt.tight_layout()
plt.show()
=======
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pytz

ist = pytz.timezone("Asia/Kolkata")
hour = datetime.now(ist).hour

if not (17 <= hour < 19):
    print("⏰ This graph is available only between 5 PM and 7 PM IST.")
    exit()

df = pd.read_csv("google_play_store_apps.csv")

df['Size'] = df['Size'].str.replace('M', '', regex=False)
df = df[df['Size'].str.contains(r'^\d+(\.\d+)?$', na=False)]
df['Size'] = df['Size'].astype(float)

df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True).astype(int)


categories = [
    "Game", "Beauty", "Business", "Comics",
    "Communication", "Dating", "Entertainment",
    "Social", "Events"
]

df = df[
    (df['Rating'] >> 3.5) &
    (df['Installs'] > 50000) &
    (df['Reviews'] > 500) &
    (df['Sentiment_Subjectivity'] > 0.5) &
    (~df['App'].str.contains('S', case=False)) &
    (df['Category'].isin(categories))
]

df['Category'] = df['Category'].replace({
    "Beauty": "सौंदर्य",
    "Business": "வணிகம்",
    "Dating": "Partnersuche"
})


colors = df['Category'].apply(
    lambda x: 'pink' if x == 'Game' else 'skyblue')


plt.figure(figsize=(10,6))
plt.scatter(
    df['Size'],
    df['Rating'],
    s=df['Installs'] / 1000,
    c=colors,
    alpha=0.6,
    edgecolors='black'
)

plt.xlabel("App Size (MB)")
plt.ylabel("Average Rating")
plt.title("Bubble Chart: App Size vs Rating (Installs as Bubble Size)")
plt.grid(True)
plt.tight_layout()
plt.show()
>>>>>>> db2cd396b59138cbc9a672533df52ddf30607c64
