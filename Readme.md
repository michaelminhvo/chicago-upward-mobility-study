This code is for assignment #1 from https://opportunityinsights.org/course/. The course uses Strata, a paid product. We instead convert the Strata file into a csv using:

```
python ConvertToCSV/convert_dta_csv.py --i=atlas.dta --o=atlas.csv
mv ConvertToCSV/atlas.csv aslas.csv
```



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

For question 4 and 5 on the assignment:

To compare the sample value to the sample mean (for example for West Fulton tract), we calculate the standard deviation and call the function 

```
st.norm.cdf(value)
```


Question 6:
Calculate correlation between 25th and 75th percentile in the tracts in Cook County. 
```
python linear_regression.py --data=atlas.csv --state=17 --county=31 --column1=k
fr_pooled_p25 --column2=kfr_pooled_p75
```

Question 7:

```
python linear_regression.py --data=atlas.csv --state=17 --county=31 --column1=kfr_black_p25 --column2=kfr_black_p75
python linear_regression.py --data=atlas.csv --state=17 --county=31 --column1=kfr_asian_p25 --column2=kfr_asian_p75
python linear_regression.py --data=atlas.csv --state=17 --county=31 --column1=kfr_white_p25 --column2=kfr_white_p75
```

Question 8:

```
python linear_regression.py --data=atlas.csv --state=17 --county=31 --column1=kfr_white_p25 --column2=singleparent_share1990
python linear_regression.py --data=atlas.csv --state=17 --county=31 --column1=kfr_black_p25 --column2=singleparent_share1990
```


