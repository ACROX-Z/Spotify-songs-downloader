import os
import sys

def download_song(song_url):
    """
    Downloads a single song from Spotify using spotdl.
    """
    print(f"Downloading song: {song_url}")
    os.system(f"spotdl {song_url}")

def download_playlist(playlist_url):
    """
    Downloads an entire playlist from Spotify.
    """
    print(f"Downloading playlist: {playlist_url}")
    os.system(f"spotdl {playlist_url}")

def download_from_file(file_path):
    """
    Downloads multiple songs or playlists from a text file containing Spotify links.
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found!")
        return

    print(f"Downloading songs from file: {file_path}")
    os.system(f"spotdl --list {file_path}")

def main():
    print("Spotify Song Downloader using SpotDL\n")

    print("Options:")
    print("1. Download a Single Song")
    print("2. Download a Playlist")
    print("3. Bulk Download from File (songs.txt)")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        song_url = input("Enter Spotify song URL: ")
        download_song(song_url)

    elif choice == "2":
        playlist_url = input("Enter Spotify playlist URL: ")
        download_playlist(playlist_url)

    elif choice == "3":
        file_path = input("Enter file path (e.g., songs.txt): ")
        download_from_file(file_path)

    elif choice == "4":
        print("Exiting program.")
        sys.exit()

    else:
        print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

