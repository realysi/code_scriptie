from code.process_agouti_data import data_agouti, agoutidata_to_dict
from code.process_deepsquak_data import data_in_dict

path = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/artis_csv'
linked_data = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/linked_results.csv"

#data_agouti("/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/observations.csv", "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/media.csv")


agoutidata_to_dict(linked_data)