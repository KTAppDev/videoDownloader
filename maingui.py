import os
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import yt_downloader
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import ssl
from kivy.config import Config  # used to set window size

ssl._create_default_https_context = ssl._create_unverified_context  # important used to make internet coms legit

############Screen size################
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '500')


#######################################

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class BoxLayoutUI(BoxLayout):
    link = ObjectProperty(None)
    op_input = ObjectProperty(None)
    update_label = ObjectProperty(None)
    download_button = ObjectProperty(None)

    main_canv_image = resource_path('bg.png')
    yt_logo = resource_path('ytlogo.png')

    def download_button_action(self):
        desktop = os.path.expanduser("~/Desktop/")
        if self.link.text == '':
            self.update_label.text = 'ERROR - Please enter a song name and artiste'
            return
        if self.op_input.text == '':
            self.op_input.text = 'Youtube'
        self.path_to_last_song = desktop + self.op_input.text # Made this so i ca reuse it below
        self.update_label.text = f'Downloaded {yt_downloader.youtube_single_download(yt_downloader.searchtube(self.link.text), self.path_to_last_song)}'
        self.rename_file(self.path_to_last_song + '/' + self.update_label.text[11:] + '.mp4')
        self.link.text = ''
        self.op_input.text = ''

    def rename_file(self, song_path):
        print(song_path)
        base, ext = song_path.split('.')
        new_file = base + '.mp3'
        os.rename(song_path, new_file)


class YoutubeDownloader(App):
    def build(self):
        self.title = 'Youtube Clean Audio Downloader - KTAD'
        kv = Builder.load_file(resource_path('yt.kv'))
        return kv


if __name__ == "__main__":
    YoutubeDownloader().run()
