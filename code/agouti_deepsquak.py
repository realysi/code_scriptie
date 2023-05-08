from code.process_agouti_data import agoutidata_to_dict
from code.process_deepsquak_data import deepsquakfiledata_to_dict
import datetime

path = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/artis_csv'
linked_data = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/linked_results.csv"
artis_folder_deepsquak = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/artis_csv'

agoutidata = agoutidata_to_dict(linked_data) #{ID: pd.Dataframe}
deepsquakfiledata = deepsquakfiledata_to_dict(artis_folder_deepsquak) #{ID: [filename, filename]}

#Step 1: check if they have same ID, if so put that id in a list
def overlapping_id(dict_agouti: dict, dict_deepsquak: dict):
    dict_agouti_keys = list(dict_agouti.keys())
    for i in range(0, len(dict_agouti_keys)):
        dict_agouti_keys[i] = "_".join(dict_agouti_keys[i].split("_", 2)[:2])
    dict_deepsquak_keys = list(dict_deepsquak.keys())
    for i in range(0, len(dict_deepsquak_keys)):
        dict_deepsquak_keys[i] = "_".join(dict_deepsquak_keys[i].split("_", 2)[:2])
        
    overlapping_ids = []
    for i in dict_agouti_keys:
        if i in dict_deepsquak_keys:
            overlapping_ids.append(i)
    return overlapping_ids #['artis_26', 'artis_22', 'artis_24', 'artis_18', 'artis_20', 'artis_21', 'artis_19', 'artis_27']

#step 2: check if times overlap (HEELLLL veel gedoe), als het binnen 10.000 seconden van elkaar zit(deepsquak) --> overlappend!
def overlap_time(dict_agouti, dict_deepsquak):
    ids = overlapping_id(dict_agouti, dict_deepsquak) #['artis_26', 'artis_22', 'artis_24', 'artis_18', 'artis_20', 'artis_21', 'artis_19', 'artis_27']
    
    for i in ids:
        #deepsquak timestamps per id
        filenames_deepsquak: list[str] = dict_deepsquak[f"{i}_audio1"] #['artis_26_audio1_2021-10-09_16-00-00_(19) 2022-12-14  5_39 PM.csv', etc]
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
        
            
        #agouti timestamps per id
        rows_agouti = dict_agouti[f"{i}_wildlifecamera1"]
        epoch_timestamps_agouti = rows_agouti['epoch'].tolist() #all unique id names

        for j in epoch_timestamps_deepsquak:
            starttime = j
            aprox_endtime = starttime + 10000
            #print(f'starttime: {starttime}, endtime: {aprox_endtime}')
            for h in epoch_timestamps_agouti:
                #print(h - j)
                if h >= starttime and h <= aprox_endtime:
                    print(h)
        #2 minuten tijdinterval nog in verwerken
    #agouti timestamps


