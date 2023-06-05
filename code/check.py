import os
import glob
import shutil
import sys
import pandas as pd

def check(path_folder_agouti, path_folder_deepsqueak):
    """
    Checks data of agouti (folder and csv file itself for columns) and deepsqueak (columns)
    Returns list of paths [media, deployments, observations]"""
    paths = check_agouti_folder(path_folder_agouti)
    check_media_columns(paths[0])
    check_deployments_columns(paths[1])
    check_observations_columns(paths[2])
    check_deepsqueak_columns(path_folder_deepsqueak)
    return paths

def check_agouti_folder(path_folder_agouti):
    """
    check if media.csv deployments.csv and observatoins.csv are in the data.
    if checks is good, return list with paths [media, deployments, observations]
    """
    files_in_folder = glob.glob(f'{path_folder_agouti}/*')
    if f'{path_folder_agouti}/deployments.csv' and f'{path_folder_agouti}/media.csv' and f'{path_folder_agouti}/observations.csv' not in files_in_folder:
        raise Exception("The agouti data does not contain the three required csv files: media.csv, deployments.csv & observations.csv")
    else:
        paths = [f'{path_folder_agouti}/media.csv', f'{path_folder_agouti}/deployments.csv', f'{path_folder_agouti}/observations.csv']
        return paths
    
def check_deepsqueak_columns(path_folder_deepsqueak):
    """
    checks if the deepsqueak files contain the right columns
    """
    #do this were deepsqueak data gets processed --> check for name in folders location_cameraID_audio_1_year-month-day_hour-minute-seconds_(0) etc (dit is enige belangrijke)
    column_names_required = ['Box_1','Box_2','Box_3','Box_4','Score','Type','Accept']
    files_in_folder = glob.glob(f'{path_folder_deepsqueak}/*.csv')
    for file_name in files_in_folder:
        file_data = pd.read_csv(file_name)
        column_names_file = list(file_data.columns)
        if column_names_required != column_names_file:
            raise Exception("The csv file does either not have the following columns in the correct order, or are missing them al at: 'Box_1','Box_2','Box_3','Box_4','Score','Type','Accept' ")

def check_media_columns(path_media):
    """
    checks if the media.csv file contains the right columns
    """
    columns_names_required = ['sequenceID', 'fileName']
    media_data = pd.read_csv(path_media, low_memory=False)
    column_names_file = list(media_data.columns)
    for column in columns_names_required:
        if column not in column_names_file:
            raise Exception(f"The media.csv file from the agouti data does not contain the {column}. This column is required to filter the data.")
        
def check_observations_columns(path_observations):
    """
    checks if the observations.csv file contains the right columns
    """
    columns_names_required = ['deploymentID', 'sequenceID', 'scientificName', 'timestamp']
    media_data = pd.read_csv(path_observations)
    column_names_file = list(media_data.columns)
    for column in columns_names_required:
        if column not in column_names_file:
            raise Exception(f"The observations.csv file from the agouti data does not contain the {column}. This column is required to filter the data.")
        
def check_deployments_columns(path_deployments):
    """
    checks if the deployments.csv file contains the right columns
    """
    columns_names_required = ['deploymentID', 'longitude', 'latitude', 'locationName', 'cameraID']
    media_data = pd.read_csv(path_deployments)
    column_names_file = list(media_data.columns)
    for column in columns_names_required:
        if column not in column_names_file:
            raise Exception(f"The deployments.csv file from the agouti data does not contain the {column}. This column is required to filter the data.")
        