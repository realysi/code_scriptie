from code.process_agouti_data import data_agouti, agoutidata_to_dict, process_observation_data, link_observation_media, deployments
from code.process_deepsquak_data import deepsquakfiledata_to_dict
from code.agouti_deepsquak import overlapping_id, overlap_time

path = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/artis_csv'
linked_data = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/linked_results.csv"
artis_folder_deepsquak = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/artis_csv'
#data_agouti("/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/observations.csv", "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/media.csv")


"""agoutidata_to_dict(linked_data)
id_names(artis_folder)"""
#data_in_dict(artis_folder)
"""agoutidata = agoutidata_to_dict(linked_data) #{ID: pd.Dataframe}
deepsquakfiledata = deepsquakfiledata_to_dict(artis_folder_deepsquak) #{ID: [filename, filename]}

#overlapping_id(agoutidata, deepsquakfiledata)
overlap_time(agoutidata, deepsquakfiledata)"""

#process_observation_data('/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/observations.csv')
#link_observation_media('/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/filtered_observation.csv', '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/media.csv')
deployments('/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/deployments.csv', '/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/filtered_observation.csv')
