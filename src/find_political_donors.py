# Program that calculates the individual political contributions

# Importing the necessary modules
import os
from collections import defaultdict
from datetime import datetime
import numpy

# Set path to text file
dir = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
file_input_path = dir+'/input/itcont.txt'
file_output_path_zip = dir+'/output/medianvals_by_zip.txt'
file_output_path_date = dir+'/output/medianvals_by_date.txt'


# This function reads the input text file
def read(file_path):
    data = []
    with open(file_input_path) as file_object:
        lines = file_object.readlines()
        for line in lines:
            temp = line.split('|')
            if temp[15] == '' and temp[0] !='' and temp[14] != '':
                data.append({'ID':temp[0], 'ZIP':temp[10], 'DT':temp[13], 'AMT':temp[14], 'OTHER':temp[15]})
    return data


# This function finds the same elements and store the index in a dictionary
def find_same(list1):
    dict1 = defaultdict(list)
    for i,item in enumerate(list1):
        dict1[item].append(i)
    return dict1


# This function validates the date format in MMDDYY
def validate_date(date):
    flg = 0
    try:
        datetime.strptime(date, '%m%d%Y')
    except ValueError:
        flg = 1
    return flg


# This function calculates the total and median amount of contributions by ZIP or DATE
def calculate_by_type(data_for_type, type, AMT):
    data_output = []
    for key,value in data_for_type.items():
        type_id = []
        AMT_id = []
        for i in value:
            type_id.append(type[i])
            AMT_id.append(AMT[i])
        type_same = find_same(type_id)
        for k,v in type_same.items():
            AMT_type = []
            for i in v:
                AMT_type.append(AMT_id[i])
            data_output.append({'ID':key,'TYPE':k,'TOTAL':sum(AMT_type),'COUNT':len(AMT_type),'MEDIUM':int(round(numpy.median(AMT_type),0))})
    return data_output


# Main
def main():
    data = read(file_input_path)
    # Calculation by zip
    ZIP = []
    ID = []
    AMT = []
    for donor in data:
        if len(donor['ZIP']) == 5 or len(donor['ZIP']) == 9 :
            ZIP.append(donor['ZIP'])
            ID.append(donor['ID'])
            AMT.append(int(donor['AMT']))
    data_for_zip = find_same(ID)
    data_by_zip = calculate_by_type(data_for_zip, ZIP, AMT)
    # Calculation by date
    DT = []
    ID = []
    AMT = []
    for donor in data:
        flg = validate_date(donor['DT'])
        if flg == 0:
            DT.append(donor['DT'])
            ID.append(donor['ID'])
            AMT.append(int(donor['AMT']))
    data_for_date = find_same(ID)
    data_by_date = calculate_by_type(data_for_date, DT, AMT)
    # Output to text file
    with open(file_output_path_zip,'w') as file_object_1:
        for temp_1 in data_by_zip:
            file_object_1.write(temp_1['ID']+'|'+temp_1['TYPE'][0:5]+'|'+ str(temp_1['MEDIUM'])+'|'+ str(temp_1['COUNT'])+'|'+ str(temp_1['TOTAL'])+'\n')
    with open(file_output_path_date,'w') as file_object_2:
        for temp_2 in data_by_date:
            file_object_2.write(temp_2['ID']+'|'+temp_2['TYPE']+'|'+ str(temp_2['MEDIUM'])+'|'+ str(temp_2['COUNT'])+'|'+ str(temp_2['TOTAL'])+'\n')


if __name__ == '__main__':
    main()
