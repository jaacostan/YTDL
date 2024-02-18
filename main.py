import yt_dlp
import os

def download_playlist(playlist_url, output_dir):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Choose the best quality available
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',  # Output template for the downloaded files
        'writeinfojson': True,  # Write metadata to a .info.json file
        'writethumbnail': True,  # Write thumbnail image to disk
        'quiet': False  # Show informational messages and warnings
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def get_output_directory():
    output_dir = input("Enter the output directory: ")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

if __name__ == "__main__":
    playlist_url = input("Enter the URL of the playlist you want to download: ")
    output_directory = get_output_directory()
    download_playlist(playlist_url, output_directory)

