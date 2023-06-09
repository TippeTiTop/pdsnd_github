import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
city_list = ['chicago', 'new york', 'washington']      
time_filter_type_list = ['month', 'day', 'both', 'none']
month_list = ['january', 'february', 'march', 'april', 'may', 'june']  
day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
   

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = ''
    time_filter_type = ''
    month = ''
    day = ''
    leave = False
    
    print('Hello! Let\'s explore some US bikeshare data! Enjoy!')
        
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_filter_value('city', city_list)
    leave = (city == 'no')  
    
    # get time filter type
    if not leave:         
        time_filter_type = get_filter_value('filter_type', time_filter_type_list)
        leave = (time_filter_type == 'no')  
        
    # get user input for month (all, january, february, ... , june)
    if (not leave) and (time_filter_type == 'both' or time_filter_type == 'month'):         
        month = get_filter_value('month', month_list)
        leave = (month == 'no')  

    # get user input for day of week (all, monday, tuesday, ... sunday)
    if (not leave) and (time_filter_type == 'both' or time_filter_type == 'day'):         
        day = get_filter_value('day', day_list)
        leave = (day == 'no') 

    print('-'*40)
    return city, month, day
    
    
def get_filter_value(val_type, val_list):
    """
    The function outputs the filter value based on the filter type and the corresponding list and controls the individual questions to the user
    
    Args:
        (str) val_type - specifies the type and/or the kind of the filter (city, filter_type, month, day)
        (list) val_list - List containing the possible values of a user response matching the val_type
    
    Returns:
        (str) input_val - Filter value for the dataframe
    """
    
    input_val = ''
    input_count = 0
    
    if val_type == 'city':
        input_msg_1 = 'Would you like to see data for Chicago, New York, or Washington?\n'     
        input_msg_2 = 'The answer could not be detected. Please Enter "Chicago", "New York" or "Washington" to filter the data.\nEnter "no" to leave the program.\n'  
        
    elif val_type == 'filter_type':
        input_msg_1 = 'Would you like to filter the data by month, day, or not at all? Type "none" for no time filter.\n'     
        input_msg_2 = 'The answer could not be detected. Please Enter "month", "day", "both" or "none" for no time filter.\nEnter "no" to leave the program.\n'
         
    elif val_type == 'month':
        input_msg_1 = 'Which month? January, February, March, April, May or June?\n'     
        input_msg_2 = 'The answer could not be detected. Please Enter "January", "February", "March", "April", "May" or "June".\nEnter "no" to leave the program.\n'     
              
    elif val_type == 'day':                    
        input_msg_1 = 'Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n'     
        input_msg_2 = 'The answer could not be detected. Please Enter "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" or "Sunday".\nEnter "no" to leave the program.\n'     
    
    
    while (input_val not in val_list) and (input_val != 'no'): 
         if input_count == 0:    
             input_msg = input_msg_1    
         else:
             input_msg = input_msg_2      
 
         input_val = input(input_msg).lower()  
         input_count += 1   

    return input_val
    


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """  
    day_index = 0 
    month_index = 0
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    
    # filter by month to create the new dataframe
    if month != '':
        month_index = month_list.index(month) + 1  
        df = df[df['month']==month_index]
    
    # filter by day of week to create the new dataframe    
    if day != '':
        day_index = day_list.index(day) 
        df = df[df['day_of_week']==day_index]        
      
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', month_list[common_month-1])

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', day_list[common_day])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station:', common_start_station)
    
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common end station:', common_end_station)

    # display most frequent combination of start station and end station trip
    common_comb = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most frequent combination of start station and end station:', common_comb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time - hours, minutes, seconds
    travel_total = df['Trip Duration'].sum() 
    print('Total travel time:', pd.to_datetime(travel_total, unit='s').strftime('%H:%M:%S'))
    
    # display mean travel time - minutes, seconds 
    travel_mean = df['Trip Duration'].mean() 
    print('Mean travel time:', pd.to_datetime(travel_mean, unit='s').strftime('%H:%M:%S'))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types    
    user_types = df['User Type'].value_counts()
    print('Counts of user types:')
    print(user_types)
    print('\n')

    # Display counts of gender
    gender_counts = df['Gender'].value_counts()
    print('Counts of gender:')
    print(gender_counts)
    print('\n')

    # Display earliest, most recent, and most common year of birth
    birth_earliest = df['Birth Year'].min()
    birth_mostrecent = df['Birth Year'].max()
    birth_mostcommon =  df['Birth Year'].mode()[0]
    
    print('Earliest year of birth:', int(birth_earliest))
    print('Most recent year of birth:', int(birth_mostrecent))
    print('Most common year of birth:', int(birth_mostcommon))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_rawdata(df):
    
    """
    
    continuously outputs a predefined number of lines of a Panda DataFrame, starting with index 0. 
    The output is interrupted within one iteration if the user does not answer with "yes" 
    and automatically terminated when the end of the DataFrame has been reached
    
    """
    
    show_rows = True
    show_steps = 10
    rows_max = show_steps
    rows_min = 0
   
    while show_rows and (len(df) >= rows_max):
      
      if rows_max == show_steps:
          show_msg = '\nWould you like to see the first '+ str(show_steps) +' lines of raw data? Enter yes or no.\n'
      else:
          show_msg = '\nWould you like to see another '+ str(show_steps) +' lines of raw data? Enter yes or no.\n' 
      
      show_input = input(show_msg)
      if show_input.lower() != 'yes':
         show_rows = False
      else:
         if len(df) != rows_max: 
             print(df.iloc[rows_min:rows_max]) 
         else:
             print(df.iloc[rows_min:])      
               
           
      if len(df) >= (rows_max +show_steps):
          rows_min = rows_max
          rows_max += show_steps
      elif len(df) == rows_max:
          show_rows = False  
      else:  
          rows_min = rows_max        
          rows_max = len(df)              
       

def main():
    while True:
        city, month, day = get_filters()
        if (city != 'no') and (month != 'no') and (day != 'no'):          
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            
            if city != 'washington':
                user_stats(df)
            else:
                print('\nNo User Stats available for Washington...\n')
                print('-'*40) 
                            
            show_rawdata(df)                 

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        else:
            break        


if __name__ == "__main__":
	main()
