#costomisation basique et rotation de label
import matplotlib.pyplot as plt
import numpy as np
import csv
import matplotlib.dates as mdates

x = []
y = []
w = []
z = []


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconverter


with open('TSLA.csv', 'r') as csvfile:
    fig = plt.figure('figure one')
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    ax1.grid(True, color='g', linestyle='-', linewidth=0.3)

    source_code = csvfile.read()
    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'Date' is not line and 'Close' not in line:
                stock_data.append(line)

    date, openp, hightp, lowp, closep, aclosep, volume = np.loadtxt(stock_data,
                                                                    delimiter=',',
                                                                    unpack=True,
                                                                    converters={0: bytespdate2num('%Y-%m-%d')})


    plt.xlabel('dates')
    plt.ylabel('close price')
    #plt.plot_date(date, closep, '-', label='price')

    ax1.plot_date(date, closep, '-', label='price')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.title('finance with python  matplotlib')
    plt.legend()
    #plt.subplots_adjust(left=0.9, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()