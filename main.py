from pytube import YouTube

link = "https://www.youtube.com/watch?v=bhxhNIQBKJI"
youtube_1 = YouTube(link)
# print(youtube_1.title)
# print(youtube_1.thumbnail_url)

# videos = youtube_1.streams.all()
# videos = youtube_1.streams.filter(only_audio=True)
videos = youtube_1.streams.filter(only_audio=False)
vid = list(enumerate(videos))

for i in vid:
    print(i)
print()

stream = int(input("enter: "))
print("Downloading...")
videos[stream].download()
print("Successfully")

from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)