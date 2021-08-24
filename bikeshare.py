import time
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city do you want to explore Chicago, New York City or Washington? \n> ').lower()
        if city in CITY_DATA:
            break
        else:
            print('\nPlease type the correct city name!')
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('enter a monthe from the first six or "all" for all\n>').lower()
        if month in('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            break
        else:
            print('\nPlease type the correct month name!')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('enter a day or "all for all\n>').lower()
        if day in('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
        else:
            print('\nPlease type the correct day name!')

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        m = months.index(month) +1
        df = df[df['month'] == m]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is :', most_common_month)
    # display the most common day of week
    most_common_day_of_week = df['day'].mode()[0]
    print('The most common day of week is :', most_common_day_of_week)
    # display the most common start hour
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is :', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station :', most_common_start_station)
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station :', most_common_end_station)
    # display most frequent combination of start station and end station trip
    most_common_start_end_station = (df['Start Station'] + ', ' + df['End Station']).mode()[0]
    print('The most commonly used start station and end station :',\
          most_common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time :', total_travel)
    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time :', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_counts = df['User Type'].value_counts()
    print('Counts of user types:\n', user_counts)
    # Display counts of gender
    if city == 'chicago' or city == 'new york city':
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender:\n", gender_counts)
    # Display earliest, most recent, and most common year of birth
    if city == 'chicago' or city == 'new york city':
        earliest_year = df['Birth Year'].min()
        print('The most earliest birth year:\n', earliest_year)
        most_recent = df['Birth Year'].max()
        print("The most recent birth year:\n", most_recent)
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print("The most common birth year:\n", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    d = 0
    while True:
        v = input('\nWould you like to view also five raws from data? "Y" OR "N"?\n>').lower()
        if v == 'n':
            break
        elif v == 'y':
            print(df[d:d+5])
            d = d + 5
        else:
            print('\nPlease enter "y" OR "N"!')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":

	main()
