from code.read_data import read_csv
import datetime
import os
import copy
import pandas as pd

"""
def test(dict_agouti, dict_deepsqueak_files) -> dict:

    returns dictionary with {agouti_timestamp_possible overlap: deepsqueak_filename}

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
    return new_data"""

def timestamps_deepsqueak_to_epoch(filename_deepsqueak):
    timestamp = filename_deepsqueak.split('audio1_')[1]
    timestamp = timestamp.split("_(")[0]
    date, time = timestamp.split('_')
    year, month, day = date.split("-")
    hours, minutes, seconds = time.split("-")
    datetime_object: datetime.datetime = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hours), minute=int(minutes), second=int(seconds))
    epoch = datetime_object.timestamp()
    return epoch



"""
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


        print(f"Starttime deepsqueak: {deepsqueak_starttime_epoch} | agouti timestamp: {agouti_timestamp}")
        print(f"Difference: {difference}")
        print(f"max: {highest_value}")
        print(deepsqueak_data.df)"""

