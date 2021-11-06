from typing import List
import random
import sys
# My name: Jaden Nobles
# My partner's name: Jason Nobles

# User Information
USERNAME = "MusicFan'03"
PASSWORD = "hunter1"
users_playlists = [2019386, 5343409, 9082438]
subscriber_count = 10

RESPONCES = ['yes', 'no']
ACTIONS = [1, 2, 4]

# Site Policies
MAX_PASSWORD_ATTEMPTS_ALLOWED = 3
MAX_VIDEOS_OUTPUTTED_AT_ONCE = 5

# Playlists (in the form of lists of video IDs)
top_hits_playlist = [5390161, 7736243, 8267507, 4922599, 4559658, 9897626, 1461025, 7434914, 6093037, 6438692, 8117542, 
5746821, 9566779, 5718817, 2459304, 5610524, 6980497, 4547223, 9086699]
top_2010s_playlist = [3720918, 6382983, 1012930, 1109274, 2981023, 7394792]
my_mix = [6382983, 2981023, 9086699]

# Dictionaries
playlist_id_to_video_list = {2019386 : top_hits_playlist, 5343409: top_2010s_playlist, 9082438: my_mix}
playlist_id_to_title = {2019386 : "Top Hits", 5343409: "Top 2010s", 9082438: "My Mix"}
playlist_title_to_id = {"Top Hits": 2019386, "Top 2010s": 5343409, "My Mix": 9082438}

# Videos (key = Video ID, value = Video Title)
video_id_to_title = {
5390161 : "Who Want Smoke",
7736243 : "INDUSTRY BABY",
8267507 : "STAY",
1012930 : "Style",
1109274 : "bad guy",
2981023 : "Blank Space",
4922599 : "Love Nwantiti Remix",
4559658 : "Essence (Official Video)",
9897626 : "Pepas",
5610524 : "Outside (Better Days)",
6980497 : "Lo Siento BB:/",
4547223 : "Face Off",
9086699 : "Heat Waves",
3720918 : "Despacito",
9086691 : "Royals",
1461025 : "Fancy Like",
7434914 : "Way 2 Sexy",
6093037 : "Corta Venas",
6438692 : "Need to Know",
8117542 : "MONEY",
5746821 : "Wild Side ",
9566779 : "Knife Talk",
1683724 : "Life Support",
5718817 : "Save Your Tears",
2459304 : "Ghost",
6382983 : "Love Yourself",
7394792 : "7 rings",
}

def get_shuffled_playlist(video_list: List[int]) -> List[int]:
    shuffled_playlist = []
    
    if video_id == top_hits_playlist:
         shuffled_playlist = users_playlists[0]
    elif video_id == top_2010s_playlist:
         shuffled_playlist = users_playlists[1]
    elif video_id == my_mix:
        shuffled_playlist = users_playlists[2]

    random.shuffle(video_id)
    print('*' * len(playlist_to_action))
    print(playlist_to_action)
    print('*' * len(playlist_to_action))

    
    return display_full_playlist(shuffled_playlist)


def get_shortend_playlist(video_list: List[int]) -> List[int]:
    shortened_list = []

    if video_id == top_hits_playlist:
        shortened_list = users_playlists[0]
    elif video_id == top_2010s_playlist:
        shortened_list = users_playlists[1]
    elif video_id == my_mix:
        shortened_list = users_playlists[2]
    video_id.pop(0)
    if len(video_id) >= 1:
        print('*' * len(playlist_to_action))
        print(playlist_to_action)
        print('*' * len(playlist_to_action))
    elif len(video_id) < 1:
        print('Error.')
        sys.exit()
    return display_full_playlist(shortened_list)


def display_full_playlist(playlist_id: int):
    play_list = []
    
    if playlist_id == users_playlists[0]:
        playlist_id = top_hits_playlist
    elif playlist_id == users_playlists[1]:
        playlist_id = top_2010s_playlist
    elif playlist_id == users_playlists[2]:
        playlist_id = my_mix
        
    for video_id in playlist_id:
        if video_id in video_id_to_title:
            play_list.append(video_id_to_title[video_id])

    for song in play_list[:5]:
        print(song)
    for song in play_list[:5]:
        play_list.remove(song)

    see_playlist = ''
    global action_choise
    global playlist_to_action
    
    if len(play_list) < 1:
        action_choise = int(input('Actions: 1 for shuffle, 2 for shorten, 4 for exit. '))
        if action_choise not in ACTIONS:
            print('Error.')
            sys.exit()
        elif action_choise == 4:
            sys.exit()
        playlist_to_action = input('Which playlist do you want to see? ')
        if playlist_to_action not in playlist_title_to_id:
            print('Error.')
            sys.exit()

    else:
        see_playlist = input('...Do you want to see more? ')
        if see_playlist not in RESPONCES:
            print('Error.')
            sys.exit()
            
    while see_playlist == 'yes':
        for song in play_list[:5]:
            print(song)
        for song in play_list[:5]:
            play_list.remove(song)
            
        if len(play_list) < 1:
            action_choise = int(input('Actions: 1 for shuffle, 2 for shorten, 4 for exit. '))
            if action_choise not in ACTIONS:
                print('Error.')
                sys.exit()
            elif action_choise == 4:
                sys.exit()
            playlist_to_action = input('Which playlist do you want to see? ')
            if playlist_to_action not in playlist_title_to_id:
                print('Error.')
                sys.exit()

            if playlist_to_action == 'Top Hits':
                playlist_id = users_playlists[0]
            elif playlist_to_action == 'Top 2010s':
                playlist_id = users_playlists[1]
            elif playlist_to_action == 'My Mix':
                playlist_id = users_playlists[2]
        
            do_playlist_action(playlist_id, action_choise)
        else:
            see_playlist = input('...Do you want to see more? ')
            if see_playlist not in RESPONCES:
                print('Error.')
                sys.exit()
            
    if see_playlist == 'no':
        action_choise = int(input('Actions: 1 for shuffle, 2 for shorten, 4 for exit. '))
        if action_choise not in ACTIONS:
            print('Error.')
            sys.exit()
        elif action_choise == 4:
            sys.exit()
        playlist_to_action = input('Which playlist do you want to see? ')
        if playlist_to_action not in playlist_title_to_id:
            print('Error.')
            sys.exit()
   

    if playlist_to_action == 'Top Hits':
        playlist_id = users_playlists[0]
    elif playlist_to_action == 'Top 2010s':
        playlist_id = users_playlists[1]
    elif playlist_to_action == 'My Mix':
        playlist_id = users_playlists[2]
        
    do_playlist_action(playlist_id, action_choise)


def display_playlist_preview(playlist_id: int) -> None:
    if playlist_id == users_playlists[0]:
        print("Top Hits")
        top_hits_video_count = len(top_hits_playlist)
        print(top_hits_video_count, "videos")
        print()
    elif playlist_id == users_playlists[1]:
        print("Top 2010s")
        top_2010s_video_count = len(top_2010s_playlist)
        print(top_2010s_video_count,"videos")
        print()
    elif playlist_id == users_playlists[2]:
        print("My Mix")
        my_mix_video_count = len(my_mix)
        print(my_mix_video_count, "videos")
        print()


     
 
def display_personal_homepage() -> None:
    display_playlist_preview(users_playlists[0])
    display_playlist_preview(users_playlists[1])
    display_playlist_preview(users_playlists[2])


def do_playlist_action(playlist_id: int, choice: int) -> None:
    global video_id
    if playlist_id == users_playlists[0]:
        video_id = top_hits_playlist
    elif playlist_id == users_playlists[1]:
        video_id = top_2010s_playlist
    elif playlist_id == users_playlists[2]:
        video_id = my_mix
        
    if action_choise == 1:
        get_shuffled_playlist(video_id)
    if action_choise == 2:
        get_shortend_playlist(video_id)


def main_playlist_interface() -> None:
    choose_playlist = input('Which playlist do you want to see? ')
    if choose_playlist not in playlist_title_to_id:
        print('Error.')
        sys.exit()
    print('*' * len(choose_playlist))
    print(choose_playlist)
    print('*' * len(choose_playlist))
    if choose_playlist == 'Top Hits':
        playlist_id = users_playlists[0]
    elif choose_playlist == 'Top 2010s':
        playlist_id = users_playlists[1]
    elif choose_playlist == 'My Mix':
        playlist_id = users_playlists[2]

    display_full_playlist(playlist_id)


def user_login() -> bool:
    attempts = 0
    global successful_login
    while attempts <= 3:
        enter_username = input('Username: ')
        enter_password = input('Password: ')
        if enter_username != USERNAME or enter_password != PASSWORD:
            attempts += 1
            if attempts == 3:
                print('Access Denied.')
                sys.exit()
            else:
                print('Try again.')
        else:
            successful_login = True
            print('*' * len(USERNAME))
            print(USERNAME)
            print(subscriber_count, 'subscribers')
            print()
            return successful_login

print("> YouTube")
successful_login = False

user_login()

if successful_login:
    display_personal_homepage()
    main_playlist_interface()