import os
import glob
import pandas as pd
from code.read_data import read_csv
import datetime
from code.classes.dataframe_extension import Dataframe

def csv_filenames(path_folder):
    """
    Returns a list with all the filenames that have the .csv extension
    """
    extension = 'csv'
    os.chdir(path_folder)
    filenames: list = glob.glob('*.{}'.format(extension))
    return filenames

def location_deepsqueak_file(filename_deepsqueak) -> str:
    """
    Grabs the location of the camera from the filename. flevopark_1_audio1_2021-09-28_16-00-00_(0) 2023-01-23 12_44 PM.csv --> flevopark_1
    """
    location = filename_deepsqueak.split('_audio1')[0]
    return location

def timestamps_deepsqueak_to_datetime(filename_deepsqueak):
    """
    Turns the timestamps in the deepsqueak filename into a datetime object. flevopark_1_audio1_2021-09-28_16-00-00_(0) 2023-01-23 12_44 PM.csv --> 2021-09-28 16:00:00
    """
    timestamp = filename_deepsqueak.split('audio1_')[1]
    timestamp = timestamp.split("_(")[0]
    date, time = timestamp.split('_')
    year, month, day = date.split("-")
    hours, minutes, seconds = time.split("-")
    datetime_object: datetime.datetime = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hours), minute=int(minutes), second=int(seconds))
    return datetime_object

def datetime_to_epoch(datetime_object: datetime.datetime):
    """
    Turns datetime object into epoch. 2021-09-28 16:00:00 --> 13480123 etc.
    """
    epoch = datetime_object.timestamp()
    return epoch

def recordings(path_folder, location_data):
    """
    Creates a csv(runtime_flevopark) with information of each recording. LocationName | start_recording | end_recording | runtime (seconds)
    """
    starttimes, endtimes, runtime, location = [], [], [], []
    files = csv_filenames(path_folder)
    for file in files:
        current_data = read_csv(file)
        observations: list = current_data.df['Box_1'].tolist()
        last_observation = round(max(observations))
        current_location = location_deepsqueak_file(file)
        start = timestamps_deepsqueak_to_datetime(file)
        end = start + datetime.timedelta(seconds=last_observation)
        run_time = abs(datetime_to_epoch(start) - datetime_to_epoch(end))
        starttimes.append(start)
        endtimes.append(end)
        runtime.append(run_time)
        location.append(current_location)

    data = {
    'locationName': location,
    'start': starttimes,
    'end': endtimes,
    'runtime (sec)': runtime 
    }
    df = pd.DataFrame(data)
    df = df.sort_values('locationName')
    path = f"/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/deepsqueak/runtime_{location_data}.csv"
    df.to_csv(path, index=False)
    return df

def total_runtime(pddataframe):
    """
    returns dictionary with total runtime per location and total recordings. {flevopark_1: [3 days 1:36:56, 52}.
    """
    data = Dataframe(pddataframe)
    data = data.total_runtime_per_location()
    print(data)
    return data

def observations_per_location_no_interval(path_folder, interval_seconds):
    """
    interval is what amounts to one 1 sighting
    Returns the amount of observations per location {location: [total observations, epoch observations]}
    """
    data = {}
    files = csv_filenames(path_folder)

    timestamps = []
    locations = []
    observations_count = []

    total_length_observations = 0
    for file in files:
        current_data = read_csv(file)
        start = timestamps_deepsqueak_to_datetime(file)

        observations: list = current_data.df['Box_1'].tolist()
        total_length_observations += len(observations)
        #start with first observation 
        location = location_deepsqueak_file(file)
        timestamp = []
        total_observations_now = 0
        end_interval = 0
        for i in range(0, len(observations)):
                if observations[i] > end_interval:
                    total_observations_now += 1
                    timestamp_observation_epoch = datetime_to_epoch(start) + observations[i]
                    timestamp.append(timestamp_observation_epoch)
                    end_interval = observations[i] + interval_seconds
                else:
                    continue

        timestamps.extend(timestamp)
        for j in range(len(timestamp)):
            observations_count.append(total_observations_now)
            locations.append(location)
    path = f"/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/deepsqueak/{interval_seconds}s_{len(timestamps)}obs_interval_observationInfo.csv"

    dictionary = {
        'locationName': locations,
        'total_observations': observations_count,
        'timestamps': timestamps
        }
    df = pd.DataFrame(dictionary)
    df = df.sort_values('locationName')
    df.to_csv(path, index=False)
    

    "Write this data per location to a csv file!!!!!!!"
    #print(data)
    return(data)


def info(path_folder, location_data):
    df = recordings(path_folder, location_data)
    runtimes = total_runtime(df)

def info_per_location(path_folder, location_data):
    pass


def locations(path_folder):
    filenames = csv_filenames(path_folder)
    locations = []
    for i in filenames:
        #id_names.append(i.split('_202')[0]) ARTIS
        locations.append(i.split('_audio1')[0])
    locations = list(set(locations))
    return locations #not sorted on number

def deepsquakfiledata_to_dict(path_folder) -> dict:
    locations_deepsqueak = locations(path_folder) #['artis_26_audio1', 'artis_19_audio1', etc]
    files: list = csv_filenames(path_folder) #['artis_26_audio1_2021-10-09_16-00-00_(19) 2022-12-14  5_39 PM.csv', etc]
    data = {}
    for location in locations_deepsqueak:
        filenames_per_location = []
        for file in files:
            file_location = file.split("_audio1")[0]
            if location == file_location:
                filenames_per_location.append(file)
        data.update({location: filenames_per_location}) #{flevopark_1: [filename, filename, filename]}            {'artis_26_audio1': ['artis_26_audio1_2021-10-09_16-00-00_(19) 2022-12-14  5_39 PM.csv', etc]}
    return data
    


"4 mei: vandaag: - code opgeschoond, agouti data nu in dictionary, deepsquak files begin daaraan (files kunnen worden ingelezen)"
