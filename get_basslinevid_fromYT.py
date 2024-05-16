from pytube import YouTube

def download_youtube_video(url, output_path):
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download(output_path)

# Example usage
youtube_url = 'https://www.youtube.com/watch?v=BdkUWKdb1wQ' 
# Replace with the actual YouTube video URL
output_path = 'D:/Content/Videos'
download_youtube_video(youtube_url, output_path)