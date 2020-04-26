import matplotlib.pyplot as plt, numpy

def mean(xarr: list):
    '''returns the average of a list'''

    mean = 0
    for x in xarr:
        mean += x
    mean /= len(xarr)

    return mean

def variance(xarr: list):
    '''Returns population variance:
     The average squared distance from the mean
     '''
    variance = 0
    mean_x = mean(xarr)
    for x in xarr:
        variance += (mean_x - x) ** 2
    variance /= len(xarr) #Population size = len(xarr)

    return variance

def covariance(xarr: list, yarr: list):
    '''Returns population covariance:
    The average product of the difference of x to the mean and the difference of y to the mean
    '''
    meanx = mean(xarr)
    meany = mean(yarr)

    covar = 0
    for i in range(len(xarr)):
        covar += (xarr[i] - meanx) * (yarr[i] - meany)
    covar /= len(xarr)

    return covar

def leastsquares(xarr: list, yarr: list):
    '''Returns slope and y intercept of the line of best fit. 
    In the form slope, y_int'''
    slope = covariance(xarr, yarr)/variance(xarr)
    y_int = mean(yarr) - slope * mean(xarr)#Because the line goes through the point with mean x and mean y

    return slope, y_int

def plot_line_data(xarr: list, yarr: list, xlabel = "", ylabel = "", title = ""):
    '''Plots line and data with matplotlib'''
    slope, y_int = leastsquares(xarr, yarr)
    print(slope,y_int)
    print(min(xarr), min(yarr))
    x = numpy.arange(min(xarr), max(xarr), 0.001)

    plt.scatter(xarr,yarr)
    plt.plot(x, slope*x + y_int, "-g", label= "y = " + str(slope)+ " + " + str(y_int))

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    y_set = [1.22,1.17,1.15,1.1,1.1,1.05,1.03,0.95]
    x_set = [0.05,0.095,0.125,0.19,0.22, 0.3,0.375,0.47]
    plot_line_data(x_set, y_set,xlabel="Current",ylabel="Voltage", title="I-V Curve for Battery")
