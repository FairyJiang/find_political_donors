### Insight Data Engineering - coding challenge
### Submitted by Fairy Jiang 10/30/2017

### File Directory:
Input file: ./input/itcont.txt

Output file: ./output/medianvals_by_date.txt
             ./output/medianvals_by_date.txt
             
Source file: ./src/find_political_donors.py

run.sh

insight_testsuite

### Modules
import os

from collections import defaultdict

from datetime import datetime

import numpy

### Structure of the code
read(): this function reads the text file in input folder into a list,
        according to the requirements on the data
        
find_same(): this function is used to find the same ID, ZIPCODE, DATE,
        returns the index of the same elements
        
validate_date(): this function is used to validate the date format

alculate_by_type(): this function is used to calculate the total amount
        of contributions with specific ID and ZIPCODE or DATE
        
main(): this function is the main function to calculate the total and median
        contributions under specific ID and ZIPCODE or DATE, outputs text
        files to write in the results

### Test
Use run_test.sh to compare the output with the files in test folder, if
same, show PASS


