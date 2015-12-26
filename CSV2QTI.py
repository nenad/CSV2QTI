import argparse
from CSVImporter import CSVImporter
import xmlGenerator
import os
import shutil

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, 
description=
"""Create zip with xml which are ready to be imported in TAO
CSV Structure is: question, correct_answer_index, answers_separated_by_delimiter...
Example: "What is opposite of yes?", "2", "Maybe", "Yes", "Never"
""")
parser.add_argument('csv', metavar='csv', help='csv file to be converted')
parser.add_argument('output', metavar='output', help='Export filename')
parser.add_argument('prefix', metavar='prefix', help='Prefix for xml files (ex. IT_General_Knowledge')
parser.add_argument('--delimiter', metavar='delimiter', default=',', help='Delimiter for the csv file')
parser.add_argument('--quotechar', metavar='quotechar', default='"', help='Quote character for the csv file')

args = parser.parse_args()
questions = CSVImporter(args.delimiter, args.quotechar).getQuestions(args.csv)

if not os.path.exists(args.output):
	os.makedirs(args.output)
if not os.path.exists(args.output + '/' + args.output):
	os.makedirs(args.output + '/' + args.output)

for i in range(0, len(questions)):
	item_id = '%03d' % i
	questions[i].title = args.prefix + "_" + item_id
	questions[i].title_id = questions[i].title.lower()
	xmlGenerator.saveXML(questions[i], args.output + '/' + args.output + '/' + questions[i].title + '.xml')
xmlGenerator.generateManifest(args.output, args.prefix + "_pack")
print "%d items generated!" % len(questions)
shutil.make_archive(args.output, 'zip', args.output)
shutil.rmtree(args.output, ignore_errors=True)