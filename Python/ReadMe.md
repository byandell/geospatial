# Python Training Session

Special program on Friday 22 March 2024 hosted by Jim Sanovia featuring Nathan Quarderer and Elsa Culler from the
[Environmental Data Science Innovation and Inclusion Lab (ESIIL)](https://esiil.org)
at the University of Colorado - Boulder. The 1.5-hour program was a joint session including students and faculty from
[Oglala Lakota College](https://olc.edu)
and
[Navajo Technical University](http://www.navajotech.edu/).
Nate and Elsa presented an introduction to GIS with Python.
It requires a laptop with an internet connection and Google email or Gmail account to participate in the seminar.

- [esiil-olc-ntu-eds-workshop slides](https://docs.google.com/presentation/d/1N0VL1t2J4rwI3xwu4GVUb-w4GQHY9024OYLDw3V1JK8) 
- <https://email.org/esiil-stars>
- Gmail account versions of Python NoteBooks on my personal gmail
  + <https://colab.research.google.com/>
  + [BY olc-ntu-python-training-hv-empty.ipynb](https://colab.research.google.com/drive/143DJsbCPJUchJogtSgaBcML9y7b-J5dV) 
  + [BY olc-ntu-python-training-hv.ipynb](https://colab.research.google.com/drive/111FpbHuAOTS8FvQCdHxt0k_X-iDEKUdl)
- Online versions of python files
  + [olc-ntu-python-training-hv-empty.ipynb](https://colab.research.google.com/drive/1ZuzbG74DIqRibNtyyylYLbcZo8aTwmIB)  
  + [olc-ntu-python-training-hv.ipynb](https://colab.research.google.com/drive/1rys6eH1a6cRCrt3CzAziMX2FX7i1vmNd)
- Local downloaded python files
  + `by_olc_ntu_python_training_hv_empty.py`
  + `by_olc_ntu_python_training_hv.py`
    
## Segments of Code

Following could use some narration but are examples of code from notebooks.

running on colab

```
import geopandas as gpd
import holoviews as hv
import hvplot.pandas
import pandas as pd
```

aiannh shape file (zip) that has information about reservation boundaries

```
# Land areas url
aiannh_url = (
   "https://www2.census.gov/geo/tiger/TIGER2020/AIANNH/"
   "tl_2020_us_aiannh.zip")

# Open land area boundaries
aiannh_boundary = gpd.read_file(aiannh_url)
aiannh_boundary
```

```
# Plot data using .plot
aiannh_boundary.plot()
```

```
list(aiannh_boundary.NAME[
       aiannh_boundary.NAME.str.contains('Table')])
```

```
# Load bokeh extension for interactive plots
hv.extension('bokeh')

# Simplify geometry for faster plotting
standing_rock_boundary = aiannh_boundary[aiannh_boundary.NAME.str.startswith('Standing')]

# Plot land area boundaries
standing_rock_boundary
```

```
aiannh_boundary.NAME[
       aiannh_boundary.NAME.str.contains('Table')]
```

```
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
```

```
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
```

```
# Load bokeh extension for interactive plots
hv.extension('bokeh')


# Simplify geometry for faster plotting
standing_rock_boundary = (
   aiannh_boundary[
       aiannh_boundary.NAME.isin(['Standing Rock'])])
pine_ridge_boundary = (
   aiannh_boundary[
       aiannh_boundary.NAME.isin(['Pine Ridge', 'Rosebud'])])
```

```
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
```

## References

- [Geopandas Dataframe To Shapefile](https://mapscaping.com/geopandas-dataframe-to-shapefile/) 
- [Bokeh](https://bokeh.org/) 
- [hvPlot](https://hvplot.holoviz.org/)
- [Matplotlib list of named colors](https://matplotlib.org/stable/gallery/color/named_colors.html) 
- [HoloViews Tiles](https://holoviews.org/reference/elements/bokeh/Tiles.html)

