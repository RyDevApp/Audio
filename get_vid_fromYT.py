import os
from pytube import YouTube

def download_youtube_audio(url, output_path):
    """
    Downloads the audio from a YouTube video given its URL and saves it to the specified output path.

    Args:
        url (str): The URL of the YouTube video.
        output_path (str): The path where the downloaded audio file will be saved.

    Returns:
        None
    """
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(output_path=output_path)
    original_file = os.path.join(output_path, audio.default_filename)
    output_file = os.path.join(output_path, 'audio.wav')
    os.rename(original_file, output_file)

# Example usage
youtube_url = 'https://www.youtube.com/watch?v=k1iXOR_xlwE' 
# Replace with the actual YouTube video URL
output_path = "D:/Music/Sounds"  # Replace with the desired output path
download_youtube_audio(youtube_url, output_path)
