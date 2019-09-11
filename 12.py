#-*-encoding:utf8-*-
#  spines and horizontal lines
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import datetime as dt


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


with open('TSLA.csv', 'r') as csvfile:
    fig = plt.figure('figure one')
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    ax1.grid(True, color='g', linestyle='-', linewidth=0.1)

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

    ax1.plot_date(date, closep, '-', label='price')
    ax1.plot([], [], linewidth=5, label='loss', color='r', alpha=0.5)
    ax1.plot([], [], linewidth=5, label='loss', color='g', alpha=0.5)
    # ax1.axhline(closep[0], color='k', linewidth=1)
    ax1.fill_between(date, closep, closep[700], where=(closep>closep[700]), facecolor='g', alpha=0.3)
    ax1.fill_between(date, closep, closep[700], where=(closep<closep[700]), facecolor='r', alpha=0.3)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')
    ax1.set_yticks([0, 100, 200, 300, 400, 500])

    # ax1.spines['left'].set_color('c')
    # ax1.spines['top'].set_visible(False)
    # ax1.spines['right'].set_visible(False)
    # ax1.spines['left'].set_linewidth(3)

    # ax1.tick_params(axis='x', colors='#f06215')

    plt.xlabel('dates')
    plt.ylabel('close price')
    plt.title('finance with python  matplotlib')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()