input_filename = 'country_info.txt'

countries = {}
# code_lookup = {}
empty_data = {}

with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        # print(data)
        country, capital, code, cc3, dialing, timezone, currency = data
        # print(country, capital, code, cc3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'code': code,
            'cc3': cc3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        # code_lookup[code.casefold()] = country
        # countries[code.casefold()] = country_dict

# for country, data in countries.items():
#     print(country, data, sep=" ---> ")

for country, data in countries.items():
    empty_fields = []
    for param_key, param in data.items():
        if not param:
            ID = id(empty_fields)
            empty_fields.append(param_key)
            empty_data[country] = empty_fields

print(empty_data)
