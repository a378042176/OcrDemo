#encoding:utf8
from pytesser import image_to_string


class STHelper(object):
    def getCode(self, img):
        return image_to_string(img)