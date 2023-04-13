import datetime
from reading_data_voorbeelden import read_audio_data, read_video_data

def one_minute(link_audio_data):
    audio_df = read_audio_data(link_audio_data)
    audio_df["Tijd begin detectie"] #

b = a[["ID", "Tijd begin detectie"]]
print(b)
print("\n\n")
#print(b.loc[1])

tijd = b.loc[0, "Tijd begin detectie"]
print(tijd)
print(tijd)
print(type(tijd))
#b.loc[0, "Tijd begin detectie"] = tijd + 5