import csv

# Open CSV file and load columns into dictionary
with open('ChilliwackTerrainCodes.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    terrain_dict = {row['fid']: row['terrain'] for row in reader}

# Parse 'terrain' values and add to dictionary
for key, value in terrain_dict.items():
    parsed_values = []
    temp_value = value
    while True:
        index = min(temp_value.find('/'), temp_value.find('='), len(temp_value))
        parsed_values.append(temp_value[:index].strip())
        if index == len(temp_value):
            break
        temp_value = temp_value[index+1:]
    terrain_dict[key] = {'terrain': value, 'parsed_values': parsed_values}

# Print updated dictionary
for key, value in terrain_dict.items():
    print(f"{key}: {value}")