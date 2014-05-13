import argparse
from pandas import read_csv
import docx

parser = argparse.ArgumentParser(description='Read a CSV and genrate documentation')
parser.add_argument('--filename', 
                   help='an input file for reading as a CSV')
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
print args.filename
df = read_csv(args.filename)
#print df
documents = df['TABLE_NAME'].unique()
print documents