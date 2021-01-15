from mod.mlog import log

class RtException(Exception):
    def __init__(self, message='Generic Error Exception', loggable=True):
        if loggable:
            log.error(message)
        super(RtException, self).__init__(message)