#-*-encoding:utf8-*-
#  impleting subplot to our stock graph
# take code from 18.py
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ochl
from matplotlib import style

style.use('fivethirtyeight')
print(style.available)

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graphs(stock):
    with open(stock+'.csv', 'r') as csvfile:
        fig = plt.figure('figure one')

        ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
        plt.title(stock)
        ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1)
        plt.xlabel('dates')
        plt.ylabel('price')
        ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1)

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

        candlestick_ochl(ax2, ohlc, width=0.4, colordown='r', colorup='g')

        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)

        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax2.grid(True)

        bbox_props = dict(boxstyle='round', fc='w', ec='k')
        ax2.annotate(str(closep[-1]), (date[-1],closep[-1]), xytext=(date[-1]+3,closep[-1]), bbox=bbox_props)

        plt.subplots_adjust(left=0.09, bottom=0.25, right=0.82, top=0.90, wspace=0.2, hspace=0)
        plt.show()


graphs('tsla')