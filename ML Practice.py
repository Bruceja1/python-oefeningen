import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# Mean = average value
x_mean = numpy.mean(speed)

# Median = middlemost value AFTER the numbers are sorted
x_median = numpy.median(speed)
print(x_mean)
print(x_median) 

speed = [99,86,87,88,86,103,87,94,78,77,85,86]
# Mode = number that appears the most
x_mode = stats.mode(speed)
print(x_mode)

# Standard deviation. Small number = values are close to average.
speed = [86,87,88,86,87,85,86]
x_std = numpy.std(speed)
print(x_std)
