import numpy as np
from keras.models import Sequential
from keras.layers import Dense, TimeDistributed, Input, Dropout, Activation
from keras.optimizers import SGD
from LottoManager import LottoManager
from random import randint
from sklearn.model_selection import train_test_split

manager = LottoManager("DEBUG")
print("LottoManager Version = %s"%(manager.__version__))
manager.get_all_lotto()
manager.save_lotto_data()

lotto_data = manager.lotto_data

x_datas = []
y_datas = []

start_point = 100
last_point = len(lotto_data) + 1

for i in range(start_point, last_point):
    x = [0] * 45
    y = [0] * 45

    for j in range(1, i):
        tmp = lotto_data[j]["Num"]
        for num in tmp:
            x[num - 1] += 1
    x_max = max(x)
    x = list(map(lambda x: float(x)/float(x_max), x))

    for num in lotto_data[i]["Num"]:
        y[num - 1] = 1

    x_datas.append(x)
    y_datas.append(y)

deepth = 100
dropout_rate = 0.5
model = Sequential()
model.add(Dense(deepth ,input_dim=45, activation="relu"))
model.add(Dropout(dropout_rate))
model.add(Dense(deepth, activation="relu"))
model.add(Dropout(dropout_rate))
model.add(Dense(deepth, activation="relu"))
model.add(Dropout(dropout_rate))
model.add(Dense(deepth, activation="relu"))
model.add(Dropout(dropout_rate))
model.add(Dense(deepth, activation="relu"))
model.add(Dropout(dropout_rate))
model.add(Dense(deepth, activation="relu"))
model.add(Dropout(dropout_rate))
model.add(Dense(deepth, activation="relu"))
model.add(Dropout(dropout_rate))
model.add(Dense(deepth, activation="relu"))
model.add(Dense(45, activation='softmax'))

x_train, x_test, y_train, y_test = train_test_split(x_datas, y_datas, test_size=0.2,
                                                    random_state=randint(0, 1000))

# try using different optimizers and different optimizer configs
opt = SGD(lr=1e-2)
#binary_crossentropy
              #optimizer=['adam', 'rmsprop'][1],
model.compile(loss=['categorical_crossentropy', 'binary_crossentropy'][0],
              optimizer=opt,
              metrics=['accuracy'])

model.fit(x_train, y_train,
                  batch_size=1,
                  epochs=5,
                  validation_data=(x_test, y_test))

def lprint(x):
    result = []
    x = list(x[0])
    print(x)
    for _ in range(6):
        x_max = max(x)
        x_index = x.index(x_max)
        result.append(x_index + 1)
        x[x_index] = 0
    print(result)

lprint(model.predict(np.asarray([x_datas[-100]])))
lprint(model.predict(np.asarray([x_datas[-10]])))
lprint(model.predict(np.asarray([x_datas[-1]])))
