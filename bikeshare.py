import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # Initiate city, month, day with no value
    city = None
    month = None
    day = None
    print('Hello! Let\'s explore some US bikeshare data!')

    # Asks user to choose which city to analyze until a valid choice is given
    while city not in CITY_DATA:
        # If an invalid city is given, print an error message and ask the user to try again
        if city:
            print('\nWrong city:',city,'. Please try again!\n')
        city=input('\nEnter the city you\'d like to analyze (chicago, new york city, washington): ').lower()

    # Asks user to choose a month to analyze until a valid choice is given
    while month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        # If an invalid month is given, print an error message and ask the user to try again
        if month:
            print('\nWrong month: ', month,'. Please try again!\n')
        month=input('\nEnter the month you\'d like to analyze (all, january, february, march, april, may, june): ').lower()

    # Asks user to choose a day of week to analyze until a valid choice is given
    while day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        # If an invalid day is given, print an error message and ask the user to try again
        if day:
            print('\nWrong day: ', day,'. Please try again!\n')
        day=input('\nEnter the day of week you\'d like to analyze (all, mon, tues, wednes, thurs, fri, satur, sun): ').lower()
        # Concatenates the given day short name with 'day' to get the full day name
        if day != 'all':
            day=day+'day'

    print('-'*40)
    return city, month, day


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]    
    return df


def display_raw_data(city):
    """    
        Loads data for the specified city into dataframe df_print.
        Ask user whether to see 5 lines of raw data.
        If the user answers 'Yes', iterate through the next five rows in dataframe
    """
    
    start_time = time.time()
    # initiate see with 'Yes'  
    see = 'Yes'
    count = 0
    # Load data for chosen city into dataframe
    df_print = pd.read_csv(CITY_DATA[city])

    # ask user whether to see 5 lines of raw data until another answer than 'Yes' is given
    while see == 'Yes':
        see = input('\nWould you like to see 5 lines of raw data? Yes/No: ').title()
        if see != 'Yes':
            break

        print('\n\nPrinting raw data...\n')
        print('-'*40)
        # initiate counter which ensures to show five new lines of raw data
        next_count = 0
        # as long as there are rows in the dataframe
        for row in df_print:  
            # display the next five rows of raw data from dataframe
            if next_count < 5:
                print(df_print.loc[count,:],'\n')
                count += 1
                next_count += 1
            else:
                print("\nThis took %s seconds." % (time.time() - start_time))
                print('-'*40)
                break
   
def month_number_to_month_name(month_number, month_name):
    """ 
        converts month number to month name 
    """
    
    months = {
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June'
        }
    
    try:
        month_name = months[month_number]
        return month_name
    except:
        raise ValueError('Given value is not a valid month number')


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # fetch the most common month
    common_month = df['month'].mode()[0]
    month_name = None
    # converts month number to month name
    month_name = month_number_to_month_name(common_month, month_name)
    
    print('The most common month is: ',month_name)

    # display the most common day of week
    print('The most common day is: ',df['day_of_week'].mode()[0])

    # add hour to data frame
    df['hour'] = df['Start Time'].dt.hour

    # display the most common hour (from 0 to 23)
    print('Most Frequent Start Hour:', df['hour'].mode()[0] )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station is: ',df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The most commonly used end station is: ',df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    counts = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
    print('The most frequent combination of start station and end station trip is: ', counts.index[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n\nCalculating Trip Duration...\n')
    start_time = time.time()

    # sum the total of Trip Duration in seconds
    total_travel_time_sec = int(df['Trip Duration'].sum())
    #calculate the total trip duration in days, hours, minutes and seconds
    total_travel_time_min, total_travel_time_sec = divmod(total_travel_time_sec, 60)
    total_travel_time_hour, total_travel_time_min = divmod(total_travel_time_min, 60)
    total_travel_time_day, total_travel_time_hour = divmod(total_travel_time_hour, 24)    
    # display total travel time
    print('Total travel time: {} days, {} hours, {} minutes, {} seconds'.format(total_travel_time_day,total_travel_time_hour, total_travel_time_min, total_travel_time_sec))

    # find the mean travel time in seconds
    mean_travel_time_sec = int(df['Trip Duration'].mean())
    #calculate the average trip duration in days, hours, minutes and seconds 
    mean_travel_time_min, mean_travel_time_sec = divmod(mean_travel_time_sec, 60)
    mean_travel_time_hour, mean_travel_time_min = divmod(mean_travel_time_min, 60)
    mean_travel_time_day, mean_travel_time_hour = divmod(mean_travel_time_hour, 24)    
    # display mean travel time
    print('Mean travel time: {} days, {} hours, {} minutes, {} seconds'.format(mean_travel_time_day,mean_travel_time_hour, mean_travel_time_min, mean_travel_time_sec))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\n\nCalculating User Stats...\n')
    start_time = time.time()

    # counts unique values of user types
    user_types = df['User Type'].value_counts()
    # Display counts of user types
    print('Count for each user type:\n',user_types)



    # check whether gender is present in the data set for chosen city
    if 'Gender' in df.columns:
        # count unique values of gender leaving out NaN
        counts_of_gender = df['Gender'].value_counts(dropna=True)
        # TO DO: Display counts of gender
        print('\nCount pr. gender:\n', counts_of_gender)
    
    else:
        print('\nGender is not present in the data for {}.\n'.format(city))

    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
  
    # program runs repeatedly until the user chooses another answer than 'yes'
    while True:
        # get input values for city, month and day to analyze
        city, month, day = get_filters()
        # filter data from the chosen data set into data frame 
        df = load_data(city, month, day)

        # calculate time, station, trip duration and user statistics based on previous user input
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        # display 5 lines of raw data until the user chooses no to   
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
