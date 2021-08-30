import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_key = {'1':'chicago',
            '2':'new york city',
            '3':'washington'}
month_key = {'1':'january',
             '2':'february',
             '3':'march',
             '4':'april',
             '5':'may',
             '6':'june',
             '7':'july',
             '8':'august',
             '9':'september',
             '10':'october',
             '11':'november',
             '12':'december',
             'all':'all'}
day_key = {'1':'sunday',
           '2':'monday',
           '3':'tuesday',
           '4':'wednesday',
           '5':'thursday',
           '6':'friday',
           '7':'saturday',
           'all':'all'}
restart_key = {'y':'yes',
               'n':'no'}
def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!\n')
    
    city_numbers = city_key.keys()
    city_input = 0
        
    while city_input not in city_numbers:
        city_input = input('\nPlease choose one of the following cities by entering a number between 1-3\n (1) Chicago\n (2) New York City\n (3) Washington\n\nCity: ')
        if city_input in city_numbers:
            city = city_input
            break
        else:
            print(f'\nOops! {city_input} is not a number between 1 and 3. Please try again.')
    
    month_numbers = month_key.keys()
    month_input = 0
    
    while month_input not in month_numbers:
        month_input = input('\nPlease choose a month to filter by between 1-12 or "all"\n (1) January \n (2) February\n (3) March\n (4) April\n (5) May\n (6) June\n (7) July\n (8) August\n (9) September\n (10) October\n (11) November\n (12) December\n (all) No Filter\n\nMonth: ').lower()
        if month_input in month_numbers:
            month = month_input
            break
        else:
            print(f'\nOops! {month_input} is not a number between 1 and 12 or "all". Please try again.')
    day_numbers = day_key.keys()
    day_input = 0
    
    while day_input not in day_numbers:
        day_input = input('\nPlease choose a day of week to filter by between 1-7 or "all"\n (1) Sunday\n (2) Monday\n (3) Tuesday\n (4) Wednesday\n (5) Thursday\n (6) Friday\n (7) Saturday\n(all) No Filter\n\nDay of week: ').lower()
        if day_input in day_numbers:
            day = day_input
            break
        else:
            print(f'\nOops! {day_input} is not a number between 1 and 12 or "all". Please try again.')
            
    city = city_key[city]
    month = month_key[month]
    day = day_key[day]
    restart_numbers = restart_key.keys()
    restart_input = 0
     
    while restart_input not in restart_numbers:
        restart_input = input(f'\n Does this look correct? Enter Y or N.\n City: {city}\n Month: {month}\n Day: {day}\n').lower()
        if restart_input in restart_numbers:
            if restart_input == 'y':
                break
            else:
                restart_input = input('\n Would you like to start over?').lower()
                if restart_input in restart_numbers:
                    if restart_input == 'n':
                        break
                    else:
                        city,month,day = get_filters()
                else:
                    print('oops!')
        else:
            print('oops!')
   
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = (df['Start Time'].dt.strftime("%B")).str.lower()
    df['day'] = (df['Start Time'].dt.weekday_name).str.lower()
    
        
    if month != 'all':
        df['month'] = df['month']
        df = df[df['month'] == month]
        
    if day != 'all':
        df['day'] = df['day']
        df = df[df['day'] == day]
        
    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is',common_month)
    
    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('The most common day of week is',common_day)

    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df,city):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    common_lane_station = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    
    print(f'The most popular stations in {city.title()}... \n Start Station: {common_start_station} \n End Station: {common_end_station} \n Start to End Station: {common_lane_station}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df,city):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()

    print(f'{city.title()} travel time... \n Total: {total_travel} \n Mean: {mean_travel}')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        count_user = df['User Type'].value_counts().rename(None)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts().rename(None)
    else:
        count_gender = 'column not found'

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        early_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
    else:
        early_birth = 'column not found'
        recent_birth = 'column not found'
        common_birth = 'column not found'

    print(f'USER TYPE\n{count_user} \n\nGENDER\n{count_gender} \n\nYear of birth... \n +Earliest: {early_birth} \n +Most Recent: {recent_birth} \n +Most Common: {common_birth}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df,city)
        trip_duration_stats(df,city)
        user_stats(df)
        
        raw_data = input('\nWould you like to view five lines of raw data? Enter Y or N.\n')
        if raw_data.lower() == 'y':
            print(df.head())
        
        restart = input('\nWould you like to restart? Enter Y or N.\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
