import os
import pprint

d = {}
c = 0

path = r"C:\Users\allpyl\PycharmProjects\Python_kod\Python_for_WEB\zadanie_1_words"

for fileName in os.listdir(path):
    fullPath = os.path.join(path, fileName)
    if os.path.isfile(fullPath) and fileName[-3:].lower() == 'txt':
        with open(fileName, 'r', encoding='utf-8') as file:
            for i in file.read():
                y = i.lower()
                if y in 'abcdefghijklmnopqrstuvwxyz':
                    c += 1
                    if y in d:
                        d[y] += 1
                    else:
                        d[y] = 1

pprint.pprint("Częstotliwość występowania każdej litery we wszystkich plikach: {}".format(d))
