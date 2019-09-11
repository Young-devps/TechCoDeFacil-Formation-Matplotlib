#-*-encoding:utf8-*-
#  addinf more indicator to our charts
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ochl
from matplotlib import style

style.use('seaborn-notebook')
print(style.available)
print(plt.__file__)

MA1 = 10
MA2 = 20

def moving_average(values, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas

def high_minus_low(highs, lows):
    return highs-lows

highs = [11, 12, 15, 14, 13]
lows = [5, 6, 2, 6, 7]

h_l = list(map(high_minus_low, highs, lows))
print(h_l)

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graphs(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
    plt.title(stock)
    ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1)
    plt.xlabel('dates')
    plt.ylabel('price')
    ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1)

    with open(stock+'.csv', 'r') as csvfile:
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

    ma1 = moving_average(closep, MA1)
    ma2 = moving_average(closep, MA2)
    start = len(date[MA2-1:])

    h_l = list(map(high_minus_low, hightp, lowp))
    ax1.plot_date(date, h_l, '-')

    candlestick_ochl(ax2, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')

    for label in ax2.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax2.grid(True)

    bbox_props = dict(boxstyle='round', fc='w', ec='k', lw=1)
    ax2.annotate(str(closep[-1]), (date[-1], closep[-1]), xytext=(date[-1]+3, closep[-1]), bbox=bbox_props)

    print(len(date), len(ma1))
    ax3.plot(date[-start:], ma1[-start:])
    ax3.plot(date[-start:], ma2[-start:])

    plt.subplots_adjust(left=0.09, bottom=0.25, right=0.82, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graphs('tsla')