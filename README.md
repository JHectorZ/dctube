# dctube
This is a package that is in progress to be able to download videos and music from the linux terminal

The pytube module is required at the moment :(
you can get it with https://aur.archlinux.org/python-pytube.git

This will be the structure to run:

python index.py <link> <type> -lv <Playlist: True o False (optional)> -q <quality (optional)> 

example:
  python index.py https://www.youtube.com/watch?v=B9RgougnhiE video 
  
  python index.py https://www.youtube.com/watch?v=B9RgougnhiE song
  
  python index.py https://www.youtube.com/watch?v=B9RgougnhiE song -lv True (if playlist) 

  python index.py https://www.youtube.com/watch?v=B9RgougnhiE song -lv False (if not playlist) 

  python index.py https://www.youtube.com/watch?v=B9RgougnhiE video -q low


  
This is provisional in what will be done in package for linux in future commits!!
  
