from code.read_data import read_csv
from code.classes.dataframe_extension import Dataframe
import datetime
import copy
import pandas as pd
#from code.matchingdates import dates_between
from code.read_data import read_csv
from code.classes.dataframe_extension import Dataframe
import datetime
import copy
import pandas as pd
from code.matchingdates import string_to_datetime, matching_locations, agouti_recording_dates, deepsqueak_recording_dates, matching_dates_csv


#Transforms a string of format yy-mm-day hh:mm:ss to a datetime.datetime object
def dates_between(start_date: str, end_date: str) -> list[str]:
    """
    Return a list with the dates between the start_date and the end_date
    """
    dates = []
    current_date: datetime.datetime = string_to_datetime(start_date)
    #current_date += datetime.timedelta(days=1) #skip first day of recordings

    while current_date < string_to_datetime(end_date): #<= if also want to include endday
        timestamps = str(current_date)
        date = timestamps.split(" ")[0]
        dates.append(str(date))
        current_date += datetime.timedelta(days=1)

    return dates


def dates_study(agouti_runtime, deespqueak_runtime, path_resutls):
    """
    {location: [all dates]}
    """
    my_dict = {}
    agouti_dict = agouti_recording_dates(agouti_runtime)
    deepsqueak_dict = deepsqueak_recording_dates(deespqueak_runtime)
    locations = matching_locations(agouti_dict, deepsqueak_dict)
    dates = dates_between('2021-11-24 00:00:00', '2021-12-02 23:59:59')

    for i in locations:
        my_dict.update({i: dates})


    matching_dates_csv(my_dict, path_resutls)
    return my_dict

#split total time period up into lenght of all_dates -> note for the day which locations had an observation
def occupancy_matrix_agouti(dates, observations_agouti: Dataframe, path_results, dates_per_location_recorded: dict[str, list[str]]):
    """
    returns (is the plan)
    -------------2021-09-01 2021-09-02
    flevopark_13     0          1
    flevopark_9      0          0
    """
    locations = list(dates.keys())
    locations = sorted(locations, key=lambda x: int(x.split('_')[1]))
    values = dates_between('2021-11-24 00:00:00', '2021-12-02 23:59:59')

    df = pd.DataFrame(columns=values, index=locations)

    total_observations = 0
    for date in values:
        for location in locations:
            camera_data = copy.deepcopy(observations_agouti)
            #select by location
            camera_data.select_rows_by_columnvalue(columnname='locationName', columnvalue=location)
            #check if there was a hit at date
            if date not in dates_per_location_recorded[location]:
                result = 'NA'
                continue
            elif camera_data.df['filename'].str.contains(date).any():
                result = 1
                total_observations += 1
            else:
                result = 0
            df.at[location, date] = result

    df.to_csv(f"{path_results}/agouti/occupancy_matrix.csv", index=True, na_rep='NA')

    return total_observations

def occupancy_matrix_deepsqueak(dates, observations_deepsqueak: Dataframe, path_results, dates_per_location_recorded):
    """
    returns (is the plan)
    -------------2021-09-01 2021-09-02
    flevopark_13     0          1
    flevopark_9      0          0
    """
    locations = list(dates.keys())
    locations = sorted(locations, key=lambda x: int(x.split('_')[1]))
    values = dates_between('2021-11-24 00:00:00', '2021-12-02 23:59:59')

    #df = pd.DataFrame(columns=values, index=locations)
    df = pd.DataFrame(columns=values, index=locations)

    total_observations = 0
    for date in values:
        for location in locations:
            camera_data = copy.deepcopy(observations_deepsqueak)
            #select by location
            camera_data.select_rows_by_columnvalue(columnname='locationName', columnvalue=location)
            #check if there was a hit at date
            if date not in dates_per_location_recorded[location]:
                result = 'NA'
                continue
            elif camera_data.df['filename'].str.contains(date).any():
                result = 1
                total_observations += 1
            else:
                result = 0
            df.at[location, date] = result

    df.to_csv(f"{path_results}/deepsqueak/occupancy_matrix.csv", index=True, na_rep='NA')

    return total_observations

def occupancy_matrix_agouti_test(dates, dates_dates, observations_agouti: Dataframe, path_results, dates_per_location_recorded: dict[str, list[str]]):
    """
    returns (is the plan)
    -------------2021-09-01 2021-09-02
    flevopark_13     0          1
    flevopark_9      0          0
    """
    locations = list(dates.keys())
    locations = sorted(locations, key=lambda x: int(x.split('_')[1]))
    values = dates_between('2021-09-10 00:00:00', '2021-10-11 23:59:59')

    df = pd.DataFrame(columns=dates_dates, index=locations)

    total_observations = 0
    for date in dates_dates:
        for location in locations:
            camera_data = copy.deepcopy(observations_agouti)
            #select by location
            camera_data.select_rows_by_columnvalue(columnname='locationName', columnvalue=location)
            #check if there was a hit at date
            if date not in dates_per_location_recorded[location]:
                result = 'NA'
                continue
            elif camera_data.df['filename'].str.contains(date).any():
                result = 1
                total_observations += 1
            else:
                result = 0
            df.at[location, date] = result

    df.to_csv(f"{path_results}/agouti/occupancy_matrix.csv", index=True, na_rep='NA')

    return total_observations

def occupancy_matrix_deepsqueak_test(dates, dates_dates, observations_deepsqueak: Dataframe, path_results, dates_per_location_recorded):
    """
    returns (is the plan)
    -------------2021-09-01 2021-09-02
    flevopark_13     0          1
    flevopark_9      0          0
    """
    locations = list(dates.keys())
    locations = sorted(locations, key=lambda x: int(x.split('_')[1]))
    values = dates_between('2021-09-10 00:00:00', '2021-10-11 23:59:59')

    #df = pd.DataFrame(columns=values, index=locations)
    df = pd.DataFrame(columns=dates_dates, index=locations)

    total_observations = 0
    for date in dates_dates:
        for location in locations:
            camera_data = copy.deepcopy(observations_deepsqueak)
            #select by location
            camera_data.select_rows_by_columnvalue(columnname='locationName', columnvalue=location)
            #check if there was a hit at date
            if date not in dates_per_location_recorded[location]:
                result = 'NA'
                continue
            
            elif camera_data.df['filename'].str.contains(date).any():
                result = 1
                total_observations += 1
            else:
                result = 0
            df.at[location, date] = result

    df.to_csv(f"{path_results}/deepsqueak/occupancy_matrix.csv", index=True, na_rep='NA')

    return total_observations
def agouti_dates(runtime_agouti: Dataframe):
    """
    {location: [date recorded, date recorded]}
    """
    my_dict = {}
    locations = list(set(runtime_agouti.df['locationName'].to_list()))
    locations = sorted(locations, key=lambda x: int(x.split('_')[1]))

    for location in locations:
        dates = []
        runtime_location = copy.deepcopy(runtime_agouti)
        runtime_location.select_rows_by_columnvalue(columnname='locationName', columnvalue=location)

        for i in runtime_location.df.index: 
            start_date = str(runtime_location.df.loc[i, 'start_utc'])
            end_date = str(runtime_location.df.loc[i, 'end_utc'])
            dates_recorderd: list[str] = dates_between(start_date, end_date)
            dates.extend(dates_recorderd)

        my_dict.update({location: dates})

    return my_dict

def deepsqueak_dates(runtime_deepsqueak: Dataframe):
    """
    {location: [date recorded, date recorded]}
    """
    my_dict = {}
    locations = list(set(runtime_deepsqueak.df['locationName'].to_list()))
    locations = sorted(locations, key=lambda x: int(x.split('_')[1]))

    for location in locations:
        dates = []
        runtime_location = copy.deepcopy(runtime_deepsqueak)
        runtime_location.select_rows_by_columnvalue(columnname='locationName', columnvalue=location)

        for i in runtime_location.df.index: 
            date = str(runtime_location.df.loc[i, 'start'])
            dates.append(date.split(" ")[0])

        dates = list(set(dates))
        my_dict.update({location: dates})

    return my_dict

def all_deepsqueak_dates(runtime_deepsqueak):
    """
    {location: [date recorded, date recorded]}
    """
    my_dict = {}
    locations = list(set(runtime_deepsqueak.df['locationName'].to_list()))
    locations = sorted(locations, key=lambda x: int(x.split('_')[1]))
    dates_timestamps = list(set(runtime_deepsqueak.df['start'].to_list()))
    dates = []
    for i in dates_timestamps:
        date_time = str(i)
        date = date_time.split(" ")[0]
        dates.append(date)

    dates = list(set(dates))

    for location in locations:
        my_dict.update({location: dates})
    return my_dict

def all_deepsqueak_dates_list(runtime_deepsqueak):
    """
    {location: [date recorded, date recorded]}
    """
    dates_timestamps = list(set(runtime_deepsqueak.df['start'].to_list()))
    dates = []
    for i in dates_timestamps:
        date_time = str(i)
        date = date_time.split(" ")[0]
        dates.append(date)

    dates = list(set(dates))

    return dates

#agouti
#0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

#deepsqueak
#0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

#0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1