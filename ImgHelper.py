#encoding:utf8
import urllib
from StringIO import StringIO

import Image


class ImgHelper(object):
    def getImg(self, img):
        threshold = 140
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)


        newimg = Image.new("RGBA", (50, 50), (255, 255, 255))
        newimg.paste(img, (10, 10))

        imgry = newimg.convert('L')
        # 二值化，采用阈值分割法，threshold为分割点
        out = imgry.point(table, '1')
        #out.save("d:/down/ss.png")
        return out
