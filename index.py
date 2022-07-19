import pytube 
import argparse
import os


#dctube link video -q high -p ~/download
#dctube link song -p ~/download


class dctube():

    def __init__(self, link, type, quality = 'high'):
    
        self.link = link
        self.type = type
        self.quality = quality


    def download_path(self):

        home = os.path.expanduser('~')
        self.down_path = os.path.join(home, 'Downloads')


    def download(self):
        
        if self.type == 'song':
            pytube.YouTube(self.link).streams.get_audio_only().download(self.down_path)


        elif self.type == 'video':

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
    aft.add_argument('-q', type = str, help = 'quality video, default: high', default = 'high')
    argu = aft.parse_args()

    dctube_p = dctube(argu.link, argu.type, argu.q)
    dctube_p.download_path()
    dctube_p.download()


