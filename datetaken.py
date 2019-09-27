import os, glob
from PIL import Image
from datetime import datetime

for file in glob.glob('*.JPG'):
    path = datetime.strptime(Image.open(file)._getexif()[36867], '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d_%H-%M-%S')
    if not os.path.exists(path[:-9]):
        os.mkdir( path[:-9], 0o755 )
    os.rename(file, path[:-9]+"/"+file)
    print ("Done")
