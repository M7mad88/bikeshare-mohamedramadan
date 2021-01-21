import time
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'wa': 'washington.csv' }
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        try:
            city=input('\nTo view Bikeshare data, type:\n ch for chicago\n ny for new york city\n wa for washington\n').lower()
            if city in {'ch','ny','wa'}:
                break
        except KeyboardInterrupt:
            print('\nNO input taken?!')
        else:
            print('Invalid city choice\n')
    

    months=['january','february','march','april','may','june','all']
    month=input('\nTo filter {}\'s data by a particular month, please type the month or all:\n January\n February\n March\n April\n May\n June').lower()
    while month not in months:
        print('Invald month, please type a valid month or all.')
        month=input('\nTo filter {}\'s data by a particular month, please type the month or all:\n January\n February\n March\n April\n May\n June\n ').lower()
        
    days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
    day=input('\nTo filter {}\'s data by day, please type the day or all:\n Sunday\n Monday\n Tuesday\n Wednesday\n Thursday\n Friday\n Saturday\n').lower()
    while day not in days:
        print('Invald day, please type a valid day or all.')
        day=input('\nTo filter {}\'s data by day, please type the day or all:\n Sunday\n Monday\n Tuesday\n Wednesday\n Thursday\n Friday\n Saturday').lower()
        
        
    print('-'*40)
    return city, month, day


def load_data(city,month,day):
    
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
        df = df[df['day_of_week'] == day.title()]

    return df



def time_status(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel\n')
    start_time = time.time()
    
    # Display the most common month
    most_common_month=df['month'].mode()[0]
    print('The most common month is: ', most_common_month)
    
    #Display the most common day
    most_common_day=df['day_of_week'].mode()[0]
    print('The most common day is: ', most_common_day)
    
    #Display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    most_common_hour=df['hour'].mode()[0]
    print('The most common hour of day is: ',most_common_hour)
    
    print('\nThis took {} seconds.'.format(time.time()-start_time))
    print('-'*40)
    
    
def station_status(df):
    """Display statistics on the most popular stations and trip."""
    print('\nCalculating the most popular stations and trip.\n')
    start_time=time.time()
    #Display most commonly used start station
    
    start_station=df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: ',start_station)
    
    #Display most commonly used end station
    
    end_station=df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is: ',end_station)
    
    #Display most frequent combination of start and end stations.
    
    df['combination_station']=df['Start Station'] + ' '+df['End Station']
    print('The most frequent combination of start station and end station trip is: ',df['combination_station'].mode()[0])
    print('\nThis took {} seconds'.format(time.time()-start_time))
    print('-'*40)
    
def trip_duration_status(df):
    """Display statistics on the total & average trip duration."""
    
    print('\nCalculating trip duration.\n')
    start_time=time.time()
    
    #Display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total travel time is: ',total_travel_time)
    
    #Display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The total travel time is: ',mean_travel_time)
    
    print('\nThis took {} seconds'.format(time.time()-start_time))
    print('-'*40)
    
    
    
def user_status(df):
    """Display statistics on bikeshare users."""
    
    print('\nCalculating user stats.\n')
    start_time=time.time()
    #Display counts of user types
    
    user_types=df['User Type'].value_counts()
    print('The number of user types are: ',user_types)
    
    #Display counts of user types
    
    user_types=df['User Type'].value_counts()
    print('The number of user types are: ',user_types)
    
    #Display counts of gender 
    
    if 'Gender' in df.columns:
        gender_counts=df['Gender'].value_counts()
        print('The number of gender is: ',gender_counts)
        
    #Display year of birth
    
    if 'Birth Year' in df.columns:
        earliest_year=df['Birth Year'].min()
        print('The earlist year is: ',earliest_year)
        
        most_recent_year=df['Birth Year'].max()
        print('The most recent year is: ',most_recent_year)
        
        most_common_yearbirth=df['Birth Year'].value_counts().idxmax()
        print('The most common yearbirth is: ',most_common_yearbirth)
        
    print('\nThis took {} seconds'.format(time.time()-start_time))
    print('-'*40)
    
    
    
def display_raw_data(df):
    
    raw_data=input('Do you want to display some raw data? yes or no').lower()
    
    x=1
    
    while True:
        if raw_data=='yes':
            print(df.iloc[x : x+10])
            x+=10
            raw_data=input('\nDo you want to see more raw data? yes or no\n ').lower()
            
            
        else:
            break
            
def main():
    while True:
        city,month,day=get_filters()
        df=load_data(city,month,day)
        time_status(df)
        station_status(df)
        trip_duration_status(df)
        user_status(df)
        display_raw_data(df)
        
        restart=input('\nWould you like to restart? enter yes or no.\n')
        if restart.lower()!='yes':
            break
            
            
            
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    


        
    

            
    