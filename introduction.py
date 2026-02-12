import os
import pandas as pd
data=pd.read_csv('C:\\Users\\Lenovo\\dataset_heart.csv')
print(data)
print(data.head())
print(data.tail()) 
print(data.describe())
print(data.info())
import numpy as np
df=pd.read_csv('C:\\Users\\Lenovo\\test.csv')
print(data.isnull())
data['heart disease']=data['heart disease'].replace(np.nan,data['heart disease'].mean())
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
xpoints=np.array([1,3,5,76])
ypoints=np.array([0,34,67,250])
plt.plot(xpoints,ypoints)
plt.show()
y=np.array([25,35,15,25])
plt.pie(y)
plt.show()
x=np.random.normal(170,10,250)
print(x)
plt.hist(x)
plt.show()
sns.distplot([1,2,3,4])
plt.show()
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,r2_score  

import plotly.express as px
fig=px.bar(x=["A","B","C"],y=[1,3,2],title="Sample Bar Chart")
print(fig.show())
fig.write_html("interactive_plot.html")


import plotly.io as pio
html_files_path=",/"
if not os.path.exists(html_files_path):
    os.makedirs(html_files_path)
plot_containers=""
def save_plot_to_html(fig,filename,insight):
    global plot_containers
    filepath=os.path.join(html_files_path,filename)
    html_content=pio.to_html(fig,full_html=False,include_plotlyjs='inline')
    plot_containers += f"""
    <div class ="plotcontainer"id="('{filename}')"onclick="openplot('{filename}')"open
    <div class ="plot">{html_content}</div>
    <div class="insights">{insight}</div> 
    </div>
    """
    fig.write_html(filepath,full_html=False,include_plotlyjs='inline')
plot_width=400
plot_height=300
plot_bg_color='black'
text_color='white'
title_font={'size':16}
axis_font={'size':12}
#figure2

# Now this will work
category_counts = data['heart disease'].value_counts().nlargest(10)
print(category_counts)

category_counts=data['heart disease'].value_counts().nlargest(10)
print(category_counts)
fig1=px.bar(
    x=category_counts.index,
    y=category_counts.values,
    labels={'x':'Category','y':'Count'},
    title='Top Category on Play Store',
    color=category_counts.index,
    color_discrete_sequence=px.colors.sequential.Plasma,
    width=400,
    height=300
)
fig1.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font={'size':16},
    xaxis=dict(title_font={'size':12}),
    yaxis=dict(title_font={'size':12}),
    margin=dict(l=10,r=10,t=30,b=10)
)
#fig1.update_traces(marker=dict(line=dict(color='white', width=1)))
save_plot_to_html(fig1,"interactive_plot.html","the top categories on the playstore")




#figure 3
fig3=px.histogram(
    data,
    x='age',
    nbins=20,
    title='rating distribution',
    color_discrete_sequence=['#636EFA'],
    width=400,
    height=300
)
fig3.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font={'size':16},
    xaxis=dict(title_font={'size':12}),
    yaxis=dict(title_font={'size':12}),
    margin=dict(l=10,r=10,t=30,b=10)
)
#fig2.update_traces(marker=dict(line=dict(color='white', width=1)))
save_plot_to_html(fig3,"rating graph 3.html","rating are skewed towards higher values,suggested that most apps are rated favorably by users")

#figure 4

sentiment_counts=data['heart disease'].value_counts()
fig4=px.bar(
    x=category_counts.index,
    y=category_counts.values,
    labels={'x':'Category','y':'Count'},
    title='Top Category on Play Store',
    color=category_counts.index,
    color_discrete_sequence=px.colors.sequential.RdPu,
    width=400,
    height=300
)
fig4.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font={'size':16},
    xaxis=dict(title_font={'size':12}),
    yaxis=dict(title_font={'size':12}),
    margin=dict(l=10,r=10,t=30,b=10)
)
#fig4.update_traces(marker=dict(line=dict(color='white', width=1)))
save_plot_to_html(fig4,"sentiment graph 4.html","sentiment in reviews show a mix of positive and negative")


#figure 5

installs_by_category=data.groupby('age')['chest pain type'].sum().nlargest(10)
fig5=px.bar(
    x=installs_by_category.index,
    y=installs_by_category.values,
    orientation='h',
    labels={'x':'chest pain type','y':'category'},
    title='installs by category',
    color=installs_by_category.index,
    color_discrete_sequence=px.colors.sequential.Blues,
    width=400,
    height=300
)
fig5.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font={'size':16},
    xaxis=dict(title_font={'size':12}),
    yaxis=dict(title_font={'size':12}),
    margin=dict(l=10,r=10,t=30,b=10)
)
#fig5.update_traces(marker=dict(line=dict(color='white', width=1)))
save_plot_to_html(fig5,"installs graph 5.html","the categories with the most installs are social and communication apps by reflectes their broad appels and daily usage")



#figure 6
updates_per_year = data['chest pain type'].value_counts().sort_index()
fig6=px.line(
    x=updates_per_year.index,
    y=updates_per_year.values,
    labels={'x':'years','y':'number of updates'},
    title='number of updates over the years',
    color_discrete_sequence=['#AB63FA'],
    width=plot_width,
    height=plot_height
)
fig6.update_layout(
    plot_bgcolor='blue',
    paper_bgcolor='purple',
    font_color='yellow',
    title_font={'size':16},
    xaxis=dict(title_font={'size':12}),
    yaxis=dict(title_font={'size':12}),
    margin=dict(l=10,r=10,t=30,b=10)
)
#fig6.update_traces(marker=dict(line=dict(color='white', width=1)))
save_plot_to_html(fig6,"updates graph 6.html","updates have been increasing over the years,showing that developers are actively maintaining and improving their apps")


#figure7
revenue_by_category=data.groupby('age')['chest pain type'].sum().nlargest(10)
fig7=px.bar(
    x=installs_by_category.index,
    y=installs_by_category.values,
    labels={'x':'category','y':'revenue'},
    title='revenue by category',
    color=installs_by_category.index,
    color_discrete_sequence=px.colors.sequential.Blues,
    width=400,
    height=300
)
fig7.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font={'size':16},
    xaxis=dict(title_font={'size':12}),
    yaxis=dict(title_font={'size':12}),
    margin=dict(l=10,r=10,t=30,b=10)
)
#fig5.update_traces(marker=dict(line=dict(color='white', width=1)))
save_plot_to_html(fig7,"revenue graph 7.html","category such as buiseness and productivity leads in revenue generation indicating their monitization potential")

#figure 8
genrecounts=data['age'].value_counts()
fig8=px.bar(
    x=genrecounts.index,
    y=genrecounts.values,
    labels={'x':'genre','y':'count'},
    title='top genres',
    color_discrete_sequence=px.colors.sequential.OrRd,
    width=400,
    height=300
)
fig8.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font={'size':16},
    xaxis=dict(title_font={'size':12}),
    yaxis=dict(title_font={'size':12}),
    margin=dict(l=10,r=10,t=30,b=10)
)
#fig5.update_traces(marker=dict(line=dict(color='white', width=1)))
save_plot_to_html(fig8,"genre graph 8.html","action and casual genres are the most common reflecting user preference")

#figure9

fig9=px.scatter(
    data,
    x='serum cholestoral',
    y='resting blood pressure',
    color='oldpeak',
    title='impact of last update on rating',
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=400,
    height=300
)
fig9.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font={'size':16},
    xaxis=dict(title_font={'size':12}),
    yaxis=dict(title_font={'size':12}),
    margin=dict(l=10,r=10,t=30,b=10)
)
#fig9.update_traces(marker=dict(line=dict(color='white', width=1)))
save_plot_to_html(fig9,"update graph 9.html","the scatter plot shows a weak correlation between the last update and ratings,suggesting that more frequent updates dont always result")


#figure10
fig10=px.box(
    data,
    x='oldpeak',
    y='resting blood pressure',
    color='oldpeak',
    title='rating for paid vs free',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    width=400,
    height=300
)
fig10.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font={'size':16},
    xaxis=dict(title_font={'size':12}),
    yaxis=dict(title_font={'size':12}),
    margin=dict(l=10,r=10,t=30,b=10)
)
#fig10.update_traces(marker=dict(line=dict(color='white', width=1)))
save_plot_to_html(fig10,"paid free graph 10.html","paid apps generation")

plot_containers_split=plot_containers.split('</div')
if len(plot_containers_split)>1:
    final_plot=plot_containers_split[-2]+'</div'
else:
    final_plot=plot_containers





#############################################################
#creating web dashboard
import os
html_files_path = "E:/nullclass/html_files"
import webbrowser
dashboard_html= """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name=viewport" content="width=device-width,initial-scale-1.0">
    <title>Google Play Store Review Analytics</title>
    <style>
        body {{
            font-family:Arial,sans-serif;
            background-color:#333;
            color:#fff;
            margin: 0;
            padding: 0;
        }}
        .header {{
            display.flex;
            align-items: center;
            justify-content: center
            padding: 20px
            background-color:#444
        }}
        .header img {{
            margin: 0 10px;
            height: 50px;
        }}
        .container {{
            display:flex;
            flex-wrap:wrap;
            justify_content: center;
            padding: 20px;
         }}
         .plot-container {{
            border: 2px solid #555;
            margin: 10px;
            padding: 10px
            width: {plot_width}px;
            height: {plot_height}px;
            overflow:hidden;
            position:relative;
            cursor:pointer;
        }}
        .insights {{
            display:none;
            position:absolute;
            right: 10px;
            top: 10px;
            background-color: rgba(0,0,0,0.7)
            padding: 5px;
            border-radius: 5px;
            color: #fff;
        }}
        .plot-container: hover .insights {{
            display: block;
        }}
        </style>
        <script>
            function openPlot(filename) {{
                window.open(filename, '_blank');
                }}
        </script>
    </head>
    <body>
        <div class= "header">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Logo_2013_Google.png/800px-Logo_2013_Google.png"alt="Google Logo">
            <h1>Google Play Store Reviews Analytics</h1>
            <img src="https://upload.wikimedia.org/wikipedia/commons/7/78/Google_Play_Store_badge_EN.svg" alt="Google Play Store Logo" height="50">
        </div>
        <div class="container">
            {plots}
        </div>
</body>
</html>
"""
final_html=dashboard_html.format(plots=plot_containers,plot_width=plot_width,plot_height=plot_height)
html_dashboard=r"E:\nullclass\html_dashboard"
dashboard_path=os.path.join(html_dashboard,"web page.html")
with open(dashboard_path, "w",encoding="utf-8") as f:
    f.write(final_html)
webbrowser.open('file://'+os.path.realpath(dashboard_path))

