import csv

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    # sample = countries_data.read()  # not efficient, sniffer only needs few lines
    sample = ""
    for line in range(3):
        sample += countries_data.readline()
    # print(sample)
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True  # removes leading spaces
    countries_data.seek(0)
    # country_reader = csv.reader(countries_data, delimiter='|')
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print('*' * 80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]

for attribute in attributes:
    # print(f'{attribute}: {getattr(country_dialect, attribute)}')
    print(f'{attribute}: {repr(getattr(country_dialect, attribute))}')
