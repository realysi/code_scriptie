import pandas as pd
from code.hits import agouti_observations, deepsqueak_observations
from code.matchingdates import matching_dates
from code.classes.dataframe_extension import Dataframe
import copy
import datetime
import matplotlib.pyplot as plt
import pytz

def total_observations(observation: pd.DataFrame):
    total_observations = len(observation['timestamps'].tolist())
    return total_observations


"""def total_runtime(agouti_runtime, deepsqueak_runtime):

    dates = matching_dates(agouti_runtime, deepsqueak_runtime)
    total_dates = 0
    for location in dates.keys():
        total_dates += len(dates[location])
    total_hours = total_dates / 24.0
    return total_hours"""


def observations_location(observations: pd.DataFrame):
    """
    Returns total observations per location agouti
    """
    my_dict = {}
    data = Dataframe(observations)
    locations = list(set(data.df['locationName'].tolist()))
    for location in locations:
        copy_data = copy.deepcopy(data)
        copy_data.select_rows_by_columnvalue('locationName', location)
        observations_per_location = len(copy_data.df)
        my_dict.update({location: observations_per_location})
    return my_dict

def info(observations):
    info_location = observations_location(observations)
    tot_observations = total_observations(observations)


def hours(data: Dataframe):
    timestamps_observations = data.df['timestamps'].tolist()
    list_hours = []
    for timestamp in timestamps_observations:
        # Convert the epoch timestamp to a UTC datetime object
        utc_datetime = datetime.datetime.utcfromtimestamp(timestamp)
        amsterdam_tz = pytz.timezone('Europe/Amsterdam')
        
        amsterdam_tz = pytz.timezone('Europe/Amsterdam')
        amsterdam_time = amsterdam_tz.localize(utc_datetime)

        hour_extra_amsterdam = str(amsterdam_time).split('+')[1]
        hour_extra_amsterdam = int(hour_extra_amsterdam.split(':')[0])

        utc_hour = utc_datetime.hour
        ams_hour = utc_hour + hour_extra_amsterdam

        list_hours.append(ams_hour)
    return list_hours

def amount_hours(hours: list):
    hours_spread = {}

    all_hours = list(range(24))

    total_count = 0
    for i in all_hours:
        current_count = 0 
        for hour in hours:
            if hour == i:
                current_count += 1
        hours_spread.update({i: current_count/len(hours)})
    return hours_spread

def hour_day(data_agouti: Dataframe, data_deepsqueak: Dataframe, path_results):
    #find out when converted to other timezones!!!!!!
    agouti_hours = hours(data_agouti)
    deepsqueak_hours = hours(data_deepsqueak)

    #calculates how many times each our is in the dataset. also total observations --> percentage can be calculated.


    #MAKE IT PERCENTAGES --> EASIER TO SEE THAN PROPORTION????
    agouti_spread = amount_hours(agouti_hours)
    deepsqueak_spread = amount_hours(deepsqueak_hours)

    bar_width = 0.40

    agouti_hours_keys = list(agouti_spread.keys())
    agouti_hours_values = list(agouti_spread.values())

    positions = range(len(agouti_hours_keys))
    postions_agouti, postions_deepsqueak = [], []
    for i in positions:
            postions_agouti.append(i - bar_width/2)
            postions_deepsqueak.append(i + bar_width/2)

    deepsqueak_hours_keys = list(deepsqueak_spread.keys())
    deepsqueak_hours_values = list(deepsqueak_spread.values())

    #should be done in proportions and deepsqueak and agouti on 1 
    plt.bar(x=postions_agouti ,height=agouti_hours_values, width=bar_width, tick_label=agouti_hours_keys, color='black')
    plt.bar(x=postions_deepsqueak, height=deepsqueak_hours_values, width=bar_width, tick_label=deepsqueak_hours_keys, color='gray')
    plt.xlabel("hour of day")
    plt.ylabel("proportion of observations")
    plt.legend(["CT", 'PAM'])
    plt.title("daily activity pattern Rattus Norvegicus")
    plt.savefig(f'{path_results}/data/daily activity pattern Rattus Norvegicus')


    'https://www.researchgate.net/figure/The-daily-activity-pattern-for-one-nocturnal-and-one-diurnal-animal-species-for-a-BCI_fig3_46588027'

#recorded in utc + 1 --> now in utc --> change to amsterdam time
