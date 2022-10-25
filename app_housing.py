import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data(1990) -By Lianxi Huang')
df = pd.read_csv('housing.csv')

# a price slider
median_house_value_filter = st.slider('Minimal Median House Price (Millions):', 0, 500001, 200000)  # min, max, default

# create a multi select of location
ocean_proximity_filter = st.sidebar.multiselect(
     'Choose an location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a subtitle before giving more filter in the sidebar 
genre = st.sidebar.radio(
    'Choose an income level',
    ('Low','Medium','High')
)

# filter by income level
if genre is None:
    pass
elif genre == 'Low':
    df = df[df.median_income <= 2.5]
elif genre == 'Medium':
    df = df[(df.median_income >2.5) & (df.median_income <4.5)]
elif genre == 'High':
    df = df[df.median_income >= 4.5]

# filter by house value
df = df[df.median_house_value >= median_house_value_filter]

# filter by location type
df = df[df.ocean_proximity.isin(ocean_proximity_filter)]

# show on map
st.map(df)

# show dataframe
st.subheader('See more filters in the sidebar:')
fig, ax = plt.subplots()
df.median_house_value.hist(ax=ax,bins = 30)

#df.median_house_value.hist(ax = ax) #bar柱状图
st.pyplot(fig)

