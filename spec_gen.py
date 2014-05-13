import argparse
import pandas as pd
from docx import *
source_system_dict ={}
table_source = []
parser = argparse.ArgumentParser(description='Read a CSV and genrate documentation')
parser.add_argument('--filename', 
                   help='an input file for reading as a CSV')
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
#parser.add_argument("--templatefile", help="This is the template specification document")					
parser.add_argument("--basedocname",help="The name of the document, the table name will be added at the end")
args = parser.parse_args()
print args.filename
df = pd.read_csv(args.filename)
#print df
documents = df['TABLE_NAME'].unique()
def read_template():
#setup template dictionary
	dict = {}


	return dict

def create_file(filename):
# use the filename parsed from the csv file to create a word document returning a file_handle
	opened_file = open(filename,'w')
	return opened_file

def write_data(data_file,text_dict,subset_df,table_name):
# the subset_df is the data frame that contains the source to target data for this mapping
# the data file is the spec document
#the text_dict is the dictionary that contains the template data. 
# Default set of relationshipships - the minimum components of a document
	relationships = relationshiplist()

	# Make a new document tree - this is the main part of a Word document
	document = newdocument()

	# This xpath location is where most interesting content lives
	body = document.xpath('/w:document/w:body', namespaces=nsprefixes)[0]
	# Add an image
	relationships, picpara = picture(relationships, 'gmf.png',
									 'This is the GMF logo')
	body.append(picpara)

	# Append two headings and a paragraph
	body.append(heading("Data Vault: Satellite", 1))
	body.append(heading('ETL Technical Specs Document', 2))
	body.append(heading('1.0 Table of Contents',3))
	body.append(heading('3.0 Description',3))
	body.append(paragraph('This document provides specifications for creating and loading S_satellite and H_hub.'))

	body.append(heading('4.0 Assumption',3))
	body.append(paragraph('The following are assumptions made about the project in regards to ETL\'s responsibilities:'
		'1.	The entity will adhere to Data Vault standards (link in section 5.0 Related Documents)'))
	body.append(heading('5.0 Technical Requirements',3))
	body.append(heading('5.1 '+table_name,3))
	body.append(paragraph('The following are assumptions made about the project in regards to ETL\'s responsibilities:'
		'1.	The entity will adhere to Data Vault standards (link in section 5.0 Related Documents)'))

	body.append(paragraph([('For those of us who prefer something simpler, I '
						  'made docx.', 'i')]))
	body.append(heading('Making documents', 2))
	body.append(paragraph('The docx module has the following features:'))

	# Add some bullets
	points = ['Paragraphs', 'Bullets', 'Numbered lists',
			  'Multiple levels of headings', 'Tables', 'Document Properties']
	for point in points:
		body.append(paragraph(point, style='ListBullet'))

	body.append(paragraph('Tables are just lists of lists, like this:'))
	# Append a table
	tbl_rows = [ ['A1', 'A2', 'A3']
			   , ['B1', 'B2', 'B3']
			   , ['C1', 'C2', 'C3']
			   ]
	body.append(table(tbl_rows))

	body.append(heading('Editing documents', 2))
	body.append(paragraph('Thanks to the awesomeness of the lxml module, '
						  'we can:'))
	points = [ 'Search and replace'
			 , 'Extract plain text of document'
			 , 'Add and delete items anywhere within the document'
			 ]
	for point in points:
		body.append(paragraph(point, style='ListBullet'))


	# Search and replace
	print 'Searching for something in a paragraph ...',
	if search(body, 'the awesomeness'):
		print 'found it!'
	else:
		print 'nope.'

	print 'Searching for something in a heading ...',
	if search(body, '200 lines'):
		print 'found it!'
	else:
		print 'nope.'

	print 'Replacing ...',
	body = replace(body, 'the awesomeness', 'the goshdarned awesomeness')
	print 'done.'

	# Add a pagebreak
	body.append(pagebreak(type='page', orient='portrait'))

	body.append(heading('Ideas? Questions? Want to contribute?', 2))
	body.append(paragraph('Email <python.docx@librelist.com>'))

	# Create our properties, contenttypes, and other support files
	title = 'Python docx demo'
	subject = 'A practical example of making docx from Python'
	creator = 'Mike MacCana'
	keywords = ['python', 'Office Open XML', 'Word']

	coreprops = coreproperties(title=title, subject=subject, creator=creator,
							   keywords=keywords)
	appprops = appproperties()
	c_types = contenttypes()
	web_settings = websettings()
	word_relationships = wordrelationships(relationships)

	# Save our document
	savedocx(document, coreprops, appprops, c_types, web_settings,
			 word_relationships, filename)
	result = 0
	return result	
for doc in documents:
	filename = args.basedocname+doc+'.docx'
	print filename
	subset_df = df.loc[(df.TABLE_NAME ==doc),]
	data_file = create_file(filename)
	text_dict = read_template()
	write_data(data_file,text_dict,subset_df,doc)
	
	
