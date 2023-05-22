from code.read_data import read_csv
import datetime
import os
import copy
import pandas as pd

#AT THE MOMENT NOT TAKING START AND END DATES WITH AS DAYS OF RECORDING AGOUTI (WHICH IT PROBABLY IS) In DATES_BETWEEN()
def matching_dates(runtime_agouti, runtime_deespqueak) -> dict:
    agouti_data = agouti_recording_dates(runtime_agouti)
    deepsqueak_data = deepsqueak_recording_dates(runtime_deespqueak)
    shared_locations: list = overlapping_locations(agouti_data, deepsqueak_data)
    my_dict = {}
    for i in shared_locations:
        shared_dates = []
        dates_agouti = agouti_data[i]
        dates_deepsqueak = deepsqueak_data[i]
        for j in dates_agouti:
            if j in dates_deepsqueak:
                shared_dates.append(j)
        my_dict.update({i: shared_dates})

    locations = []
    values = []
    for a in my_dict.keys():
        value:list = my_dict[a]
        for b in range(len(value)):
            locations.append(a)
        values.extend(value)

    path = f"/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/data/matchingDates.csv"

    dictionary = {
        'matching_date': values,
        'locationName': locations,
        }
    df = pd.DataFrame(dictionary)
    df = df.sort_values('locationName')
    df.to_csv(path, index=False)
    return my_dict


def overlapping_locations(dict_agouti: dict, dict_deepsquak: dict):
    """
    check which IDs the agouti- and deepsqueakdata share, return those IDs.
    """
    dict_agouti_keys = list(dict_agouti.keys())
    dict_deepsquak_keys = list(dict_deepsquak.keys())
    overlapping_ids = []
    for i in dict_agouti_keys:
        if i in dict_deepsquak_keys:
            overlapping_ids.append(i)
    return overlapping_ids #['artis_26', 'artis_22', 'artis_24', 'artis_18', 'artis_20', 'artis_21', 'artis_19', 'artis_27']


def agouti_recording_dates(runtime_agouti) -> dict:
    #agouti dates of recording (startdate and enddate per deployment not taken with it (as it differt a couple of minutes and don't want to code that now))
    agouti = read_csv(runtime_agouti)
    locations = list(set(agouti.df['locationName'].tolist()))
    my_dict = {}
    for i in locations:
        dates = []
        data = copy.deepcopy(agouti)
        agouti_data = data.select_rows_by_columnvalue('locationName', i)
        starts = agouti_data.df['start_utc'].tolist() #2021-11-18 13:02:08, 2021-11-24 13:18:58
        ends = agouti_data.df['end_utc'].to_list() #2021-11-24 13:18:16, 2021-12-02 12:19:51
        for j in range(0, len(starts)):
            lijst = dates_between(starts[j], ends[j])
            dates.extend(lijst)
        my_dict.update({i: dates})
    return my_dict

def deepsqueak_recording_dates(runtime_deepsqueak):
    #deepsqueak dates of recording. I assume that every date that is mentioned started at 00:00:00 and ended at 23:59:59 as the deployment data of deepsqueak is different.
    deepsqueak = read_csv(runtime_deepsqueak)
    locations = list(set(deepsqueak.df['locationName'].tolist()))
    my_dict = {}
    for i in locations:
        data = copy.deepcopy(deepsqueak)
        deepsqueak_data = data.select_rows_by_columnvalue('locationName', i)
        dates = deepsqueak_data.df['start'].tolist()
        for j in range(0, len(dates)):
            dates[j] = dates[j].split(" ")[0]
        dates = list(set(dates))
        my_dict.update({i: dates})
    return my_dict

def utc_to_datetime(string):
    date, time = string.split(' ')
    year, month, day = date.split("-")
    hours, minutes, seconds = time.split(":")
    datetime_object: datetime.datetime = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hours), minute=int(minutes), second=int(seconds))
    return datetime_object

def dates_between(start_date, end_date):
    dates = []
    current_date = utc_to_datetime(start_date)
    current_date += datetime.timedelta(days=1)

    while current_date < utc_to_datetime(end_date):
        timestamps = str(current_date)
        date = timestamps.split(" ")[0]
        dates.append(str(date))
        current_date += datetime.timedelta(days=1)

    return dates


def oefenshit(dict_agouti, dict_deepsqueak_files) -> dict:
    """
    returns dictionary with {agouti_timestamp_possible overlap: deepsqueak_filename}
    """
    data = timestamps_overlaps(dict_agouti, dict_deepsqueak_files)  #--> dict of possible_overlaps {ID: [[timestamps_agouti_observering], [starttime_deepsqueak_observering]]}
    new_data = {}
    deepsqueak_filenames_overlaps = []
    for current_id in data.keys(): 
        files_deepsqueak_current_id = dict_deepsqueak_files[current_id]
        epoch_agoutidata:list = data[current_id][0] #both lists are the same length if everything is correct
        epoch_starttimes_deepsqueak: list = data[current_id][1]
        for j in range(0, len(epoch_agoutidata)):
            starttime_epoch = epoch_starttimes_deepsqueak[j]
            starttime_utc = str(datetime.datetime.fromtimestamp(starttime_epoch))
            date, time = starttime_utc.split(" ")
            time = time.replace(":", "-")
            filename = f"{current_id}_audio1_{date}_{time}"
            for file in files_deepsqueak_current_id:
                if filename in file:
                    deepsqueak_filenames_overlaps.append(file)
                    new_data.update({epoch_agoutidata[j]: file})
    print(new_data)
    return new_data

def timestamps_deepsqueak_to_epoch(filename_deepsqueak):
    timestamp = filename_deepsqueak.split('audio1_')[1]
    timestamp = timestamp.split("_(")[0]
    date, time = timestamp.split('_')
    year, month, day = date.split("-")
    hours, minutes, seconds = time.split("-")
    datetime_object: datetime.datetime = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hours), minute=int(minutes), second=int(seconds))
    epoch = datetime_object.timestamp()
    return epoch





def stap2(dict_agouti, dict_deepsqueak_files): #in the future folder_path as argument
    #interval hier checken
    data = oefenshit(dict_agouti, dict_deepsqueak_files) #{1637855589.0: 'flevopark_11_audio1_2021-11-25_16-00-00_(6) 2022-12-14  7_35 PM.csv', 1637856387.0: 'flevopark_11_audio1_2021-11-25_16-00-00_(6) 2022-12-14  7_35 PM.csv',}
    folder_path = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/flevopark_csv'

    #1. read in csv file of deepsqueak corresponding to possible overlap agouti timestamp
    for agouti_timestamp in data.keys():
        deepsqueak_filename = os.path.join(folder_path, data[agouti_timestamp])
        deepsqueak_starttime_epoch = timestamps_deepsqueak_to_epoch(deepsqueak_filename)
        deepsqueak_data = read_csv(deepsqueak_filename)
        #box1 = seconds since start recording | box2 = lowest frequency | box3 = duration | box4 = delta frequency


        #2. check if difference bigger than last sighting (last row box1) of deepsqueak
        difference = agouti_timestamp - deepsqueak_starttime_epoch
        seconds_since_starttime:list = deepsqueak_data.df['Box_1'].tolist()
        highest_value = max(seconds_since_starttime)
        if difference > highest_value:
            print("no overlap possible without bigger interval")


        """print(f"Starttime deepsqueak: {deepsqueak_starttime_epoch} | agouti timestamp: {agouti_timestamp}")
        print(f"Difference: {difference}")
        print(f"max: {highest_value}")
        print(deepsqueak_data.df)"""

