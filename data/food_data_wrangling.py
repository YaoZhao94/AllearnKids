from os import listdir
from os.path import isfile, join
import re
import pandas as pd
import wikipedia


def get_data(dir):
    a = 249
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
    holder = []
    allergy = []
    summary = []
    url = []
    for x in onlyfiles:
        address = join(dir, x)
        name = x.replace('.txt', '')
        file = open(address, "r").readlines()
        i = 0
        while i < len(file):
            file[i] = file[i].strip().lower()
            i += 1

        for x in file:
            holder.append(re.split('[+]|\(| or |\*|\/|\,', x)[0].strip())
            allergy.append(name)

            try:
                summary.append(wikipedia.summary(x))
            except:
                summary.append('')
            try:
                url.append(wikipedia.page(x).url)
            except:
                url.append('')
            print (a)
            a-=1
    return (holder, allergy, summary, url)


if __name__ == '__main__':

    get_data.run(dir)





