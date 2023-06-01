from code.read_data import read_csv
from code.hits import deepsqueak_observations, agouti_observations
from code.classes.dataframe_extension import Dataframe
import datetime
import os
import copy
import pandas as pd



def chances(deepsqueak_observations: Dataframe, agouti_observations: Dataframe, interval):
    ds_observations = deepsqueak_observations
    ag_observations = agouti_observations

    total_deepsqueak_observations = len(ds_observations.df)
    total_agouti_observations = len(ag_observations.df)

    audio_at_camera = 0
    camera_at_audio = 0

    locations = list(set(ag_observations.df['locationName'].tolist())) #locations in agouti
    for location in locations:
        intervals_audio_at_camera = []
        intervals_camera_at_audio = []

        ag_data = copy.deepcopy(ag_observations)
        ds_data = copy.deepcopy(ds_observations)

        ag_data.select_rows_by_columnvalue('locationName', location)
        ds_data.select_rows_by_columnvalue('locationName', location)

        agou_observations = ag_data.df['timestamps'].tolist() #all timestamps in a list.
        deeps_observations = ds_data.df['timestamps'].tolist()
        #audio observation at camera observation
        for ag_observation in agou_observations: #skips through timestamps
            ag_timestamp = ag_observation
            for ds_observation in deeps_observations:
                ds_timestamp = ds_observation
                if ag_timestamp - interval <= ds_timestamp <= ag_timestamp + interval or ds_timestamp == ag_timestamp:
                    intervals_audio_at_camera.append(ds_timestamp)
                    audio_at_camera += 1
                    break
        #camera observation at audio observation
        for ds_observation in deeps_observations: #skips through timestamps
            ds_timestamp = ds_observation
            for ag_observation in agou_observations:
                ag_timestamp = ag_observation
                if ds_timestamp - interval <= ag_timestamp <= ds_timestamp + interval or ag_timestamp == ds_timestamp:
                    intervals_camera_at_audio.append(ag_timestamp)
                    camera_at_audio += 1
                    break





        #my_data.update({location: intervals})
    chance_audio_atcamera = audio_at_camera / total_agouti_observations #in percentages
    chance_camera_ataudio = camera_at_audio / total_deepsqueak_observations #in percentages
    print(f'chance_audio_atcamera: {chance_audio_atcamera}')
    print(audio_at_camera, total_agouti_observations)
    print(f"chance camera at audio: {chance_camera_ataudio}")
    print(camera_at_audio, total_deepsqueak_observations)



def timestamps_deepsqueak_to_epoch(filename_deepsqueak):
    timestamp = filename_deepsqueak.split('audio1_')[1]
    timestamp = timestamp.split("_(")[0]
    date, time = timestamp.split('_')
    year, month, day = date.split("-")
    hours, minutes, seconds = time.split("-")
    datetime_object: datetime.datetime = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hours), minute=int(minutes), second=int(seconds))
    epoch = datetime_object.timestamp()
    return epoch


