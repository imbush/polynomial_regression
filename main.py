def get_dim(array):
    '''returns height,width'''
    if isinstance(array[0], list):
        height = len(array)
        width = len(array[0])
    else:
        height = 1
        width = len(array)
    return height,width

def multiply(array1: list, array2: list):
    '''Performs matrix multiplication. array1 times array2'''
    height1, width1 = get_dim(array1)
    height2, width2 = get_dim(array2)

    array3 = []

    for a in range(height1):
        row =[]
        for b in range(width2):
            x = 0
            for c in range(width1):
                x += array1[a][c] * array2[c][b]
            row.append(x)
        array3.append(row)
    return array3


def add(array1, array2, coeff1 = 1, coeff2 = 1):
    '''adds two matrices, they must have the same dimensions'''
    height, width = get_dim(array1)
    array3 = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(coeff1 * array1[y][x] + coeff2 * array2[y][x])
        array3.append(row)
    return array3

def scale(array1, coeff):
    '''Performs scalar multiplication of the inputed array by the coefficient'''
    height, width = get_dim(array1)
    array3 = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(array1[y][x] * coeff)
        array3.append(row)
    return array3

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
    for x in xarr:
        variance += (mean() - x) ** 2
    variance /= len(xarr) #Population size = len(xarr)

    return variance

def covariance(xarr: list, yarr: list):
    ''''''
    meanx = mean(xarr)
    meany = mean(yarr)

    covar = 0
    for i in range(len(xarr)):
        covar += (xarr - meanx) * (yarr - meany)
    covar /= len(xarr)

    return covar

def leastsquares(xarr: list, yarr: list):
    '''Returns slope and y intercept of the line of best fit. 
    In the form slope, y_int'''
    slope = covariance(xarr, yarr)/variance(xarr)
    y_int = mean(yarr) - slope * mean(xarr)#Because the line goes through the point with mean x and mean y

    return slope, y_int