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

## Running the project

- Link to download original data on "Population, surface area and density"
  - https://data.un.org/_Docs/SYB/CSV/SYB65_1_202209_Population,%20Surface%20Area%20and%20Density.csv
  - First row is the spreadsheet title and must be manually removed (column headers in second row)
- [filter_data.py](code/filter_data.py) was used to process the data
  - The data is filtered to only Population Density in the year 2022
  - Since we are interested in countries, Region/Area entries are filtered out
    - ex. Macau and Hong Kong (despite being one of the most populated regions in the world)
  - Despite only selecting the top 10 entries, there is a vast range of values (24475.8 max to 640.1 min)
    - To minimize this difference, values are encoded as bubble areas and we obtain diameter by taking the square root of the values 

## Design choices 

- The "svg" folder contains SVG files created using Inkscape
  - [popdensity22_top10.inkscape.svg](svg/popdensity22_top10.inkscape.svg) presents bubbles as circles using the calculated diameters. For viewers to easily sort the bubbles:
    - Bubbles are numbered in descending order based on Population Density
    - Bubbles are arranged so adjacent numbers are next to each other
  - [popdensity22_top10_region.inkscape.svg](svg/popdensity22_top10_region.inkscape.svg) adds additional encoding, namely that bubbles are color-coded according to geographic region (ex. Europe, Asia, etc.)
    - Bubbles of the same color are grouped together so viewers can better compare the various regions
  - Plain SVG formats of the above files have also been created for the HTML page 
