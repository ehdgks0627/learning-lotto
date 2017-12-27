import pickle
import os

class FileSaver:
    def __init__(self, log_level, filename="lotto.data"):
        self.filename = filename
        self.log_level = log_level

    def save_lotto_data(self, lotto_list, filename=None):
        if not filename:
            filename = self.filename
        f = open(filename, "wb")
        pickle.dump(lotto_list, f)
        f.close()

    def load_lotto_data(self, filename=None):
        if not filename:
            filename = self.filename
        if os.path.isfile(filename):
            f = open(filename, "rb")
            result = pickle.load(f)
            f.close()
            if self.log_level == "DEBUG":
                print("lotto data(%s) is exist... loaded %d"%(filename, len(result)))
        else:
            result = {}
            if self.log_level == "DEBUG":
                print("lotto data(%s) is not exist"%(filename))
        return result
