import csv
import re

txt_file = r"DoorTxt.txt"
csv_file = r"ConvertedCsv.csv"


test_str = ""

with open(txt_file, 'r', newline='\n') as in_txt:
    test_str = in_txt.read().strip()


    test_str = re.sub(',', '.', test_str)
    test_str = re.sub(' +', ',', test_str)
    test_str = re.sub('\r', '', test_str)

    # test_str = re.sub('FullplusEvidence\r', 'FullplusEvidence', test_str)
    # test_str = re.sub('MaintenanceDept\r', 'MaintenanceDept', test_str)
    # test_str = re.sub('CH\r', 'Spare-CH', test_str)
    # test_str = re.sub('Full\r', 'Spare-CH', test_str)

    test_str = test_str.splitlines()

    reader = csv.reader(test_str, delimiter = ",")
    out_csv = csv.writer(open(csv_file, 'w', newline=''), quoting=csv.QUOTE_NONE)
    for row in reader:
        out_csv.writerows(reader)