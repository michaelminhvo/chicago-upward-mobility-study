import pandas as pd
import numpy
import math
import scipy.stats as st
import matplotlib.pyplot as plt

# TODO refactor to read command line argument
# all = pd.read_csv(
#     "/Users/vo/Desktop/github/opportunity-atlast-homework-1/tract_outcomes_simple.csv")
usa = pd.read_csv(
    "/Users/vo/Desktop/github/opportunity-atlast-homework-1/atlas.csv")

count_pooled = "count_pooled"


def weighted_avg_and_std(values, weights):
    """
    Return the weighted average and standard deviation.

    values, weights -- Numpy ndarrays with the same shape.
    """
    average = numpy.average(values, weights=weights)
    # Fast and numerically precise:
    variance = numpy.average((values-average)**2, weights=weights)
    return (average, math.sqrt(variance))


# 17 == Illinois. Two-digit state 2010 FIPS code
# 031 County. Three-digit county 2010 FIPS code but the original data file uses integers so it truncates the "0"
# a = a[(a[:, 0] == "17") & (
#     a[:, 1] == "31") & (a[:, 2] == "833000")]
def print_stats(data, statistic_name, count_pooled):
    wa = weighted_avg_and_std(data[statistic_name].fillna(
        0), data[count_pooled].fillna(0))
    print("{} {}".format("USA (Mean, SD): ", wa))
    illinois = data[data["state"] == 17]
    county = illinois[illinois["county"] == 31]

    print("{} {}".format("State (Mean, SD): ", (weighted_avg_and_std(illinois[statistic_name].fillna(0),
                                                                     illinois[count_pooled].fillna(0)))))
    print("{} {}".format("County (Mean, SD): ", (weighted_avg_and_std(county[statistic_name].fillna(0),
                                                                      county[count_pooled].fillna(0)))))


cook_county = usa.loc[(usa['state'] == 17) & (
    usa['county'] == 31)]


# cook_county.plot.scatter(x='kfr_pooled_p25', y='kfr_pooled_p75', c='DarkBlue')
# plt.show()

# If you don't fill NAN with zeros the data takes forever to run. This means that I should always run it with zeros
print(cook_county['kfr_pooled_p25'].fillna(0).corr(
    cook_county['kfr_pooled_p75'].fillna(0)))
