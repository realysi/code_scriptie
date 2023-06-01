import os
import glob
import datetime

def csv_filenames(path_folder):
    """
    Returns a list with all the filenames that have the .csv extension
    """
    extension = 'csv'
    os.chdir(path_folder)
    filenames: list = glob.glob('*.{}'.format(extension))
    return filenames

def location_deepsqueak_file(filename_deepsqueak: str) -> str:
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

def deepsqueak_locations(path_folder):
    filenames = csv_filenames(path_folder)
    locations = []
    for i in filenames:
        #id_names.append(i.split('_202')[0]) ARTIS
        locations.append(i.split('_audio1')[0])
    locations = list(set(locations))
    return locations #not sorted on number