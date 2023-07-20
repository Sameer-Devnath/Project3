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

