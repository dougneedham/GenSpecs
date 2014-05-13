import argparse
import pandas as pd
import docx
source_system_dict ={}
table_source = []
parser = argparse.ArgumentParser(description='Read a CSV and genrate documentation')
parser.add_argument('--filename', 
                   help='an input file for reading as a CSV')
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("--basedocname",help="The name of the document, the table name will be added at the end")
args = parser.parse_args()
print args.filename
df = pd.read_csv(args.filename)
#print df
documents = df['TABLE_NAME'].unique()
def read_template():
#setup template dictionary
	return dict

def create_file(filename):
# use the filename parsed from the csv file to create a word document returning a file_handle
	opened_file = open(filename,"wb")
	return opened_file

def write_data(data_file,text_dict,subset_df):
# the subset_df is the data frame that contains the source to target data for this mapping
# the data file is the spec document
#the text_dict is the dictionary that contains the template data. 
	result = 0
	return result	
for doc in documents:
	filename = args.basedocname+doc
	print filename
	subset_df = df.loc[(df.TABLE_NAME ==doc),]
	data_file = create_file(filename)
	text_dict = read_template()
	write_data(data_file,text_dict,subset_df)
	
	
