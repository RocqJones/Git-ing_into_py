playlist = {'playlist': 'Dear Mellanholy',
            'author': 'The Weeknd',
            'songs':[
                #store title, duration... inside a dictionary because each song is a dictionary inside a list
                {'title': 'song1', 'artist':['blue'], 'duration': 2.5},
                {'title': 'song2', 'artist':['Wayne','Dj Khaled'], 'duration': 5.25},
                {'title': 'wait', 'artist':['August Alsina'], 'duration': 2.0}
            ]
}
total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
print(total_length)
