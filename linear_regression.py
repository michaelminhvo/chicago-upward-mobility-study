import pandas as pd
import numpy as np
import math
import scipy.stats as st
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from scipy import stats


import argparse

parser = argparse.ArgumentParser(
    description='Calculate regression between two variables')
parser.add_argument("--data")
parser.add_argument("--column1")
parser.add_argument("--column2")
parser.add_argument("--state", help="Two-digit state 2010 FIPS code",
                    type=int)
parser.add_argument("--county", help="Three-digit county 2010 FIPS code but the original data file uses integers so it truncates leading zeroes",
                    type=int)

args = parser.parse_args()
data = args.data
usa = pd.read_csv(data)
column1 = args.column1
column2 = args.column2


cook_county = usa.loc[(usa['state'] == args.state) & (
    usa['county'] == args.county)]


cook_county.plot.scatter(
    x=column1, y=column2, c='DarkBlue')
plt.show()


def pearsonr_ci(x, y, alpha=0.05):
    ''' calculate Pearson correlation along with the confidence interval using scipy and numpy
    Parameters
    ----------
    x, y : iterable object such as a list or np.array
      Input for correlation calculation
    alpha : float
      Significance level. 0.05 by default
    Returns
    -------
    r : float
      Pearson's correlation coefficient
    pval : float
      The corresponding p value
    lo, hi : float
      The lower and upper bound of confidence intervals
    '''

    r, p = stats.pearsonr(x, y)
    r_z = np.arctanh(r)
    se = 1/np.sqrt(x.size-3)
    z = stats.norm.ppf(1-alpha/2)
    lo_z, hi_z = r_z-z*se, r_z+z*se
    lo, hi = np.tanh((lo_z, hi_z))
    return r, p, lo, hi


print("Pearson  r value, p-value, CI-low, CI-high {}".format(pearsonr_ci(
    cook_county[column1].fillna(0), cook_county[column2].fillna(0))))
