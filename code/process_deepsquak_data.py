import os
import glob
import pandas as pd

def csv_filenames(path_folder):
    extension = 'csv'
    os.chdir(path_folder)
    filenames: list = glob.glob('*.{}'.format(extension))
    return filenames

def id_names(path_folder):
    filenames = csv_filenames(path_folder)
    id_names = []
    for i in filenames:
        id_names.append(i.split('_202')[0])
    id_names = list(set(id_names))
    return id_names #not sorted on number

def data_in_dict(path_folder):
    names_id = id_names(path_folder)
    files: list = csv_filenames(path_folder)
    data = {}
    for name in names_id:
        filenames_with_id = []
        for file in files:
            if name in file:
                filenames_with_id.append(file)
        data.update({name: filenames_with_id})

    return data
    
    for h in data:
       print(f"key: {h}, values: {data[h]} \n\n")

"4 mei: vandaag: - code opgeschoond, agouti data nu in dictionary, deepsquak files begin daaraan (files kunnen worden ingelezen)"
