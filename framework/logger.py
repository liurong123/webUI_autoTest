import logging
import  os
import time
class Logger(object):
    def __init__(self,logger):
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath('.'))+'/logs/'
        log_name=log_path+rq+'.log'
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)
        formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

    def getlog(self):
        return self.logger