import pytube 
dl = input('What do you want aduio or video (A/V)? ')
if dl == "V":
    url = input("Enter the link video:  ")
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download('../Videos')
elif dl == "A":
    url = input("Enter the link video: ")
    youtube = pytube.YouTube(url)
    audio = youtube.streams.filter(only_audio=True).all()
    audio[0].download('../Music')

print("Thanks for using Crespo Download")