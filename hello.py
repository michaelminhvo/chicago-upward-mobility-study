# Use python 2.7.16 as numpy isn't compatible with the latest python version 3.15
import numpy as np

a = np.genfromtxt(open(
    "/Users/vo/Desktop/github/python-tutorial/tract_outcomes_simple.csv"), dtype=None, delimiter=",")

# 17 == Illinois. Two-digit state 2010 FIPS code
# 031 County. Three-digit county 2010 FIPS code but the original data file uses integers so it truncates the "0"
a = a[(a[:, 0] == "17") & (a[:, 1] == "31") & (a[:, 2] == "833000")]


print(a)

print ('{} {}'.format(len(a), 'rows'))
