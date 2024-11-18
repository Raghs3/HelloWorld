input_filename = 'country_info.txt'

countries = {}
missing_fields_country = {}

with open(input_filename, encoding='utf-8') as country_file:
    country_file.readline()  # skip header, iterator moves onto next line
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict
        countries[code3.casefold()] = country_dict
      
        missing_fields = []
        for key, value in country_dict.items():
            if len(value) == 0:
                missing_fields.append(key)

        if missing_fields:
            missing_fields_country[country.casefold()] = missing_fields


# print(countries)

# my method
# user_country = input('Enter country name: ')
#
# try:
#     capital_city = countries[user_country.casefold()]['capital']
# except:
#     print('Country not found.')
# else:
#     print(f'The capital city of {user_country} is {capital_city}.')

# Tim's method
# while True:
#
#     chosen_country = input('Please enter the name of a country: ').casefold()
#     if chosen_country in countries:
#         country_data = countries[chosen_country]
#         print(f"The capital of {chosen_country} is {country_data['capital']}")
#     elif chosen_country == 'quit':
#         break

# my tim's improved method
while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if chosen_country == 'quit':
        break
    elif country_key in missing_fields_country:
        print(f'{missing_fields_country[country_key]} is missing for {chosen_country}')
    elif country_key in countries:
        print(f"The capital of {chosen_country} is {countries[country_key]['capital']}")
    else:
        print('Country not found.')
#
# list_countries = list(countries)
#
# missing_fields_country = {}
#
# for country in list_countries[::3]:
#     missing_fields = []
#     for key, value in countries[country].items():
#         if len(value) == 0:
#             print(f'{key} is missing for {country}')
#             missing_fields.append(key)
#             missing_fields_country[country] = missing_fields
#
print(missing_fields_country)
