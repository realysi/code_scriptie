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

def datetime_epoch(datetime_object: datetime.datetime):
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
        #end = start + last_observation
        end = start + datetime.timedelta(seconds=last_observation)
        run_time = abs(datetime_epoch(start) - datetime_epoch(end))
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
    Returns the amount of observations per location
    """
    data = {}
    files = csv_filenames(path_folder)
    for file in files:
        current_data = read_csv(file)
        start = timestamps_deepsqueak_to_datetime(file)
        timestamps = []
        observations: list[float] = current_data.df['Box_1'].tolist()
        #start with first observation
        total_observations = 0
        end_interval = 0
        for i in range(0, len(observations)):
                if observations[i] > end_interval:
                    total_observations += 1
                    timestamp_observation_epoch = datetime_epoch(start) + observations[i]
                    timestamps.append(timestamp_observation_epoch)
                    end_interval = observations[i] + interval_seconds
                else:
                    continue

        location = location_deepsqueak_file(file)
        if location in data.keys():
            old_value = data[location][0]
            old_timestamps: list = data[location][1]
            old_timestamps.extend(timestamps)
            data.update({location: [old_value + total_observations, old_timestamps]})
        else:
            data.update({location: [total_observations, timestamps]})


        "Write this data per location to a csv file!!!!!!!"
    print(data)
    return(data)


def info(path_folder, location_data):
    df = recordings(path_folder, location_data)
    runtimes = total_runtime(df)


"""def runtime_location(path_folder, location_data):
    data = {}
    df = recordings(path_folder, location_data)
    locations = list(set(df['locationName'].tolist()))
    for location in locations:
        total_runtime = 0
        rows = df.loc[df['locationName'] == location]
        for i in rows.index:
            runtime = rows.loc[i, 'runtime']
            total_runtime += runtime
        data.update({location: total_runtime})
    return data"""

def info_per_location(path_folder, location_data):
    pass


def id_names(path_folder):
    filenames = csv_filenames(path_folder)
    id_names = []
    for i in filenames:
        #id_names.append(i.split('_202')[0]) ARTIS
        id_names.append(i.split('_audio1')[0])
    id_names = list(set(id_names))
    return id_names #not sorted on number

def deepsquakfiledata_to_dict(path_folder) -> dict:
    names_id = id_names(path_folder) #['artis_26_audio1', 'artis_19_audio1', etc]
    files: list = csv_filenames(path_folder) #['artis_26_audio1_2021-10-09_16-00-00_(19) 2022-12-14  5_39 PM.csv', etc]
    data = {}
    for name in names_id:
        filenames_with_id = []
        for file in files:
            if name in file:
                filenames_with_id.append(file)
        data.update({name: filenames_with_id}) #{flevopark_1: [filename, filename, filename]}            {'artis_26_audio1': ['artis_26_audio1_2021-10-09_16-00-00_(19) 2022-12-14  5_39 PM.csv', etc]}
    return data
    
    for h in data:
       print(f"key: {h}, values: {data[h]} \n\n")


"4 mei: vandaag: - code opgeschoond, agouti data nu in dictionary, deepsquak files begin daaraan (files kunnen worden ingelezen)"
