import requests
from FileSaver import FileSaver

class LottoManager:
    HTTP_OK = 200
    log_level_list = ("DISABLE", "DEBUG")
    __version__ = 0.1

    def __init__(self, log_level="DISABLE"):
        self.set_log_level(log_level)
        self.saver = FileSaver(self.log_level)
        self.lotto_data = self.saver.load_lotto_data()

    def get_lotto(self, drwNo):
        url = "http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=%d"%(drwNo)
        if self.log_level == "DEBUG":
            print("[+] Request %s"%(url))
        response = requests.get(url)
        if self.log_level == "DEBUG":
            print("[+] Response Status Code is %d"%(response.status_code))
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
        drwNo = 1
        while True:
            info = self.get_lotto(drwNo)
            if self.log_level == "DEBUG":
                print("[*] Request %d Lotto Data"%(drwNo))
            if info:
                self.lotto_data[drwNo] = info
            else:
                break
            drwNo += 1

    def set_log_level(self, log_level):
        if log_level not in self.log_level_list:
            print("level must be ", self.log_level_list)
        self.log_level = log_level

    def save_lotto_data(self, filename = None):
        self.saver.save_lotto_data(self.lotto_data, filename)

    def load_lotto_data(self, filename = None):
        self.lotto_data = self.saver.load_lotto_data(filename)
