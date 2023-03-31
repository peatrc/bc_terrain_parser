### String Parser for BCGS Terrain Classification System
#   Peter Carvalho peatrc@gmail.com
#
# 4 Main Symbol Categories:
#
# 1) Texture: (one to three lower case letters) describes the size, roundness and 
# sorting of particles in mineral sediments and the fiber content of organic materials.
#
# 2) Surficial Material: (One upper case letter) classified according to mode of deposition
#
# 3) Surface Expression: (1-3 lower case letters) descrbing form/shape of land surface or
# thickness of materials.
#
# 4) Geomorphological Processes (1-3 upper case letters) describes geomorphological 
# processes that are modifying either surficial materials or landforms
# 
# ^Qualifiers (1-2 superscript uppercase letters) used where appropriate to provide
# information about surficial materials and geomorphological processes. Supercript
# may be inline instead on computer drafted maps.
#
# Some Terms have associated subclass terms, all of which have their own dictionary (for now?):
# (-?)Qualified Term: [dictionary_name]
# (-F)Geomorphological Process Slow Mass Movement Terms: [slow_mass_movement_F_subclass_terms]
# (-R)Geomorphological Process Rapid Mass Movement Terms: [rapid_mass_movement_R_subclass_terms]
# (-A)Geomorphological Process Avalanche Terms: [snow_avalanches_A_subclass_terms]
# (-B,-I,-J,-M) Fluvial Processes Terms: [fluvial_B_I_J_M_subclass_terms]
# (-X,-Z) Permafrost Processes Terms: [permafrost_X_Z_subclass_terms]
# (R) Bedrock Terms: bedrock_R_subclass_terms
#
# -----
# Basic Idea of Terrain Syntax for a given string:
# textureSURFICIAL_MATERIALsurface_expressionGEOMORPHOLOGICAL_PROCESSES
# texSsexMOR
# Using dictionary names:
# [textural_terms] [surficial_material_terms] [surface_expression_terms] [geomorphological_process_terms]
# -----
# E.g.: sgF^Gt-F^I
# glaciofluvial (F^g) terrace (t) composed of sandy gravel (sg) modified by slow 
# downslope failures (F) that are no longer active (^I)

import csv

# terrain_codes = []

# with open("ChilliwackTerrainCodes.csv") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         terrain_codes.append(row["terrain"])

# print(terrain_codes)

# Dictionary for Textural Terms
textural_terms = {
    'a': 'Blocks',
    'b': 'Boulders',
    'k': 'Cobbles',
    'p': 'Pebbles',
    's': 'Sand',
    'z': 'Silt',
    'c': 'Clay',
    'd': 'Mixed Fragments',
    'g': 'Gravel',
    'r': 'Rubble',
    'm': 'Mud',
    'y': 'Shells',
    'e': 'Fibric',
    'u': 'Mesic',
    'h': 'Humic',
    '$': 'Silt',
}

# Dictionary for Surficial Material Terms //**** Must work on Active/Inactive Qualifiers
surficial_material_terms = {
    'A': 'Anthropogenic Material',
    'C': 'Colluvium',
    'D': 'Weathered Bedrock (in situ)',
    'E': 'Eolian Material',
    'F': 'Fluvial Material',
    'FG': 'Glaciofluvial Material',
    'I': 'Ice',
    'L': 'Lacustrine Material',
    'LG': 'Glaciolacustrine Material',
    'M': 'Morainal Material(Till)',
    'O': 'Organic Material',
    'R': 'Bedrock',
    'U': 'Undifferentiated Materials',
    'V': 'Volcanic Material',
    'W': 'Marine Material',
    'WG': 'Glaciomarine Material',
}

# Dictionary for Surface Expression Terms
surface_expression_terms = {
    'a': 'Moderate slope',
    'b': 'blanket',
    'c': 'cone(s)',
    'd': 'depression(s)',
    'f': 'fan(s)',
    'h': 'hummock(s)',
    'j': 'gentle slope',
    'k': 'moderately steep slope',
    'm': 'rolling',
    'p': 'plain',
    'r': 'ridge(s)',
    's': 'steep slope',
    't': 'terrace(s)',
    'u': 'undulating',
    'v': 'veneer',
    'w': 'mantle of variable thickness',
    'x': 'thin veneer'
}

# Dictionary for Geomorphological Process Terms
geomorphological_process_terms = {
    'D': 'Deflation',
    'K': 'Karst processes',
    'P': 'Piping',
    'V': 'Gully erosion',
    'W': 'Washing',
    'B': 'Braiding channel',
    'I': 'Irregularly sinuous channel',
    'J': 'Anastomising channel',
    'M': 'Meandering channel',
    'A': 'Snow avalanches',
    'F': 'Slow mass movements',
    'R': 'Rapid mass movements',
    'C': 'Cryoturbation',
    'N': 'Nivation',
    'S': 'Solifluction',
    'Z': 'General periglacial process',
    'X': 'Permafrost process',
    'E': 'Channeled by meltwater',
    'H': 'Kettled',
    'U': 'Inundation',
    'L': 'Surface seepage',
}

# Dictionary for Subclass of (-F)Geomorphological Process Slow Mass Movement Terms
slow_mass_movement_F_subclass_terms = {
    '"': 'initiation zone for mass movement',
    'c': 'soil creep',
    'g': 'rock creep',
    'k': 'tension cracks',
    'p': 'lateral spread in bedrock',
    'j': 'lateral spread in surficial material',
    'e': 'earthflow',
    'm': 'slump in earthflow',
    'u': 'slump in surficial material',
    'x': 'slump-earthflow',
    's': 'debris slide',
    'r': 'rockslide',
}

# Dictionary for Subclass of (-R)Geomorphological Process Rapid Mass Movement Terms
rapid_mass_movement_R_subclass_terms = {
    '"': 'initiation zone for mass movement',
    'f': 'debris fall',
    'b': 'rockfall',
    'd': 'debris flow',
    't': 'debris torrent',
    'e': 'earthflow',
    'm': 'slump in earthflow',
    'u': 'slump in surficial material',
    'x': 'slump-earthflow',
    's': 'debris slide',
    'r': 'rockslide',
}

# Dictionary for Subclass of (-A)Geomorphological Process Avalanche Terms
snow_avalanches_A_subclass_terms = {
    '"': 'initiation zone for mass movement',
    'f': 'major avalanche tracks; active',
    'm': 'minor avalanche tracks; active',
    'w': 'mixed major and minor tracks; active',
    'o': 'old avalanche tracks',
}

# Dictionary for Subclass of (-B,-I,-J,-M) Fluvial Processes Terms
fluvial_B_I_J_M_subclass_terms = {
    'u': 'progressive bank erosion',
    'a': 'abrupt channel diversion; avulsion',
    'b': 'backchannels (undivided)',
    'p': 'permanent river-fed backchannels',
    'e': 'ephemeral river-fed backchannels',
    's': 'spring-fed backchannels',
    't': 'permanent tributary-fed backchannels',
    'r': 'ephemeral tributary-fed backchannels',
}

# Dictionary for Subclass of (-X,-Z) Permafrost Processes Terms
permafrost_X_Z_subclass_terms = {
    'p': 'palas, peat plateaus',
    't': 'thermokarst: subsidence',
    'e': 'thermokarst: thermal erosion by water',
    'f': 'thaw flow slides',
    'w': 'ice-wedge polygons',
    'r': 'patterned ground',
}

# Dictionary for Subclass of (R) Bedrock Terms
bedrock_R_subclass_terms = {
    'kf': 'clastic, calcareous fine grained',
    'km': 'clastic, calcareous medium grained',
    'kc': 'clastic, calcareous coarse grained',
    'kz': 'clastic, calcareous siltstone',
    'kd': 'clastic, calcareous mudstone',
    'kh': 'clastic, calcareous shale',
    'ks': 'clastic, calcareous sandstone',
    'kg': 'clastic, calcareous greywacke',
    'ka': 'clastic, calcareous arkose',
    'kn': 'clastic, calcareous conglomerate',
    'kb': 'clastic, calcareous breccia',
    'uf': 'clastic, non-calcareous fine grained',
    'um': 'clastic, non-calcareous medium grained',
    'uc': 'clastic, non-calcareous coarse grained',
    'zl': 'clastic, siltstone',
    'md': 'clastic, mudstone',
    'sh': 'clastic, shale',
    'ss': 'clastic, sandstone',
    'gk': 'clastic, greywacke',
    'ak': 'clastic, arkose',
    'cg': 'clastic, conglomerate',
    'bk': 'clastic, breccia',
    'pk': 'precipitates, calcareous',
    'pu': 'precipitates, non-calcareous',
    'tv': 'precipitates, travertine',
    'ls': 'precipitates, limestone',
    'do': 'precipitates, dolomite',
    'gy': 'precipitates, gypsum',
    'li': 'precipitates, limonite',
    'ba': 'precipitates, barite',
    'ia': 'intrusive, acid(felsic)',
    'ii': 'intrusive, intermediate',
    'ib': 'intrusive, basic',
    'sy': 'intrusive, syenite',    
    'gr': 'intrusive, granite',
    'qm': 'intrusive, quartz monzonite',
    'gd': 'intrusive, grandodiorite',
    'qd': 'intrusive, quartz diorite',
    'di': 'intrusive, diorite',
    'qg': 'intrusive, quartz gabbro',
    'gb': 'intrusive, gabbro',
    'py': 'intrusive, pyroxenite',
    'pd': 'intrusive, peridotite',
    'du': 'intrusive, dunite',
    'ea': 'extrusive, acid(felsic)',
    'ei': 'extrusive, intermediate',
    'eb': 'extrusive, basic',
    'la': 'extrusive, recent lava flow',
    'ep': 'extrusive, pyroclastic',
    'tr': 'extrusive, trachyte',
    'rh': 'extrusive, rhyolite',
    'da': 'extrusive, dacite',
    'an': 'extrusive, andesite',
    'qb': 'extrusive, quartz basalt',
    'bs': 'extrusive, basalt',
    'tu': 'extrusive, tuff',
    'vb': 'extrusive, volcanic breccia',
    'ag': 'extrusive, agglomerate',
    'ff': 'foliated, fine grained',
    'fm': 'foliated, medium to coarse grained',
    'fc': 'foliated, coarse grained',
    'sl': 'foliated, slate',
    'ph': 'foliated, phyllite',
    'sc': 'foliated, schist',
    'gn': 'foliated, gneiss',
    'gg': 'foliated, granite gneiss',
    'dg': 'foliated, diorite gneiss',
    'mi': 'foliated, migmatite',
    'nf': 'non-foliated, fine grained',
    'nm': 'non-foliated, medium to coarse grained',
    'nc': 'non-foliated, coarse grained',
    'nk': 'non-foliated, calcareous',
    'ar': 'non-foliated, argillite',
    'sp': 'non-foliated, serpentinite',
    'gl': 'non-foliated, granulite',
    'qt': 'non-foliated, quartzite',
    'hf': 'non-foliated, hornfels',
    'am': 'non-foliated, amphibolite',
    'hb': 'non-foliated, hornblendite',
    'mb': 'non-foliated, marble',
    'dm': 'non-foliated, dolomite marble',
    'sm': 'non-foliated, serpentine marble',
}

# #---------------------------------------------------------
# # PARSING THE FIRST 3 CHARACTERS FOR THE TERRAIN CODE 
# #---------------------------------------------------------
# #Loop through the terrain_codes array (pulled from the csv file above)
# for i, code in enumerate(terrain_codes):
#     # Remove all symbols "=" or "/" and all characters that come after those symbols
#     code = code.split("=")[0].split("/")[0]
#     # Parse the string into 4 parts
#     parts = []
#     for part in code.split("-"):
#         first_group = ""
#         second_group = ""
#         for char in part:
#             if char.islower():
#                 first_group += char
#             elif char.isupper():
#                 if first_group == "":
#                     first_group = part[:part.index(char)]
#                 second_group += char
#         parts.append((first_group, second_group))
#     # Check the first group of lower case letters and print the terrain code if any of the characters match
#     matches = ""
#     for char in parts[0][0][:3]:
#         if char in "abkpszcdgrmyeu":
#             matches += char
#     if matches:
#         print(f"{i}: {'-'.join([p[0]+p[1] for p in parts])}", end=" ")
#         for match in matches:
#             print(textural_terms[match], end=" ")
#         print()

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

""" # Open the CSV file and load its contents into a dictionary
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

for key, value in terrain_dict.items():
    words = value.split()  # split the value string into words
    for word in words:
        if word.isupper():  # find the first word with uppercase letters
            if word in surficial_material_terms:  # find the associated value in the "surficial_materal_terms" dictionary
                terrain_dict[key] += " " + surficial_material_terms[word] + " "  # append the value to the string
            break  # break out of the loop once the first uppercase word is found

# Print the modified dictionary
print(terrain_dict)

for key, value in terrain_dict.items():
    # Find the first word with uppercase letters
    words = value.split()
    for word in words:
        if any(c.isupper() for c in word):
            break
    
    # Look at the word immediately after it and copy it into "check_this_word"
    check_this_word = ""
    if words.index(word) < len(words)-1:
        check_this_word = words[words.index(word)+1]
    
    # Find the associated values in the "surface_expression_terms" dictionary and append them
    for c in check_this_word:
        if c in surface_expression_terms:
            value += surface_expression_terms[c]
    
    # Update the value in the terrain_dict
    terrain_dict[key] = " " + value

# loop through each key-value pair in terrain_dict
for key, value in terrain_dict.items():
    # split the value string into a list of words
    words = value.split()
    if len(words) > 0 and words[0][0].islower():
        # the first word starts with a lowercase character
        textural_terms_list = []
        # loop through each character in the first word
        for char in words[0]:
            # find the associated value in the textural_terms dictionary
            if char in textural_terms:
                textural_terms_list.append(textural_terms[char])
        # join the list of textural terms into a single string and append it to the value
        terrain_dict[key] = value + ' ' + ' '.join(textural_terms_list)

print(terrain_dict)
 """

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

    # Go through each value in the parsed dictionary and merge any values of '-'
for key, value in terrain_dict_parsed.items():
    new_values = []
    merge_value = ''
    for v in value:
        if v == '-':
            merge_value += v
        elif merge_value != '':
            new_values.append(merge_value + v)
            merge_value = ''
        else:
            new_values.append(v)
        if '/' in v:
            merge_value = ''
    terrain_dict_parsed[key] = new_values
# Print the parsed dictionary
print(terrain_dict_parsed)

# Define the new dictionary
#terrain_dict_updated = {}

# Go through each value in the 'terrain' column
for key, value in terrain_dict_parsed.items():
    # Check if the first value starts with '/'
    if value[0] == '/':
        # Replace the '/' with the new value
        value[0] = '**' # ** indicicates "moderately extensive but discontinuous" to be changed after
    # Update the dictionary with the modified values
    terrain_dict_parsed[key] = value

# Print the updated dictionary
print(terrain_dict_parsed)

#adding * if no texture code exists
for key, value in terrain_dict_parsed.items():
    new_values = []
    lowercase_found = False
    for i, v in enumerate(value):
        if v.isupper() and not lowercase_found:
            new_values.append('*')
        if v.islower():
            lowercase_found = True
        new_values.append(v)
    terrain_dict_parsed[key] = new_values

# Print the updated dictionary
print(terrain_dict_parsed)

# add a * if no surface expression exists
for fid, values in terrain_dict_parsed.items():
    found_uppercase = False
    for i, value in enumerate(values):
        if any(c.isupper() for c in value):
            found_uppercase = True
            if i + 1 >= len(values) or not values[i + 1][0].islower():
                values.insert(i + 1, '*')
            break
    if not found_uppercase:
        values.insert(0, '*')
        
print(terrain_dict_parsed)
# add a * is no geomorph process
for fid in terrain_dict_parsed:
    values = terrain_dict_parsed[fid]
    index_uppercase = -1
    for i, value in enumerate(values):
        if value[0].isupper():
            index_uppercase = i
            break
    if index_uppercase == -1:
        continue
    if index_uppercase < len(values) - 1 and not values[index_uppercase + 1].startswith('-'):
        values.insert(index_uppercase + 2, '*')
print(terrain_dict_parsed)

for fid in terrain_dict_parsed:
    surf_material = surficial_material_terms.get(terrain_dict_parsed[fid][1], 'Unknown')
    print(f"Fid: {fid}, Surficial Material: {surf_material}")

#temp printing for show
print(terrain_dict_parsed)   
#count how many discrete units exist in the terrain code
counts = {}
for fid, values in terrain_dict_parsed.items():
    count = 0
    for i in range(1, len(values)):
        if values[i] == '/' or values[i] == '=':
            count += 1
    counts[fid] = count

max_count = max(counts.values())
print(max_count)


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
#print(terrain_dict_parsed)



