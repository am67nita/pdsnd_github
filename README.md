### Date created
Project: 10/22/2020
README.md: 10/22/2020

### Project Title
Bikeshare

### Description
Python script which imports US bike share data and answers interesting questions about the data 
by computing descriptive statistics. 

#### Detailed Descriptiong
This script is written to explore data related to bike share systems for three major cities in the United States
—Chicago, New York City and Washington. 
The script compares the system usage between three large cities: Chicago, New York City, and Washington, DC.

The script asks the user to enter the city, month (all, January...June) and the day of week (all, mon...sun) to analyze.
Based on this input, the script opens a csv-file for the chosen city, loads the data into a data frame and
manipulates the data frame to reflect the input given by the user.

The following descriptive statistics are then displayed for the user:
- The most common month, day of week and hour to travel 
- The most popular station(s) to travel from, to and between
- The total travel time and the average travel time
- How many times each user group and gender travels 

The user is repeatedly asked whether to look at five lines of raw data from the data set until answering 'no'.
Five lines of data is display every time the user answers 'yes'. The scripts solves this by loading raw data into av dataframe
and iterating through the dataframe five rows at a time and display these rows for the user.

The user decides when the script ends by answering restart 'yes' og 'no'


### Authors
Anne Mette Andreassen

### Files used
* bikeshare.py
* chicago.csv
* new_york_city.csv
* washington.csv


* Imported python modules: time, pandas

### Credits

* stackoverflow.com
* pandas.pydata.org

