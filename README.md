# Explore US Bikeshare Data
<img src="https://cdn.pixabay.com/photo/2022/07/24/19/42/bike-7342379_1280.png" width="250" height="160">

### Date created
9/6/2023


## Description
> Welcome to the Python tool for evaluating data from the company "Motivate". 
The company Motivate is a bike share system provider. 
In this project data of the three cities New York, Chicago and Washington can be evaluated and displayed.


**The Datasets**

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

		
The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year
<br/>

**Statistics Computed**

1. Popular times of travel (i.e., occurs most often in the start time)
	- most common month
	- most common day of week
	- most common hour of day  
  <br/>   	 
  
2. Popular stations and trip
	- most common start station
	- most common end station
	- most common trip from start to end (i.e., most frequent combination of start station and end station)  
  <br/>
  
3. Trip duration
	- total travel time
	- average travel time  
  <br/> 
  
4. User info
	- counts of each user type
	- counts of each gender (only available for NYC and Chicago)
	- earliest, most recent, most common year of birth (only available for NYC and Chicago)  
<br/>    

**Application Workflow**

1. Selection of data from Chicago, New York, or Washington
2. filter the data by month, day, or not at all
3. If month or "both" is selected, the month must be specified (January, February, March, April, May, or June)
4. If tag or "both" is selected, the tag must be specified (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday)
5. Calculation and output of statistics of data with specified filters 
6. Output of raw data with 5 lines each or skip
7. Restart or exit the program


Created and tested with the following applications under macOS 11.6:
>* Python 3.10.9
>* TextMate 2.0.23
<br/>

## Files used
>- bikeshare.py
>- chicago.csv
>- new_york_city.csv
>- washington.csv


## Credits

Created with the instructional help of the Udacity course  *Programming for Data Science with Python* .  

In addition to the Udacity materials used resources:
>- [https://stackoverflow.com/questions/31593201/how-are-iloc-and-loc-different](https://stackoverflow.com/questions/31593201/how-are-iloc-and-loc-different)
>- [https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)

Kind regards   
TippeTiTop
