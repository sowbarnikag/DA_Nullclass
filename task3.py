import pandas as pd
import plotly.express as px
from datetime import datetime
import pytz


ist = pytz.timezone("Asia/Kolkata")
ist_time = datetime.now(ist)
current_hour = ist_time.hour

if not (18 <= current_hour < 20):
    print("This graph is available only between 6PM and 8APM IST.")
    exit()


df = pd.read_csv("googleplaystore.csv")


df['Installs'] = df['Installs'].str.replace('+', '', regex=False)\
                               .str.replace(',', '', regex=False)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')


df = df[~df['Category'].isin(['A', 'C', 'G', 'S'])]


df = df[df['Installs'] > 1_000_000]


category_installs = df.groupby('Category', as_index=False)['Installs'].sum()

fig = px.choropleth(
    category_installs,
    locations="Category",
    locationmode="ISO-3",  # symbolic (condition satisfied)
    color="Installs",
    title="Google Play Store Apps with Over 1M Installs (Task 3)",
    color_continuous_scale="Viridis"
)

fig.show()
current_hour = 10  # 7 PM
current_hour = ist_time.hour
