import pytube 
from pytube import Playlist
import argparse
import os


class dctube():

    def __init__(self, link, type, listvideo = False, quality = 'high'):
    
        self.link = link
        self.type = type
        self.quality = quality
        self.listvideo = listvideo


    def download_path(self):

        home = os.path.expanduser('~')
        self.down_path = os.path.join(home, 'Downloads')


    def download(self):
        
        if self.type == 'song':

            if self.listvideo:
                l_video = Playlist(self.link)

                for video in l_video.videos:
                    video.streams.get_audio_only().download(self.down_path)

            else:
                pytube.YouTube(self.link).streams.get_audio_only().download(self.down_path)


        elif self.type == 'video':
            
            if self.listvideo:
                l_video = Playlist(self.link)

                if self.quality == 'high' or self.quality == 'default':

                    for video in l_video.videos:
                        video.streams.get_highest_resolution().download(self.down_path)

                elif self.quality == 'low':

                    for video in l_video.videos:
                        video.streams.get_lowest_resolution().download(self.down_path)

                else:
                    print('[-] Quality error')

            else:
                if self.quality == 'high' or self.quality == 'default':
                    pytube.YouTube(self.link).streams.get_highest_resolution().download(self.down_path)

                elif self.quality == 'low':
                    pytube.YouTube(self.link).streams.get_lowest_resolution().download(self.down_path)

                else:
                    print('[-] Quality error')

        else:
            print('[-] Type error')



if __name__ == '__main__':

    aft = argparse.ArgumentParser()
    aft.add_argument('link', type = str, help = 'youtube link')
    aft.add_argument('type', type = str, help = 'song or video')
    aft.add_argument('-lv', type = bool, help = 'is playlist?, default: no', default = False)
    aft.add_argument('-q', type = str, help = 'quality video, default: high', default = 'high')
    argu = aft.parse_args()

    dctube_p = dctube(argu.link, argu.type, argu.lv, argu.q)
    dctube_p.download_path()
    dctube_p.download()


