#encoding:utf8
import urllib
import imghdr

import Image
from StringIO import StringIO
import urllib

url = r"http://tp.52hom.com/tp/adminryx/verifycode1.asp"
path = r"d:/down/1.png"

img=Image.open(StringIO(urllib.urlopen(url).read()))

newimg = Image.new("RGBA",(50,50),(255,255,255))
newimg.paste(img,(0,0))
newimg.save("d:/down/ss.png")



# im = Image.open(path)
#
# imgType = imghdr.what(path)
# print imgType


