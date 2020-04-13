import pandas as pd
data = pd.io.stata.read_stata(
    '/Users/vo/Desktop/github/opportunity-atlast-homework-1/atlas.dta')
data.to_csv('/Users/vo/Desktop/github/opportunity-atlast-homework-1/atlas.csv')
