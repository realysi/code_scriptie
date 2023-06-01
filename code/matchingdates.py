from code.read_data import read_csv
from code.classes.dataframe_extension import Dataframe
import datetime
import copy
import pandas as pd


"""
Important notes:
1. The starting and ending dates of the depolyment from the agouti data are not taken into account, as these days are not complete.
This can be fixed in the future, but is for now postponed to save some time.
2. For the deepsqueak data it is assumed that if a date is named in a filename, the audioMoth recorded for the whole day.
This probably isn't true, as most intervals between the audio files is about 2,5 hours. But this isn't consistent, so 20:49
the day before to 5:00 is a possible recording.
"""

#AT THE MOMENT NOT TAKING START AND END DATES WITH AS DAYS OF RECORDING AGOUTI (WHICH IT PROBABLY IS) In DATES_BETWEEN()
def matching_dates(agouti_runtime: Dataframe, deepsqueak_runtime: Dataframe) -> dict[str, list[str]]: #bvb {flevopark_7 : ['2021-09-17', etc}
    """
    Returns dictionary with location as key and the matching dates for that location as values
    {location: [date, date]}. Also writes it to a csv file: matchingDates
    """
    agouti_data = agouti_recording_dates(agouti_runtime)
    deepsqueak_data = deepsqueak_recording_dates(deepsqueak_runtime)
    matching_dates: dict[str, list[str]]  = find_dates(agouti_data, deepsqueak_data)
    matching_dates_csv(matching_dates)
    return matching_dates

#1
def dates_between(start_date: str, end_date: str) -> list[str]:
    """
    Return a list with the dates between the start_date and the end_date
    """
    dates = []
    current_date: datetime.datetime = string_to_datetime(start_date)
    current_date += datetime.timedelta(days=1) #skip first day of recordings

    while current_date < string_to_datetime(end_date): #<= if also want to include endday
        timestamps = str(current_date)
        date = timestamps.split(" ")[0]
        dates.append(str(date))
        current_date += datetime.timedelta(days=1)

    return dates

#2
def agouti_recording_dates(agouti_runtime_dataframe: Dataframe) -> dict[str, list[str]]: #{location: [2021-11-24, etc]}
    """
    Returns a dictionary {location: [date, date]} with the dates that the camera recorded for 24 hours (see notes above)
    """
    info_recordings: Dataframe = agouti_runtime_dataframe
    locations = list(set(info_recordings.df['locationName'].tolist()))
    my_dict = {}
    for location in locations:
        dates = []
        data = copy.deepcopy(info_recordings)
        info_location: Dataframe = data.select_rows_by_columnvalue('locationName', location)
        start_dates: list[str] = info_location.df['start_utc'].tolist() #[2021-11-18 13:02:08, 2021-11-24 13:18:58, etc]
        end_dates: list[str] = info_location.df['end_utc'].to_list() #[2021-11-24 13:18:16, 2021-12-02 12:19:51, etc]
        for i in range(0, len(start_dates)):
            dates_inbetween = dates_between(start_dates[i], end_dates[i])
            dates.extend(dates_inbetween)
        my_dict.update({location: dates})
    return my_dict

#3
def deepsqueak_recording_dates(deepsqueak_runtime_dataframe) -> dict[str, list[str]]:
    """
    Returns a dictionary {location: [date, date]} with the dates that the audio recorded. For specifications, see the notes above.
    """
    info_recordings: Dataframe = deepsqueak_runtime_dataframe
    locations = list(set(info_recordings.df['locationName'].tolist()))
    my_dict = {}
    for location in locations:
        data = copy.deepcopy(info_recordings)
        info_location: Dataframe = data.select_rows_by_columnvalue('locationName', location)
        dates = info_location.df['start'].tolist()
        for i in range(0, len(dates)):
            dates[i] = str(dates[i]).split(" ")[0]
        dates = list(set(dates))
        my_dict.update({location: dates})
    return my_dict

#4
def matching_locations(dict_agouti: dict, dict_deepsquak: dict):
    """
    check which IDs the agouti- and deepsqueakdata share, return those IDs.
    """
    dict_agouti_keys = list(dict_agouti.keys())
    dict_deepsquak_keys = list(dict_deepsquak.keys())
    overlapping_locations = []
    for i in dict_agouti_keys:
        if i in dict_deepsquak_keys:
            overlapping_locations.append(i)
    return overlapping_locations

#5
def find_dates(dict_agouti_dates, dict_deepsqueak_dates) -> dict[str, list[str]]: #agouti: {flevopark_7 : ['2021-09-17', etc]} deepsqueak = hetzelfde
    """
    Finds the dates that match per location from the agouti and deepsqueak data set
    """
    my_dict = {}
    matched_locations: list = matching_locations(dict_agouti_dates, dict_deepsqueak_dates)
    for location in matched_locations:
        shared_dates = []
        dates_agouti: list[str] = dict_agouti_dates[location]
        dates_deepsqueak: list[str] = dict_deepsqueak_dates[location]
        for date_agouti in dates_agouti:
            if date_agouti in dates_deepsqueak:
                shared_dates.append(date_agouti)
        my_dict.update({location: shared_dates})
    return my_dict #bvb {flevopark_7 : ['2021-09-17', etc}
    
#6
def matching_dates_csv(dict_shared_dates): #bvb {flevopark_7 : ['2021-09-17', etc}
    """
    Writes the data stored in a dictionary from find_dates() to a csv format.
    """
    locations = []
    values = []
    for key in dict_shared_dates.keys():
        value: list[str] = dict_shared_dates[key]
        for i in range(len(value)):
            locations.append(key)
        values.extend(value)
    dictionary = {'matching_date': values, 'locationName': locations}
    df = pd.DataFrame(dictionary)
    df = df.sort_values('locationName')
    df.to_csv("/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/data/matchingDates.csv", index=False)




def string_to_datetime(string: str) -> datetime.datetime:
    """
    Transforms a string of format yy-mm-day hh:mm:ss to a datetime.datetime object
    """
    date, time = str(string).split(' ')
    year, month, day = date.split("-")
    hours, minutes, seconds = time.split(":")
    datetime_object: datetime.datetime = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hours), minute=int(minutes), second=int(seconds))
    return datetime_object

