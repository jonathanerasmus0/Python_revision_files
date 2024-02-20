# Define global variables (always follow this guide)
songs = []
playlists = {}

# Function to display menus of teh songs
def display_menu():
    print("Welcome to the Digital Music Library Management System")
    print("1. Add a song")
    print("2. Create a playlist")
    print("3. Add songs to a playlist")
    print("4. Display all songs")
    print("5. Display all playlists")
    print("6. Search for a song")
    print("7. Play a playlist")
    print("8. Exit")

# Function to add a songs 
def add_song():
    title = input("Enter the title of the song: ")
    artist = input("Enter the artist of the song: ")
    genre = input("Enter the genre of the song: ")
    duration = input("Enter the duration of the song (in minutes): ")
    songs.append({'title': title, 'artist': artist, 'genre': genre, 'duration': duration})
    print("Song added successfully!")

# Function to create a playlist of the songs 
def create_playlist():
    name = input("Enter the name of the playlist: ")
    playlists[name] = []
    print("Playlist created successfully!")

# Function to add songs to a playlist or playlists 
def add_songs_to_playlist():
    playlist_name = input("Enter the name of the playlist: ")
    if playlist_name in playlists:
        while True:
            display_songs()
            song_index = int(input("Enter the index of the song to add (-1 to stop adding): "))
            if song_index == -1:
                break
            elif 0 <= song_index < len(songs):
                playlists[playlist_name].append(songs[song_index])
                print(f"Song '{songs[song_index]['title']}' added to playlist '{playlist_name}'")
            else:
                print("Invalid song index. Please try again.")
    else:
        print("Playlist not found.")

# Function to display all songs REVISE ENUMERATE MORE 
def display_songs():
    if songs:
        print("All Songs:")
        for index, song in enumerate(songs):
            print(f"{index}. Title: {song['title']}, Artist: {song['artist']}, Genre: {song['genre']}, Duration: {song['duration']} minutes")
    else:
        print("No songs available in the library.")

# Function to display all playlists
def display_playlists():
    if playlists:
        print("All Playlists:")
        for playlist in playlists:
            print(playlist)
    else:
        print("No playlists available.")

# Function to search for a song
def search_song():
    keyword = input("Enter a keyword to search for a song: ")
    found = False
    for song in songs:
        if keyword.lower() in song['title'].lower() or keyword.lower() in song['artist'].lower():
            print(f"Title: {song['title']}, Artist: {song['artist']}, Genre: {song['genre']}, Duration: {song['duration']} minutes")
            found = True
    if not found:
        print("No matching songs found.")

# Function to play a playlist
def play_playlist():
    playlist_name = input("Enter the name of the playlist to play: ")
    if playlist_name in playlists:
        print(f"Playing playlist '{playlist_name}':")
        for song in playlists[playlist_name]:
            print(f"Now playing - {song['title']} by {song['artist']}")
    else:
        print("Playlist not found.")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_song()
        elif choice == '2':
            create_playlist()
        elif choice == '3':
            add_songs_to_playlist()
        elif choice == '4':
            display_songs()
        elif choice == '5':
            display_playlists()
        elif choice == '6':
            search_song()
        elif choice == '7':
            play_playlist()
        elif choice == '8':
            print("Thank you for using the Digital Music Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function AS ALWAYS.
if __name__ == "__main__":
    main()
