import csv

# Open the CSV file and load its contents into a dictionary
with open('ChilliwackTerrainCodes.csv') as file:
    reader = csv.DictReader(file)
    terrain_dict = {}
    for row in reader:
        terrain_dict[row['fid']] = row['terrain']

# Go through the values of the dictionary and modify the values
for key, value in terrain_dict.items():
    new_value = ""
    for i, char in enumerate(value):
        if i > 0:
            prev_char = value[i - 1]
            if char.isupper() and prev_char.islower():
                new_value += " "
            elif char.isupper() and prev_char == "$":
                new_value += " "
            elif char.islower() and prev_char.isupper():
                new_value += " "
            elif char == "/" or prev_char == "/":
                new_value += " "
            elif char == "-":
                new_value += " "
            elif char == "=" or prev_char == "=":
                new_value += " "
        new_value += char
    terrain_dict[key] = new_value


# Print the modified dictionary
print(terrain_dict)

for key, value in terrain_dict.items():
    words = value.split()
    if words[0][0].isupper():
        surficial_material_code = words[0][0]
        if surficial_material_code in surficial_material_terms:
            value += ' ' + surficial_material_terms[surficial_material_code]
        for char in words[0][1:]:
            if char in surface_expression_terms:
                value += ' ' + surface_expression_terms[char]
    else:
        for char in words[0]:
            if char in textural_terms:
                value += ' ' + textural_terms[char]
    terrain_dict[key] = value