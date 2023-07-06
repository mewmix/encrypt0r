import youtube_dl
import sys

def download_videos(urls):
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best audio format available
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convert to MP3
            'preferredquality': '192',  # Set audio quality (adjust as needed)
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Output file template
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            ydl.download([url])

# Get the URLs from command-line arguments
urls = sys.argv[1:]

# Call the download_videos function with the URLs
download_videos(urls)
