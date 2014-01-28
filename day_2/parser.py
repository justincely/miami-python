"""
Usage:

    python parser.py <filename>

example:

    python parser.py 2012_12_15.txt
"""

import sys

def filereader(filename):
    """
    This a filereader
    Arguments:
    filename: Name of the file that we are reading
    fieldname: Column name that we are making unique

    Returns a unique set of value specified by fieldname
    """
    uniques = set()
    for line_no, line in enumerate(open(filename)):
        if line_no == 0:
            # Skip the header
            continue
        line_data = line.split()
        city, state, shape = parse_record(line_no, line_data)
        uniques.add(city)
    return uniques

def parse_record(line_no, data):
    record = {}
    record['line_no'] = line_no
    record['date'] = data[0]
    record['time'] = data[1]
    record['city'] = data[2]
    record['state'] = data[3] 
    record['shape'] = data[4]
    return record['city'], record['state'], record['shape']

print filereader(sys.argv[1])
