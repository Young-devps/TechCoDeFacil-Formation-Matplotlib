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



with open('EBAY.csv', 'r') as csvfile:
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
                                                                    converters={0 : bytespdate2num('%Y-%m-%d')})



    plt.xlabel('dates')
    plt.ylabel('close price')
    #plt.plot(date, closep, label='price')
    plt.plot_date(date, closep, '-', label='price')
    plt.title('finance with python  matplotlib')
    plt.legend()
    plt.show()




# x,y= np.loadtxt('example.txt', delimiter=',', unpack=True)
