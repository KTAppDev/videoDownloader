import os
import sys

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
import yt_downloader
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    link = ObjectProperty(None)
    op_input = ObjectProperty(None)
    update_label = ObjectProperty(None)
    download_button = ObjectProperty(None)

    def download_button_action(self):
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
        self.window = GridLayout()
        # self.window.cols = 1
        # self.window.size_hint = (0.6, 0.7)
        # self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        # logo = self.resource_path('ytlogo.png')
        # self.window.add_widget(Image(source=logo))

        self.update_label = Label(
            text='Updates will appear here',
            font_size=18,
            color='red',
        )
        self.window.add_widget((self.update_label))

        self.op_input = TextInput(multiline=False,
                                  padding_y=(20, 20),
                                  size_hint=(1, 0.5),
                                  halign="center",
                                  hint_text="Specify Folder Name",
                                  hint_text_color='red'
                                  )
        self.window.add_widget(self.op_input)

        self.link = TextInput(multiline=False,
                              padding_y=(20, 20),
                              size_hint=(1, 0.5)
                              )
        self.window.add_widget(self.link)

        self.download_button = Button(text='Download',
                                      size_hint=(1, 0.5),
                                      bold=True,
                                      background_color='red',
                                      )
        self.download_button.bind(on_press=self.download_button_action)
        self.window.add_widget(self.download_button)
        return MyGrid()

    def download_button_action(self, instance):
        self.update_label.text = f'downloading {self.link.text}'
        yt_downloader.youtube_single_download(yt_downloader.searchtube(self.link.text), self.op_input.text)

    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


if __name__ == "__main__":
    YoutubeDownloader().run()
