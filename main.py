import read_from_file
import yt_downloader

# calling the Youtube file
# yt_downloader.youtube_single_download(yt_downloader.searchtube('hgsyrk'))
# ut.download_playlist()
yt_downloader.download_playlist_from_file(read_from_file.read_urls_from_file())


