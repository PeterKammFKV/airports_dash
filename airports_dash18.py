#!/usr/bin/env python
# coding: utf-8

# In[82]:


import streamlit as st
import plotly.express as px
import pandas as pd
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
from PIL import Image


# In[83]:


filtered_airports = pd.read_csv('filtered_airports.csv')


# In[87]:


# Replace NaN values in the 'continent' column with 'NA'
filtered_airports['continent'].fillna('NA', inplace=True)


# In[88]:


# Convert sample data to DataFrame
df = pd.DataFrame(filtered_airports)


# In[89]:


# Streamlit app
st.title('Airport Map Dashboard')

# Description
st.write("This interactive map displays the locations of large airports across the globe. Large airports, defined as those with over 50,000 passenger movements, play a crucial role in air transportation and connectivity. Whether serving as major hubs for international travel or facilitating regional flights, these airports contribute significantly to global mobility and economic development. Explore the map to discover the geographic distribution of these key aviation hubs.")

# Filter by continent
selected_continents = st.sidebar.multiselect('Select Continents', df['continent'].unique())

# Filter data based on selected continents
filtered_df = df[df['continent'].isin(selected_continents)]

# Create and display Folium map
st.subheader('Airport Locations')
m = folium.Map(location=[0, 0], zoom_start=2)
for idx, row in filtered_df.iterrows():
    description = f"IATA Code: {row['iata_code']}<br>State: {row['iso_country']}<br>Location: ({row['latitude_deg']}, {row['longitude_deg']})"
    folium.CircleMarker(location=[row['latitude_deg'], row['longitude_deg']], radius=3, color='blue', fill=True, fill_color='blue', popup=description).add_to(m)
folium_static(m)

# Create bar chart for number of airports per continent
st.subheader('Number of Airports per Continent')
# Filtered data for bar chart
continent_counts = df['continent'].value_counts()
plt.bar(continent_counts.index, continent_counts.values)
plt.xlabel('Continent')
plt.ylabel('Number of Airports')
plt.xticks(rotation=45)
# Show exact values on the chart
for i, value in enumerate(continent_counts.values):
    plt.text(i, value + 0.1, str(value), ha='center')
st.pyplot(plt)

# Acknowledgments
st.sidebar.title('Acknowledgments')
st.sidebar.write("Created by Petar Koljensic; Airport Planner and Data Researcher in 2024")

# Logo
image = Image.open('airport_map_Amsterdam_Airport_Schiphol.png')  # Replace 'your_logo.png' with the path to your logo image file
max_size = (200, 200)  # Set the maximum size for the image
image.thumbnail(max_size, Image.LANCZOS)

# Display the resized image
st.sidebar.image(image, use_column_width=True)


# In[ ]:




