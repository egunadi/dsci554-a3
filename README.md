[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/WofS52QW)
# DSCI 554 Assignment 3

- [ASSIGNMENT.md](ASSIGNMENT.md) contains the Rubric

## Landing page instructions

"index.html" is the landing page. It can be served on a browser via hot-reload:

```bash
npm install    #install js libraries
npm run serve  #starts server on port 2000
```
Alternately, this page can be viewed in GitHub at <https://egunadi.github.io/dsci554-a3/>.

## Design choices 

The landing page showcases two visualizations, laid out side-by-side with thumbnails and a brief description. 

### Countries in 2022 with the Highest Population Densities

This is an Inkscape-SVG bubble cloud chart showing the top ten countries with the highest population densities in 2022. Population density values are encoded as bubble/circle areas. Doing so meant obtaining circle diameters by taking the square root of the values, thus minimizing the range between the minimum and maximum values (640.1 and 24475.8 respectively). For viewers to easily sort the bubbles:

- Bubbles are numbered in descending order based on Population Density
- Bubbles are arranged so adjacent numbers are next to each other

### Region Encoding Added

This is a variant of the first chart with added encoding, namely that bubbles are color-coded according to geographic region (ex. Europe, Asia, etc.). Bubbles of the same color are grouped together so viewers can better compare the various regions.

## Running the project

"data/popdensity22_top10.csv" is the processed data used to size the SVG bubbles.

"code/filter_data.py" was used to process the data. Notably:

- The data is filtered to only Series="Population Density" and Year="2022"
- Since we are interested in countries, Region/Area entries (ex. Macau and Hong Kong) are filtered out despite being some one of the most population-dense regions in the world

The original, full data on "Population, surface area and density" can be downloaded here:

<https://data.un.org/_Docs/SYB/CSV/SYB65_1_202209_Population,%20Surface%20Area%20and%20Density.csv>

(Note that the first row is the spreadsheet title and must be manually removed prior to processing.) 
