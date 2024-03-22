# -*- coding: utf-8 -*-
"""BY olc-ntu-python-training-hv-empty.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/111FpbHuAOTS8FvQCdHxt0k_X-iDEKUdl

<img style="float: left;" src="https://www.drought.gov/sites/default/files/styles/i_square_480_480/public/hero/partners/navajo-tech-university-logo.jpeg.webp?itok=JaKCP1gi" width="175"><img style="float: left;" src="https://scontent-den2-1.xx.fbcdn.net/v/t39.30808-6/294600247_521949093060977_7728339716521427232_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=5f2048&_nc_ohc=4RBLHM3g6pcAX-FJhAa&_nc_ht=scontent-den2-1.xx&oh=00_AfDyIU8DyRfpanjc-k8b8650J8VKPjkxHUhlzi6eQ9BFcg&oe=6601BC1A" width="175" height="175"><img style="float: right;" src="https://pbs.twimg.com/profile_images/1537109064093532160/mG03dW9G_400x400.jpg" width="175" height="175">

Welcome to the **ESIIL-Oglala Lakota College-Navajo Technical University** GIS & Python Training.

My name Nate Quarderer and I'm the Education Director at the Environmental Data Science Innovation & Inclusion Lab (ESIIL). I'm joined by my good friends and colleagues Elsa Culler (Education Trainer) and Jim Sanovia (Tribal Resilience Data Scientist), also from ESIIL. Today we're going to demonstrate for you some GIS + Earth Data Science (EDS) applications using Python.

* In **Part 1 (Working with Spatial Data in Python)** we'll show you how to create maps using `geopandas` and data from the U.S. Census Bureau, specifically **The American Indian/Alaska Native/Native Hawaiian (AIANNH) Areas Shapefile:** https://catalog.data.gov/dataset/tiger-line-shapefile-2020-nation-u-s-american-indian-alaska-native-native-hawaiian-aiannh-areas

* In **Part 2 (Working with Time-Series Data in Python)** you will learn how to access data from the [Global Historical Climatology Network daily (GHCNd)](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) at **NOAA**. We will then use those data to create a time-series plot of temperature or precipitation over time using `pandas` and `matplotlib`.

***

> 🚨 Please start by **making a copy of this notebook** that you can make changes.
>
> 🚨 To do this by selecting **File > Save a copy in Drive** and then *renaming* the file (add your initials).

# Part 1: Working with Spatial Vector Data in Python

### **About Spatial Vector Data**

Vector data are composed of discrete geometric locations (x, y values) known as vertices that define the “shape” of the spatial object. The organization of the vertices determines the type of vector that you are working with. There are three types of vector data:

**Points:** Each individual point is defined by a single x, y coordinate. Examples of point data include: sampling locations, the location of individual trees or the location of plots.

**Lines:** Lines are composed of many (at least 2) vertices, or points, that are connected. For instance, a road or a stream may be represented by a line. This line is composed of a series of segments, each “bend” in the road or stream represents a vertex that has defined x, y location.

**Polygons:** A polygon consists of 3 or more vertices that are connected and “closed”. Thus, the outlines of plot boundaries, lakes, oceans, and states or countries are often represented by polygons.


<img style="float: left;" src="https://www.earthdatascience.org/images/earth-analytics/spatial-data/points-lines-polygons-vector-data-types.png">


> ### ✨ Read more about working with spatial data using Python in our free, open EDS textbook, [here](https://www.earthdatascience.org/courses/intro-to-earth-data-science/file-formats/use-spatial-data/use-vector-data/). ✨
"""

# Commented out IPython magic to ensure Python compatibility.
# Install missing python packages
# %pip install hvplot geoviews

# Import Python packages
import geopandas as gpd
import holoviews as hv
import hvplot.pandas
import pandas as pd

# Land areas url
aiannh_url = (
    "https://www2.census.gov/geo/tiger/TIGER2020/AIANNH/"
    "tl_2020_us_aiannh.zip")

# Open land area boundaries
aiannh_boundary = gpd.read_file(aiannh_url)
aiannh_boundary
aiannh_boundary.NAME[aiannh_boundary.NAME.str.contains('Table')]

# Plot data using .plot
aiannh_boundary.plot()

list(aiannh_boundary.NAME[
        aiannh_boundary.NAME.str.contains('Table')])

# Load bokeh extension for interactive plots
hv.extension('bokeh')

# Simplify geometry for faster plotting
standing_rock_boundary = (
    aiannh_boundary[
        aiannh_boundary.NAME.str.startswith('Standing')])

# Plot land area boundaries
standing_rock_boundary.hvplot(
    geo=True,
    title="Standing Rock",
    fill_color="green",
    line_color="white",
    alpha=.5,
    tiles="EsriImagery"
)

aiannh_boundary[
        aiannh_boundary.NAME.isin(['Standing Rock','Pine Ridge'])]

# Load bokeh extension for interactive plots
hv.extension('bokeh')

# Simplify geometry for faster plotting
standing_rock_boundary = (
    aiannh_boundary[
        aiannh_boundary.NAME.isin(['Standing Rock','Pine Ridge', 'Rosebud'])])

# Plot land area boundaries
standing_rock_boundary.hvplot(
    geo=True,
    title="Table",
    fill_color="orange",
    line_color="white",
    alpha=.5,
    tiles="EsriImagery"
)

# Load bokeh extension for interactive plots
hv.extension('bokeh')

# Simplify geometry for faster plotting
standing_rock_boundary = (
    aiannh_boundary[
        aiannh_boundary.NAME.isin(['Standing Rock'])])
pine_ridge_boundary = (
    aiannh_boundary[
        aiannh_boundary.NAME.isin(['Pine Ridge', 'Rosebud'])])

# Plot land area boundaries
(standing_rock_boundary.hvplot(
    geo=True,
    title="Table",
    fill_color="orange",
    line_color="white",
    alpha=.5,
    tiles="EsriImagery"
)
+ pine_ridge_boundary.hvplot(
    geo=True,
    title="Table",
    fill_color="orange",
    line_color="white",
    alpha=.5,
    tiles="EsriImagery")
).opts(shared_axes=False)

# Open US State boundary
us_url = (
    "https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_state_20m.zip")

us_gdf = gpd.read_file(us_url)
us_gdf.head()

# Load bokeh extension for interactive plots
hv.extension('bokeh')

# Select AZ

# Plot AZ boundary

# Clip AIANNH boundary to AZ boundary

# Select larger reservation areas so we can see them on the map

# Load bokeh extension for interactive plots
hv.extension('bokeh')

# Plot clipped AIANNH boundary

# Select individual reservation and plot separately

# Navajo Nation


# San Carlos


# Pine Ridge

# Load bokeh extension for interactive plots
hv.extension('bokeh')

# Plot each reservation separately

"""# Part 2: Working with Time-Series Data in Python

Here we're using the NOAA National Centers for Environmental Information (NCEI) [Access Data Service](https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation) application progamming interface (API) to request data from their web servers. We will be using daily summary data collected as part of the [Global Historical Climatology Network daily (GHCNd)](https://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND) program at NOAA.

For this example we're requesting data near **Kyle, SD** (station ID USC00394630) located on the Pine Ridge Reservation (**43.4402°, -102.1431°**).

https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USC00394630/detail


> ### ✨ Read more about working with time-series data using Python in our free, open EDS textbook, [here](https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/introduction-to-time-series-in-pandas-python/) ✨
"""

# Use NCEI API to pull data from the station @ Kyle, SD (Pine Ridge)

kyle_api_url = (
    "https://www.ncei.noaa.gov/access/services/data/v1"
    "?dataset=daily-summaries"
    "&dataTypes=TOBS,PRCP"
    "&stations=USC00394630"
    "&startDate=1956-12-01"
    "&endDate=2024-03-22"
    "&includeStationName=true"
    "&units=standard"
    )

# Open and clean data with pandas

# Load bokeh extension for interactive plots
hv.extension('bokeh')

# Plot data