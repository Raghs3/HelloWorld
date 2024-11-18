# import csv
#
# countries = {}
# missing_fields_country = {}
#
# countries_filename = 'country_info.txt'
#
# with open(countries_filename, encoding='utf-8', newline='') as countries_file:
#     # sample = ""
#     # for i in range(3):
#     #     sample += countries_file.readline()
#
#     # country_dialect = csv.Sniffer().sniff(sample)
#     # countries_file.seek(0)
#
#     reader = csv.DictReader(countries_file, delimiter='|') # dialect=country_dialect)
#
#     for row in reader:
#         countries[row['Country'].casefold()] = row
#         countries[row['CC'].casefold()] = row
#         countries[row['CC3'].casefold()] = row
#
#         missing_fields = []
#         for key, value in row.items():
#             if len(value) == 0:
#                 missing_fields.append(key)
#
#         if missing_fields:
#             missing_fields_country[row['Country'].casefold()] = missing_fields
#             missing_fields_country[row['CC'].casefold()] = missing_fields
#             missing_fields_country[row['CC3'].casefold()] = missing_fields
# # print(countries)
#
# while True:
#     chosen_country = input('Please enter the name of a country: ')
#     country_key = chosen_country.casefold()
#
#     if chosen_country == 'quit':
#         break
#     elif country_key in missing_fields_country:
#         print(f'{missing_fields_country[country_key]} is missing for {chosen_country}')
#     elif country_key in countries:
#         print(f"The capital of {chosen_country} is {countries[country_key]['Capital']}")
#     else:
#         print('Country not found.')


# tim's soln

# import csv
#
# input_filename = 'country_info.txt'
#
# countries = {}
# with open(input_filename, encoding='utf-8', newline='') as country_file:
#     dict_reader = csv.DictReader(country_file, delimiter='|')
#     for row in dict_reader:
#         # print(row)
#         # countries[country.casefold()] = country_dict
#         countries[row['Country'].casefold()] = row
#         # countries[code.casefold()] = country_dict
#         countries[row['CC'].casefold()] = row
#
# print(countries)
#
# while True:
#     chosen_country = input('Please enter the name of a country: ')
#     country_key = chosen_country.casefold()
#     if country_key in countries:
#         country_data = countries[country_key]
#         print(f"The capital of {chosen_country} is {country_data['Capital']}")
#     elif chosen_country == 'quit':
#         break


# how to make dialect and how to pass keys in DictReader

import csv

input_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'  # not recommended if you want to use dialect in more than one program
# custom_dialect = csv.Dialect(delimiter='|')  # unexpected argument error, doesn't work

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    # dict_reader = csv.DictReader(country_file, delimiter='|')
    # Get the column headings from the first line of the file
    headings = country_file.readline().strip("\n").split(dialect.delimiter)  # only need to change one line to change delimiter hence used variable instead of hardcoding `|`
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()

    dict_reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)  # using dialect so dont need to change delimiter in 2 places, all changes are in a single place
    for row in dict_reader:
        # print(row)
        # countries[country.casefold()] = country_dict
        # countries[row['Country'].casefold()] = row
        countries[row['country'].casefold()] = row  # we converted headings to lowercase when making headings list
        # countries[code.casefold()] = country_dict
        # countries[row['CC'].casefold()] = row
        countries[row['cc'].casefold()] = row

# print(countries)

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['Capital']}")
    elif chosen_country.casefold() == 'quit':
        break
