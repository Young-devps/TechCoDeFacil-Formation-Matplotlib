#-*-encoding:utf8-*-
#  annotation last price in edge of matplolib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ochl
from matplotlib import style

style.use('classic')

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


with open('tsla.csv', 'r') as csvfile:
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

    x = 0
    y = len(date)
    ohlc = []
    while x < y:
        append_me = date[x], openp[x], hightp[x], lowp[x], closep[x], aclosep[x], volume[x]
        ohlc.append(append_me)
        x+=1

    candlestick_ochl(ax1, ohlc, width=0.4, colordown='r', colorup='g')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)

    bbox_props = dict(boxstyle='larrow', fc='w', ec='k')
    ax1.annotate(str(closep[-1]), (date[-1],closep[-1]), xytext=(date[-1]+3,closep[-1]), bbox=bbox_props)

    # #example de annotate
    # ax1.annotate('Bad day!', (date[20], closep[20]), xytext=(0.8, 0.9), textcoords='axes fraction', arrowprops=dict(facecolor='grey', color='grey'))
    #
    # #example de text
    # font_dict = {'family':'serif', 'color':'darkred', 'size':15}
    # ax1.text(date[10], closep[10], 'evolution', fontdict=font_dict)

    plt.xlabel('dates')
    plt.ylabel('price')
    plt.title('finance with python  matplotlib')
    #plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.25, right=0.82, top=0.90, wspace=0.2, hspace=0)
    plt.show()