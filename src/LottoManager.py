import requests
import logging
import logging.handlers
from FileSaver import FileSaver

class LottoManager:
    HTTP_OK = 200
    __version__ = 0.2

    def __init__(self, log_level=logging.INFO):
        # setup logger
        self.logger = logging.getLogger("mylogger")
        self.logger.setLevel(log_level)
        fomatter = logging.Formatter('[%(levelname)-5s]%(filename)-15s:%(lineno)s | %(message)s')
        fileHandler = logging.FileHandler('./myLoggerTest.log')
        streamHandler = logging.StreamHandler()
        fileHandler.setFormatter(fomatter)
        streamHandler.setFormatter(fomatter)
        self.logger.addHandler(fileHandler)
        self.logger.addHandler(streamHandler)

        self.saver = FileSaver(self.logger)
        self.lotto_data = self.saver.load_lotto_data()

    def get_lotto(self, drwNo):
        ''' get lotto info from REST API '''

        url = "http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=%d"%(drwNo)
        self.logger.debug("[+] Request %s"%(url))
        response = requests.get(url)
        self.logger.debug("[+] Response Status Code is %d"%(response.status_code))
        if response.status_code != self.HTTP_OK:
            return None
        else:
            data = response.json()
            if data["returnValue"] == "fail":
                return None
            info = {"totalSell": data["totSellamnt"],
                    "winnerCount": data["firstPrzwnerCo"],
                    "bonusNum": data["bnusNo"],
                    "Num": [data["drwtNo%d"%(x)] for x in range(1, 7)]}
            return info

    def get_all_lotto(self):
        ''' get all lotto info using get_lotto '''

        drwNo = 1
        while True:
            if drwNo not in self.lotto_data:
                info = self.get_lotto(drwNo)
                self.logger.debug("[*] Request %d Lotto Data"%(drwNo))
                if info:
                    self.lotto_data[drwNo] = info
                else:
                    break
            drwNo += 1
        self.logger.info("[+] get %d data"%(drwNo))

    def save_lotto_data(self, filename = None):
        self.saver.save_lotto_data(self.lotto_data, filename)

    def load_lotto_data(self, filename = None):
        self.lotto_data = self.saver.load_lotto_data(filename)
