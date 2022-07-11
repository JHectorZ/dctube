import pytube 
import argparse


#dctube link video -q high -p ~/download
#dctube link song -p ~/download


class dctube():

    def __init__(self, link, type, quality = 'high', pathd = '.download/'):
    
        self.link = link
        self.type = type
        self.quality = quality
        self.pathd = pathd


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
    
    aft = argparse.ArgumentParser()
    aft.add_argument('link', type = str, help = 'youtube link')
    aft.add_argument('type', type = str, help = 'song or video')
    aft.add_argument('-q', type = str, help = 'quality video, default: high', default = 'high')
    aft.add_argument('-p', type = str, help = 'save path, default: /download', default = 'download/')
    argu = aft.parse_args()


    dctube(argu.link, argu.type, argu.q, argu.p).download()


