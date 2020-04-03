import pandas as pd
import numpy
import math
import scipy.stats as st

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


# print_stats(usa, 'kfr_pooled_p25', count_pooled)
# print_stats(usa, 'kfr_pooled_p75', count_pooled)
print_stats(usa, 'kfr_pooled_p100', count_pooled)

fulton = usa.loc[(usa['state'] == 17) & (
    usa['county'] == 31) & (usa['tract'] == 833000)]

print(st.norm.cdf(-1.768042827))
print(st.norm.cdf(0.0517225389))
print(st.norm.cdf(-0.2160341725))

# 75th percentile
print(st.norm.cdf(-1.406208284))
print(st.norm.cdf(0.0912927634))
print(st.norm.cdf(-0.3764243194))

# 100th percentile
print(st.norm.cdf(-0.8490051785))
print(st.norm.cdf(-0.3754639977))
print(st.norm.cdf(0.07423620524))


# print(fulton['kfr_pooled_p25'])
print(fulton['kfr_pooled_p100'])
# print(fulton['count_pooled'])
