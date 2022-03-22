from pytube import YouTube


def ut():
    link = input("Please enter the link of the video you would like to download")
    yt = YouTube(link)
    print(yt.streams.filter(file_extension='mp4'))

    # This selects the stream with this ID it is set to 720p with audio
    print("Starting download....")
    stream = yt.streams.get_by_itag(22)
    stream.download()
    print("Download complete!")

    # This selects the stream with this ID it is set to 480p with audio
    # print("Starting download....")
    # stream = yt.streams.get_by_itag(135)
    # stream.download()
    # print("Download complete!")

    # This selects the stream with this ID it is set to 1080p but this API does not download 1080p videos with sound
    # stream = yt.streams.get_by_itag(137)
    # print("Starting download....")
    # stream.download()
    # print("Download complete!")
