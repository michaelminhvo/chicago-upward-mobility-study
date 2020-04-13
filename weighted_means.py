import pandas as pd
import numpy
import math
import scipy.stats as st
import argparse

parser = argparse.ArgumentParser(description='Calculate weighted mean')
parser.add_argument("--data")
parser.add_argument("--percentile_name")
parser.add_argument("--tract", help="The tract number (last 6 digits)",
                    type=int)
parser.add_argument("--state", help="Two-digit state 2010 FIPS code",
                    type=int)
parser.add_argument("--county", help="Three-digit county 2010 FIPS code but the original data file uses integers so it truncates leading zeroes",
                    type=int)
parser.add_argument(
    "--count_pooled", help="The csv column name for the weight to use for each of the percentiles")

args = parser.parse_args()
data = args.data
usa = pd.read_csv(data)

# The weight to use for each of the percentiles
count_pooled = args.count_pooled


def weighted_avg_and_std(values, weights):
    """
    Return the weighted average and standard deviation.

    values, weights -- Numpy ndarrays with the same shape.
    """
    average = numpy.average(values, weights=weights)
    # Fast and numerically precise:
    variance = numpy.average((values-average)**2, weights=weights)
    return (average, math.sqrt(variance))


def print_stats(data, statistic_name, count_pooled):
    wa = weighted_avg_and_std(data[statistic_name].fillna(
        0), data[count_pooled].fillna(0))
    illinois = data[data["state"] == args.state]
    county = illinois[illinois["county"] == args.county]

    print("{} {}".format("USA (Mean, SD): ", wa))
    print("{} {}".format("State (Mean, SD): ", (weighted_avg_and_std(illinois[statistic_name].fillna(0),
                                                                     illinois[count_pooled].fillna(0)))))
    print("{} {}".format("County (Mean, SD): ", (weighted_avg_and_std(county[statistic_name].fillna(0),
                                                                      county[count_pooled].fillna(0)))))


print_stats(usa, args.percentile_name, count_pooled)


# fulton = usa.loc[(usa['state'] == args.state) & (
#     usa['county'] == args.county) & (usa['tract'] == args.tract)]

# print(st.norm.cdf(-1.768042827))
# print(st.norm.cdf(0.0517225389))
# print(st.norm.cdf(-0.2160341725))

# # 75th percentile
# print(st.norm.cdf(-1.406208284))
# print(st.norm.cdf(0.0912927634))
# print(st.norm.cdf(-0.3764243194))

# # 100th percentile
# print(st.norm.cdf(-0.8490051785))
# print(st.norm.cdf(-0.3754639977))
# print(st.norm.cdf(0.07423620524))
