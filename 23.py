#-*-encoding:utf8-*-
#  multi y axis plotting volume on stock chart
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ochl
from matplotlib import style

# fivethirtyeight
style.use('fivethirtyeight')
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
    plt.ylabel('H-L')
    ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1, sharex=ax1)
    plt.ylabel('price')
    ax2v = ax2.twinx()
    ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
    plt.ylabel('MAvgs')

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
    ax1.plot_date(date[-start:], h_l[-start:], '-')
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='lower'))

    candlestick_ochl(ax2, ohlc[-start:], width=0.4, colorup='#77d879', colordown='#db3f3f')

    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=7, prune='upper'))
    ax2.grid(True)

    bbox_props = dict(boxstyle='round', fc='w', ec='k', lw=1)
    ax2.annotate(str(closep[-1]), (date[-1], closep[-1]), xytext=(date[-1]+3, closep[-1]), bbox=bbox_props)
    ax2v.fill_between(date[-start:], 0, volume[-start:], fc='#0079a3', alpha=0.4)
    ax2v.axes.yaxis.set_ticklabels([])
    ax2v.grid(False)
    ax2v.set_ylim(0, 3*volume.max())

    ax3.plot(date[-start:], ma1[-start:])
    ax3.plot(date[-start:], ma2[-start:])
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                     where=(ma1[-start:] < ma2[-start:]),
                     fc='g', ec='r', alpha=0.5)
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                     where=(ma1[-start:] > ma2[-start:]),
                     fc='r', ec='g', alpha=0.5)
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='upper'))
    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)

    # plots stuffs
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.subplots_adjust(left=0.09, bottom=0.25, right=0.82, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graphs('GOOG')