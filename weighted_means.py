import pandas as pd
import numpy
import math

# all = pd.read_csv(
#     "/Users/vo/Desktop/github/python-tutorial/tract_outcomes_simple.csv")
all_data = pd.read_csv(
    "/Users/vo/Desktop/github/python-tutorial/tract_outcomes_early.csv")


def weighted_avg_and_std(values, weights):
    """
    Return the weighted average and standard deviation.

    values, weights -- Numpy ndarrays with the same shape.
    """
    average = numpy.average(values, weights=weights)
    # Fast and numerically precise:
    variance = numpy.average((values-average)**2, weights=weights)
    return (average, math.sqrt(variance))


def wavg(group, avg_name, weight_name):
    """ http://stackoverflow.com/questions/10951341/pandas-dataframe-aggregate-function-using-multiple-columns
    In rare instance, we may not have weights, so just return the mean. Customize this if your business case
    should return otherwise.
    """
    d = group[avg_name]
    w = group[weight_name]
    try:
        return (d * w).sum() / w.sum()
    except ZeroDivisionError:
        return d.mean()


# 17 == Illinois. Two-digit state 2010 FIPS code
# 031 County. Three-digit county 2010 FIPS code but the original data file uses integers so it truncates the "0"
# a = a[(a[:, 0] == "17") & (
#     a[:, 1] == "31") & (a[:, 2] == "833000")]
def print_stats(data, statistic_name):
    print(wavg(data, statistic_name, 'pooled_pooled_count'))
    illinois = data[data["state"] == 17]
    print(wavg(illinois, statistic_name, 'pooled_pooled_count'))
    county = illinois[illinois["county"] == 31]
    print(wavg(county, statistic_name, 'pooled_pooled_count'))
    print(illinois[[statistic_name]].describe())
    print(weighted_avg_and_std(illinois[statistic_name].fillna(0),
                               illinois["pooled_pooled_count"].fillna(0)))
    print(weighted_avg_and_std(county[statistic_name].fillna(0),
                               county["pooled_pooled_count"].fillna(0)))


# print_stats(all, 'kfr_pooled_pooled_p25')
print_stats(all_data, 'kfr_pooled_pooled_p75')


# print((0.374760951001459-.14)/0.07979831324219493)
# print((0.374760951001459-.01)/0.07979831324219493)
