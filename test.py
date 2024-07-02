import numpy
from scipy import stats

speed=[86,87,88,86,87,85,86,32,111,138,28,59,77,97,86]

mean_test=numpy.mean(speed)
median_test=numpy.median(speed)
mode_test=stats.mode(speed)

print(mean_test, "\n")
print(median_test, "\n")
print(mode_test)
