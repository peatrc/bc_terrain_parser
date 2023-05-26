import csv

# Open and read the original CSV file
with open('ChilliwackTerrainCodes.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    # Load the columns into a dictionary
    terrain_dict = {}
    for row in reader:
        terrain_dict[row['fid']] = row['terrain']

# Initialize the parsed dictionary
terrain_dict_parsed = {}

# Go through each value in the 'terrain' column and parse it
for key, value in terrain_dict.items():
    parsed_values = []
    current_word = ''
    for i in range(len(value)):
        if value[i] == '/' or value[i] == '=' or value[i] == '-':
            if current_word != '':
                parsed_values.append(current_word)
            parsed_values.append(value[i])
            current_word = ''
        elif i == 0:
            current_word = value[i]
        elif value[i].islower() and value[i-1].isupper():
            if current_word != '':
                parsed_values.append(current_word)
            current_word = value[i]
        elif value[i].isupper() and value[i-1].islower():
            if current_word != '':
                parsed_values.append(current_word)
            current_word = value[i]
        elif value[i] == '$' and value[i+1].isupper():
            if current_word != '':
                parsed_values.append(current_word)
            current_word = value[i] + value[i+1]
        else:
            current_word += value[i]
    if current_word != '':
        parsed_values.append(current_word)

    # Add the parsed values to the parsed dictionary
    terrain_dict_parsed[key] = parsed_values

# Add the parsed values as new columns in the original dictionary
for key, value in terrain_dict_parsed.items():
    terrain_dict[key] = value

# Write the parsed dictionary to a new CSV file
with open('ChilliwackTerrainCodes_parsed.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['fid', 'terrain'] + list(terrain_dict_parsed.values())[0])
    for key, value in terrain_dict.items():
        row_values = [key, value]
        if key in terrain_dict_parsed:
            row_values += terrain_dict_parsed[key]
        else:
            row_values += [''] * len(list(terrain_dict_parsed.values())[0])
        writer.writerow(row_values)

# Print the parsed dictionary
print(terrain_dict_parsed)
