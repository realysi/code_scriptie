from code.agouti.filter import data_aougti_test #at the end of project, remove data_agouti_test and rename _final to just data_agouti
from deepsqueak.data import deepsquakfiledata_to_dict
import datetime

linked_data_agouti_flevopark = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/flevopark+mediadata.csv'
flevopark_folder_deepsqueak = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/flevopark_csv'

agoutidata = data_aougti_test(linked_data_agouti_flevopark) #{ID: pd.Dataframe}
deepsquakfiledata = deepsquakfiledata_to_dict(flevopark_folder_deepsqueak) #{ID: [filename, filename]}

#Step 1: check if they have same ID, if so put that id in a list
def overlapping_id(dict_agouti: dict, dict_deepsquak: dict):
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

def epoch_timestamps_deepsqueak(dict_agouti, dict_deepsqueak):
    """
    Turns the timestamps in the filenames of the deepsqueak files into epoch timestmaps for every overlapping ID.
    Saves it in new dictionary timestamps_id {ID: list[epoch, epoch, epoch]}
    """
    ids = overlapping_id(dict_agouti, dict_deepsqueak)
    timestamps_id = {}
    for i in ids: 
        filenames_deepsquak: list[str] = dict_deepsqueak[f"{i}"] #[f"{i}_audio1"] for artis ['artis_26_audio1_2021-10-09_16-00-00_(19) 2022-12-14  5_39 PM.csv', etc]
        epoch_timestamps_deepsquak = []
        for file in filenames_deepsquak:
            timestamp = file.split('audio1_')[1]
            timestamp = timestamp.split("_(")[0]
            date, time = timestamp.split('_')
            year, month, day = date.split("-")
            hours, minutes, seconds = time.split("-")
            datetime_object: datetime.datetime = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hours), minute=int(minutes), second=int(seconds))
            epoch = datetime_object.timestamp()
            epoch_timestamps_deepsquak.append(epoch)
        timestamps_id.update({i: epoch_timestamps_deepsquak})
    return timestamps_id

def timestamps_overlaps(dict_agouti, dict_deepsqueak):
    """
    --> dict of possible_overlaps {ID: [[timestamps_agouti_observering], [starttime_deepsqueak_observering]]}
    """
    overlaps = {}
    epoch_timestamps: dict = epoch_timestamps_deepsqueak(dict_agouti, dict_deepsqueak) #{ID: list[epoch, epoch]
    for i in epoch_timestamps.keys():
        starttimes_overlaps = []
        timestamps_id_data = []
        rows_agouti = dict_agouti[f"{i}"] #dicht_agouti = {ID: pd.dataframe}        for artis [f"{i}_wildlifecamera1"
        epoch_timestamps_agouti = rows_agouti['epoch'].tolist() #list[epoch, epoch] per ID
        deepsqueak_timestamps_id = epoch_timestamps[i]
        for j in deepsqueak_timestamps_id:
            starttime = j
            aprox_endtime = starttime + 10000
            for h in epoch_timestamps_agouti:
                if h >= starttime and h <= aprox_endtime:
                    #print(f"ID: {i}, timestamp: {h}, starttime: {starttime}")
                    starttimes_overlaps.append(starttime)
                    timestamps_id_data.append(h)
        overlaps.update({i: [timestamps_id_data, starttimes_overlaps]})
    #print(overlaps)
    return overlaps #{id: [timestamps with potential overlaps (so agouti timestamps)]}
    print(overlaps)

def overlaps(j):
    pass