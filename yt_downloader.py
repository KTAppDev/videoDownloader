from pytube import YouTube
from pytube import Search
from pytube import Playlist


def youtube_single_download(link):
    print('single download func ran')
    yt = YouTube(link)
    yt.streams.filter(only_audio=True)
    print("Starting download....")
    stream = yt.streams.get_by_itag(140)
    stream.download()
    print("Download complete!")


def searchtube(txt):
    print('search func ran')
    video_list = []
    s = Search(f'{txt} clean')
    for obj in s.results:
        x = str(
            obj)  # in the future see if theyy have an easier way to use these youtube obj in search results. I doubt what i'm doing is the easy way lol
        video_id = x[x.rfind('=') + 1:].strip('>')
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        video_list.append(video_url)
    return video_list


def download_youtube_playlist():
    print('playlist func ran')
    pl = input('Paste playlist here >')
    playlist = Playlist(pl)
    print('*' * 40)
    print(f'Playlist contains {len(playlist)} items')
    print('*' * 40)
    for url in playlist[:3]:
        youtube_single_download(url)


def download_playlist_from_file(pl):
    print('playlist from file func ran')
    # playlist = Playlist(pl)
    print('*' * 40)
    print(f'Playlist from file contains {len(pl)} items')
    print('*' * 40)
    for url in pl:
        print(url)
        youtube_single_download(url)


if __name__ == '__main__':
    pass
