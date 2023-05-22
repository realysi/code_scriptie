from agouti.filter import data_aougti_test
from deepsqueak.info_data import deepsquakfiledata_to_dict
from code.possible_overlaps import overlapping_id, epoch_timestamps_deepsqueak, timestamps_overlaps
from code.overlaps import oefenshit, stap2

path = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/artis_csv'
linked_data = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/linked_results.csv"
artis_folder_deepsquak = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/artis_csv'
#data_agouti("/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/observations.csv", "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/media.csv")

flevopark_media = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Flevopark/media.csv'
flevopark_observations = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Flevopark/observations.csv'
flevopark_deployments = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Flevopark/deployments.csv'
"""agoutidata_to_dict(linked_data)
id_names(artis_folder)"""


#path = data_agouti(path_observations=flevopark_observations, path_media=flevopark_media, path_deployments=flevopark_deployments, location_dataset='flevopark')
path = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/flevopark+mediadata.csv'
agouti_data = data_aougti_test(path)

deepsqueak_data = deepsquakfiledata_to_dict('/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/flevopark_csv')

#epoch_timestamps_deepsqueak(agouti_data, deepsqueak_data)

#oefenshit(agouti_data, deepsqueak_data)
stap2(agouti_data, deepsqueak_data)
#ids = overlapping_id(agouti_data, deepsqueak_data)
#epoch_timestamps_deepsqueak(agouti_data, deepsqueak_data)
#timestamps_overlaps(agouti_data, deepsqueak_data)

#overlap_time(agouti_data, deepsqueak_data)
#data_in_dict(artis_folder)
#agoutidata = agoutidata_to_dict(linked_data) #{ID: pd.Dataframe}
#deepsquakfiledata = deepsquakfiledata_to_dict(artis_folder_deepsquak) #{ID: [filename, filename]}

#print(overlapping_id(agoutidata, deepsquakfiledata))
#overlap_time(agoutidata, deepsquakfiledata)

#process_observation_data('/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/observations.csv')
#link_observation_media('/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/filtered_observation.csv', '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/media.csv')
#deployments('/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/deployments.csv', '/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/filtered_observation.csv')
#link_observation_media('/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/deployments_linked.csv', '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/media.csv')