from code.reading_data_voorbeelden import read_data
from code.intervals import time_to_seconds
"https://www.geeksforgeeks.org/how-to-convert-datetime-to-integer-in-python/"

link_audio_voorbeelden = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Voorbeeld_data_audio.csv"
link_video_voorbeelden = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Voorbeeld_data_video.csv"

"""df = read_data(link_audio_voorbeelden)
print(df)
for i in df.index:
    print(df.loc[i, "Tijd begin detectie"],'\n')"""

df = time_to_seconds(link_audio_voorbeelden)
print(df)