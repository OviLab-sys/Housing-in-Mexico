import pandas as pd
import matplotlib.pyplot as plt 
import plotly.express as px  

df = pd.read_csv("data/mexico-real-estate-clean.csv")

### for location data : Latitude and Longitude 
# visualization we use plotly.express.scatter_mapbox()

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    center={"lat": 19.4326, "lon": -99.1332},  # Center on Mexico City
    width=800,
    height=800,
    hover_data=["price_usd"]
)


fig.update_layout(mapbox_style ="open-street-map")
fig.show()  # shows the map in a borwser window for interractive exploration

# Save the figure as an HTML file
fig.write_html("mexico_real_estate_map.html")


"""Categorical Data"""
#entails counts of properties by type and state
# for our case, we have property types located in different states of mexico
# to know exactly how many different values of categorical data(in this case state), we have we 
# can use the following pandas functions

df["state"].nunique() #gives the number of unique states
df["state"].unique() #gives the unique states
df["state"].value_counts() #gives the number of values per category 

"""Numerical Data"""

#for numerical data, we can use the describe() function to get a summary of the data
# this will give us the count, mean, std, min, 25%, 50%, 75%, and max values of the numerical data
#for our case, we have the price_usd and area_m2 columns
df["price_usd", "area_m2"].describe()


"""Generating Histograms"""
#histograms are a great way to visualize the distribution of numerical data
# ahistogram shows how frequent data values occur within a certain range
