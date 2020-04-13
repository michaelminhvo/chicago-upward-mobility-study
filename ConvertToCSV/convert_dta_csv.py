import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='convert to csv')
parser.add_argument("--i")
parser.add_argument("--o")

args = parser.parse_args()

data = pd.io.stata.read_stata(args.i)
data.to_csv(args.o)
