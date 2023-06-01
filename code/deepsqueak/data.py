import os
import glob
import pandas as pd
from code.read_data import read_csv
import datetime
from code.classes.dataframe_extension import Dataframe
from code.deepsqueak.functions import csv_filenames, deepsqueak_locations

def deepsquakfiledata_to_dict(path_folder) -> dict:
    locations_deepsqueak = deepsqueak_locations(path_folder) #['artis_26_audio1', 'artis_19_audio1', etc]
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

