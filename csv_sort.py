import csv
from datetime import datetime
import os
import sys

# Get input file path from command line
try:
    input_arg = sys.argv[1]
except:
    print('Please specify an input CSV! \n')
path_to_input = os.path.join(sys.path[0], input_arg)
path_to_output = path_to_input[0:-4] + '_sorted.csv'

with open(path_to_input, 'r') as csv_input, open(path_to_output, 'w') as csv_output:
    # Read CSV and hold it as a list of dictionaries, [column]: [value]
    input_reader = csv.DictReader(csv_input)

    # Get the header from the input and prepare the output file with that header
    fieldnames = input_reader.fieldnames
    output_writer = csv.DictWriter(csv_output, fieldnames)
    output_writer.writeheader()

    # Sort the input file by device ID and date
    # Making sure to parse date rather than simple string compare
    # so that e.g. 1/2/18 is before 1/18/18
    sorted_input = sorted(input_reader, key=lambda row: (
        row['Device_ID'], datetime.strptime(row['Date'], '%m/%d/%y')))

    # Write the sorted input to the output file
    output_writer.writerows(sorted_input)
