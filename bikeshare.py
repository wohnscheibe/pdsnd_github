import time
import datetime as dt
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    while True:
        city =  input('\nEnter the first letter of the city you want to explore!\
        \nEnter N=New York, C=Chicago or W=Washington\n').lower()
        try:
            if city == 'n':
                city = 'new york city'
                break
            elif city == 'c':
                city = 'chicago'
                break
            elif city == 'w':
                city  = 'washington'
                break
            else:
                false = input('\nNot a valid input. Try again? Enter y=yes or any other key to abort.\n').lower()
                if false != 'y':
                    city = 'quit'
                    month = 'quit'
                    day = 'quit'
                    return city, month, day
        except:
            print('An exception occurred')

    # get user input for month (all, january, february, ... , june)
    while True:
        month =  input('\nEnter month you want to explore!\
        \nEnter a=all, 1=january, 2=february, ... , 6=june\n')

        try:
            if month.lower() == 'a':
                month = 'all'
                break
            if month == '1':
                month = 'january'
                break
            elif month == '2':
                month = 'february'
                break
            elif month == '3':
                month  = 'march'
                break
            elif month == '4':
                month  = 'april'
                break
            elif month == '5':
                month  = 'may'
                break
            elif month == '6':
                month  = 'june'
                break
            else:
                false = input('\nNot a valid input. Try again? Enter y=yes or any other key to abort.\n').lower()
                if false != 'y':
                    month = 'quit'
                    day = 'quit'
                    return city, month, day
        except:
            print('An exception occurred')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day =  input('\nEnter day of week you want to explore!\nEnter a=all, mon=monday, tue=tuesday, ... , sun=sunday\n').lower()
        try:
            if day == 'a':
                day = 'all'
                break
            if day == 'mon':
                day = 'monday'
                break
            elif day == 'tue':
                day = 'tuesday'
                break
            elif day == 'wed':
                day  = 'wednesday'
                break
            elif day == 'thu':
                day  = 'thursday'
                break
            elif day == 'fri':
                day  = 'friday'
                break
            elif day == 'sat':
                day  = 'saturday'
                break
            elif day == 'sun':
                day  = 'sunday'
                break
            else:
                false = input('\nNot a valid input. Try again? Enter y=yes or any other key to abort.\n').lower()
                if false != 'y':
                    day  = 'quit'
                    break
        except:
            print('An exception occurred')

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

    #city = city + ".csv"
    df = pd.read_csv(CITY_DATA[city])

    # new column place
    df['place'] = city.title()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month if not specified
    if month == "all":
        popular_month = df['month'].mode()[0]
        print('Most Popular Month:\t\t', popular_month)

    # display the most common day of week if not specified
    if day == "all":
        popular_day = df['day'].mode()[0]
        print('Most Popular Day of Week:\t', popular_day)

    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:\t', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:\t\t', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:\t\t', popular_end_station)

    # display most frequent combination of start station and end station trip
    # extract hour from the Start Time column to create an hour column
    df['Start_End_Station'] = df['Start Station'] + ' --> ' + df['End Station']
    popular_start_end_station = df['Start_End_Station'].mode()[0]
    print('Most Popular Start End Combination:\t', popular_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    traveltime_total = df['Trip Duration'].sum()
    print("Total travel time:\t", traveltime_total)

    # display mean travel time
    traveltime_mean = df['Trip Duration'].mean()
    print("Mean travel time:\t", traveltime_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n', user_types)
    user_null = df['User Type'].isnull().sum()
    print('No user type data:\t', user_null)

    # In the washington data set is no gender and birth year --> skip
    if df['place'][0] != 'Washington':
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print('\nCounts of gender:\n', gender)
        gender_null = df['Gender'].isnull().sum()
        print('No Gender data:\t', gender_null)

        # Display earliest, most recent, and most common year of birth
        year_min = df['Birth Year'].min()
        print('\nEarliest year of birth\t', year_min)

        year_max = df['Birth Year'].max()
        print('\nMost recent year of birth\t', year_max)

        year_mode = df['Birth Year'].mode()
        print('Most common year of birth\t', year_mode)

        birth_year_null = df['Birth Year'].isnull().sum()
        print('No birth year data:\t', birth_year_null)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    while True:
        """Displays five rows of raw data. """
        raw_start = input('\nWould you like to see some raw data? Enter y=yes or any other key to abort\n')
        if raw_start.lower() != 'y':
            break

        stop = len(df['Start Time'])
        for line in range(0, stop, 5):
            print(df[line:line+5])
            restart = input('\nWould you like to see five more rows? Enter y=yes or any other key to abort\n')
            if restart.lower() != 'y':
                break
        break

def main():
    while True:
        city, month, day = get_filters()

        #quit if no valid input is given
        if city == "quit" or month == "quit" or day == "quit":
            print("You haven't entered valid input!")
            break

        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter y=yes or any other key to abort\n')
        if restart.lower() != 'y':
            break

if __name__ == "__main__":
	main()
