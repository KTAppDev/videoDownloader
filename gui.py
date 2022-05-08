import os
import sys
from kivy.app import App
from kivy.uix.widget import Widget
import yt_downloader
from kivy.properties import ObjectProperty
from kivy.lang import Builder


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class MyGrid(Widget):
    link = ObjectProperty(None)
    op_input = ObjectProperty(None)
    update_label = ObjectProperty(None)
    download_button = ObjectProperty(None)

    main_canv_image = resource_path('bg.png')
    yt_logo = resource_path('ytlogo.png')

    def download_button_action(self):
        self.update_label.text = ''
        self.update_label.text = 'Searching...'
        if self.link.text == '':
            self.update_label.text = 'Error - Please enter a song name and artiste'
            return
        if self.op_input.text == '':
            self.op_input.text = 'Downloads'
        self.update_label.text = f'Downloaded {yt_downloader.youtube_single_download(yt_downloader.searchtube(self.link.text), self.op_input.text)}'
        self.link.text = ''
        self.op_input.text = ''


class YoutubeDownloader(App):
    def build(self):
        kv = Builder.load_file(resource_path('yt.kv'))
        return kv


if __name__ == "__main__":
    YoutubeDownloader().run()
