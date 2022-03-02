import os
import datetime
import pandas as pd
import time
import csv
import youtube_dl
from youtube_search import YoutubeSearch

df = pd.read_csv('/home/ryo/Documents/kuvo/csv/import.csv')

# Init csv
csv_dir = '/home/ryo/Documents/kuvo/csv/record'+ str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute) +'.csv' 
file = open(csv_dir, 'w')
w = csv.writer(file)

dl_dir = '/home/ryo/Documents/kuvo/song/'


for i in range(30): 
#   get song name and artist name

    song_name = str(df.iat[i,1])
    artist = str(df.iat[i,2])
    # artist = 'NaN'

    if artist == 'nan':
        print('This is nan')
        artist = str(" ")
    else:
        print('This is not nan')
    
    print('Song:', song_name)
    print("Artist:", artist)

    search_word = str(song_name) + " " + str(artist)
    print(' ')

    result = YoutubeSearch(search_word, max_results=50).to_dict()

    false_num = 0

    while len(result) == 0:
        print("false, search again")
        result = YoutubeSearch(search_word, max_results=50).to_dict()
        false_num += 1

        #original song which can't find on YouTube search
        if false_num == 5:
            url = ' '
            break

    else:
        print("get id successful")

        id = result[0]["id"]

        url = 'https://www.youtube.com/watch?v=' + id
        print(' ')
    
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl':  dl_dir + str(song_name) + '.%(ext)s',
            'ignoreerrors': 'True',
            'noplaylist': 'True',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                     'preferredcodec': 'm4a',
                    'preferredquality': '192'
                },
                {
                     'key': 'FFmpegMetadata'
                },
            ],
        }
    
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        info_dict = ydl.extract_info(url, download=True)

    #   Init list
    add_row = []
    add_row.append(str(i))
    add_row.append(song_name)
    add_row.append(artist)
    add_row.append(url)
    
    print(' ')
    print('result')
    print(add_row)
    print(' ')

    w.writerow(add_row)
    time.sleep(5)

file.close()

