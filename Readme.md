
To get the weighted mean run 

To get the mean and standard deviation of children whose households were at the bottom 25th percentile:
```
python weighted_means.py --data=atlas.csv --percentile_name=kfr_pooled_p25 --state=17 --tract=833000 --county=31 --count_pooled=count_pooled
```

To get the mean and standard deviation of children whose households were at the top 75th percentile:
```
python weighted_means.py --data=atlas.csv --percentile_name=kfr_pooled_p75 --state=17 --tract=833000 --county=31 --count_pooled=count_pooled
```

To get the mean and standard deviation of children whose households were at the top 100th percentile:
```
python weighted_means.py --data=atlas.csv --percentile_name=kfr_pooled_p100 --state=17 --tract=833000 --county=31 --count_pooled=count_pooled
```
