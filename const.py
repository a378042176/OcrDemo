import sys

class Const(object):
    class ConstError(Exception): pass
    def __setattr__(self, key, value):
        if self.__dict__.has_key(key):
            raise self.ConstError, "Changing const.%s" % key
        else:
            self.__dict__[key] = value

    def __getattr__(self, key):
        if self.__dict__.has_key(key):
            return self.key
        else:
            return None

sys.modules[__name__] = Const()

import const

const.MAIL_PROTO_IMAP = 'imap'
const.MAIL_PROTO_GMAIL = 'gmail'
const.MAIL_PROTO_HOTMAIL = 'hotmail'
const.MAIL_PROTO_EAS = 'eas'
const.MAIL_PROTO_EWS = 'ews'