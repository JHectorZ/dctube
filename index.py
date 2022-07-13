import pytube 
import argparse
import os


#dctube link video -q high -p ~/download
#dctube link song -p ~/download


class dctube():

    def __init__(self, link, type, quality = 'high', pathd = '.download/'):
    
        self.link = link
        self.type = type
        self.quality = quality
        self.pathd = pathd


    def overwriter(self):

        for i in os.listdir(self.pathd):

            if i == str(pytube.YouTube(self.link).title):
                self.asw_overwirte = input('\nYou want to overwrite the file named? (y/n):').lower()
            
            if self.asw_overwirte == 'n':
                print('[-] There was no change!')
                return 
    

    def download(self):
        
        if self.type == 'song':
            pytube.YouTube(self.link).streams.get_audio_only().download(self.pathd)


        elif self.type == 'video':

            if self.quality == 'high' or self.quality == 'default':
                pytube.YouTube(self.link).streams.get_highest_resolution().download(self.pathd)

            elif self.quality == 'medium':
                pytube.YouTube(self.link).streams.get_by_resolution('360p').download(self.pathd)
            
            elif self.quality == 'low':
                pytube.YouTube(self.link).streams.get_lowest_resolution().download(self.pathd)

            else:
                print('[-] Quality error')

        else:
            print('[-] Type error')



if __name__ == '__main__':

    if os.path.exists('download') == False:
        os.makedirs('download')

    aft = argparse.ArgumentParser()
    aft.add_argument('link', type = str, help = 'youtube link')
    aft.add_argument('type', type = str, help = 'song or video')
    aft.add_argument('-q', type = str, help = 'quality video, default: high', default = 'high')
    aft.add_argument('-p', type = str, help = 'save path, default: /download', default = 'download/')
    argu = aft.parse_args()

    dctube_p = dctube(argu.link, argu.type, argu.q, argu.p)
    dctube_p.overwriter()
    dctube_p.download()


