import requests
from FileSaver import FileSaver

class LottoManager:
    HTTP_OK = 200
    log_level_list = ("DISABLE", "DEBUG")
    __version__ = 0.1

    def __init__(self):
        self.set_log_level("DISABLE")
        self.saver = FileSaver(self.log_level)
        self.lotto_list = self.saver.load_lotto_data()

    def get_lotto(self, drwNo):
        url = "http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=%d"%(drwNo)
        if log_level == "DEBUG":
            print("[+] Request %s"%(url))
        response = requests.get(url)
        if log_level == "DEBUG":
            print("[+] Response Status Code is %d"%(response.status_code))
        if response.status_code != self.HTTP_OK:
            return None
        else:
            data = response.json()
            info = {"totalSell": data["totSellamnt"],
                    "winnerCount": data["firstPrzwnerCo"],
                    "bonusNum": data["bnusNo"],
                    "Num": [data["drwtNo%d"]%(x) for x in ragne(1, 7)]}
            return info

    def set_log_level(self, log_level):
        if log_level not in self.log_level_list:
            print("level must be ", self.log_level_list)
        self.log_level = log_level
