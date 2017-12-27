import requests
import pickle
import os

class FileSaver:
    def __init__(self, log_level, filename="lotto.data"):
        self.filename = filename
        self.log_level = log_level

    def save_lotto_data(self, filename=None):
        if not filename:
            filename = self.filenaem
        f = open(filename, "wb")
        pickle.dump(lotto_list, f)
        f.close()

    def load_lotto_data(self, filename=None):
        if not filename:
            filename = self.filenaem
        if os.path.isfile(filename):
            result = pickle.loads(filename)
            if log_level == "DEBUG":
                print("lotto data(%s) is exist... loaded %d"%(filename, len(self.lotto_list)))
        else:
            result = {}
            if log_level == "DEBUG":
                print("lotto data(%s) is not exist"%(filename))
        return result


class LottoManager:
    HTTP_OK = 200
    log_level_list = ("DISABLE", "DEBUG")

    def __init__(self):
        self.set_log_level("DISABLE")
        self.saver = FileSaver()
        self.lotto_list = saver.load_lotto_data(log_level)

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
