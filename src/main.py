from LottoManager import LottoManager

manager = LottoManager("DEBUG")
print("LottoManager Version = ", manager.__version__)
manager.get_all_lotto()
manager.save_lotto_data()
