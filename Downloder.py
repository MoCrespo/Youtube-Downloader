from pytube import YouTube

def download():
    url = input('Enter the video link: ')
    ask = input('What do you want Video or Audio (A/V) : ')
    if ask == 'V':
        def video():
            video = YouTube(url)
            res = input('Choose the quality (720  -  480  -  360):')
            res2 = f'{res}p'
            yt = video.streams.filter(res=res2).all()
            path = input('Enter path to download : ')
            yt[0].download(path)
        video()
    elif ask == 'A':
        def audio():
            audio = YouTube(url)
            mp3 = audio.streams.filter(only_audio=True).all()
            path = input('Enter path to download : ')
            mp3[0].download(path)
        audio()
    def again():
        again = input('Do you want to return (yes/no)')
        if again == 'yes':
            download()
        elif again == 'no':
            print('Thanks \n bye')
    again()

download()



