# String parser for the BC Terrain Classification System (1997 version)
#
# The BC Terrain Classification System is a scheme designed for the classification of 
# surficial materials, landforms and geomorphological processes of a mappable area.
#
# This script takes as input a single string of alphanumeric characters which represent
# the characteristics of terrain encoded by the classification system and returns a list
# (or lists) containging plain english language descriptions of the terrain.
#
# If the terrain code contains only one terrain type it will return a single list with
# seven plain-english descriptors
#
# INPUT:
# ======
# A single string representing the code describing terrain features codified by the BC 
# Terrain Classification System, Version 2, 1997. 
#
# OUTPUTS:
# =======
# ['Surficial Material', 'Surface Expression', 'Texture', 'Geomorphological Proccess(es)', 
#   'Extent', 'Coverage Relative to next Terrain Type', 'Unparsed Terms'] 
# 
#
# OUTPUT DESCRIPTIONS:
# ====================
# 'Surficial Material': (One or Two upper case letters) classified according to mode of deposition
#
# 'Surface Expression': (1-3 lower case letters) descrbing form/shape of land surface or
# thickness of materials.
#
# 'Texture': (one to three lower case letters) describes the size, roundness and 
# sorting of particles in mineral sediments and the fiber content of organic materials.
#
# 'Geomorphological Processes': (1-3 upper case letters with lowercase subclass codes) describes geomorphological 
# processes that are modifying either surficial materials or landforms
#
# 'Extent': Describes whether the terrain is continuous of discontinuous over the unit.
#
# 'Coverage Relative to Next Terrain Term': If the terrain code describes more than one terrain type, this value
# describes whether this terrain's extent(coverage) is greater than, much greater than or equal to the following terrain
#
# 'Unparsed Terms': this returns a string descrbing any coded characters that were unable to be parsed because they were 
# not found in the associated BCTCS dictionaries.  This may due to incorrect input or order of coded characte rs
#
# If the terrain code does not specify any of the descriptors, the returned descriptor will
# simply be '' for that value.
#
# EXAMPLE 1: Typical Terrain Code
# ===============================
# Input = gFGs-F 
# Output = [['Glaciofluvial Material', 'steep slope', 'Gravel', 'Slow mass movements ', 'continuous', '', '']]
#
# EXAMPLE 2: Terrain Code Descrbing Multiple Terrain Types 
# ========================================================
# Input = Rhk/Cv 
# Output: [['Bedrock', 'hummock(s) moderately steep slope', '', '', 'continuous', 'greater extent', ''], ['Colluvium', 'veneer', '', '', 'continuous', '', '']]
#
# EXAMPLE 3: Attempted parsing for a string that has no associated values in the BCTCS System
# ===========================================================================================
# Input =  oNTA 
# [['', '', '', '', 'continuous', '', 'NTA: undefined surficial material code; o: undefined surface expression codes']]
#
# Author: Pete Carvalho Apr 25, 2023

import re

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

class Terrain:
    '''British Columbia Terrain Classification System (1997) parser
    '''
    def __init__(self, instr:str)->None:
        '''
        instr : str
            British Columbia Terrain System classification string
        '''
        self.instr = instr

    @property
    def parsed(self, terrain_code : str = None) -> list :
        '''
        Returns a list of lists. Each element contains seven sub elements representing
        ['Surficial Material', 'Surface Expression', 'Texture', 'Geomorphological Proccess(es)', 'Extent', 'Coverage Relative to next Terrain Type', 'Unparsed Terms'] 
        terrain_code : str
            BC Terrain Classification String
        '''
         #This is just the BCTCSParse function
        if not terrain_code:
            terrain_code = self.instr
        '''Returns a list of lists. Each list contains seven elements corresponding
        ['Surficial Material', 'Surface Expression', 'Texture', 'Geomorphological Proccess(es)', 'Extent', 'Coverage Relative to next Terrain Type', 'Unparsed Terms'] 
        
        terrain_code : str
            BC Terrain classification string
        '''

        # SPLIT THE CODE WHEN MULTIPLE TERRAIN TYPES ARE CONTAINED IN A CODE
        # This occurs when code contains '/' '//' or '=' chars (except for position 0 where '/' indicates discontinuity)
        
        try:
            #whether unparsed items will break the program (1) or run program and display unparsed items (0)
            strictmode=0
            # initialize an empty list called terrain_code_split
            terrain_code_split = []

            # initialize a variable called current_index and set its value to 0
            current_index = 0

            # loop through the indices of terrain_code
            for i in range(len(terrain_code)):
                # if the current character is "/" or "=" and not the first character of terrain_code
                if terrain_code[i] in ["/", "="] and i != 0:
                    #check for "double //" and perform that case, or single case if not double '//'
                    if i < len(terrain_code) - 1 and terrain_code[i+1] == '/':
                        terrain_code_split.append(terrain_code[current_index:i+2])
                        current_index = i + 2
                    else:
                        # split the string at the current index and append it to terrain_code_split
                        terrain_code_split.append(terrain_code[current_index:i+1])
                        # update current_index to be the index after the current split character
                        current_index = i + 1

            # if there are characters remaining in terrain_code, append them to terrain_code_split
            if current_index != len(terrain_code):
                terrain_code_split.append(terrain_code[current_index:])

            # strip any blank entries before moving on
            terrain_code_split = [item for item in terrain_code_split if item.strip()]
            
            # DEBUGGING print the resulting list
            print(terrain_code_split)

            ###END SPLITTING SECTION

            # PARSE/INTERPRET CODES IN THIS SECTION
            # Take each split code and make a list containing 6 descriptors describing the terrain
            # and a 7th descriptor that notes any code characters that are not defined in the BCTCS
        
            # create a new list for each item in the terrain_code_split list
            new_list = []
            for string in terrain_code_split:
                # initialize the values for the new list
                first_val = ""
                second_val = ""
                third_val = ""
                fourth_val = ""
                fifth_val = ""

                # *SURFICIAL MATERIAL*  check the first uppercase letter in the string
                first_val = ""

                # this conditional makes sure to include Bedrock modifier codes (if they exist)
                # this occurs when 'R' is preded by lowercase chars that exist in bedrock_R_subclass_terms dictionary
                if string.find("R") >= 2:
                    prev_two = string[string.find("R")-2:string.find("R")]
                    if prev_two in bedrock_R_subclass_terms.keys():
                        first_val += prev_two

                # get all characters before the first hyphen
                pre_hyphen = string.split('-')[0] if '-' in string else string

                # get the first uppercase letter or consecutive uppercase letters
                first_val = ''
                
                for i in range(len(pre_hyphen)):
                    if pre_hyphen[i].isupper():
                        first_val = pre_hyphen[i]
                        for j in range(i+1, len(pre_hyphen)):
                            if pre_hyphen[j].isupper():
                                first_val += pre_hyphen[j]
                            else:
                                break
                        break
            
                # *SURFACE EXPRESSION*  assign the second value
                upper_found = False
                second_val = ''
                for char in string:
                    if char.isupper():
                        upper_found = True
                    elif char.islower() and upper_found and '-' not in string[string.index(char)-1:string.index(char)]:
                        second_val += char
                    elif char == '-':
                        upper_found = False
                
                # *TEXTURE* assign the third value
                third_val = ""
                for char in string:
                    if char.isupper():
                        break
                    elif char.islower():
                        third_val += char
                
                # *GEOMORPHOLOGICAL PROCESS* assign the fourth value
                fourth_val = ""
                # strip the '-' that indicates the following chars codify geomorph processes
                if '-' in string:
                    i = string.index('-')
                    fourth_val = string[i:]
                    #remove / or = or numeric data
                    fourth_val = re.sub('[0-9/=-]', '', fourth_val)

                # *CONTINUITY* assign the fifth value
                fifth_val = ''
                if string[0] == '/':
                    fifth_val = "discontinuous"
                elif string[0] == '':
                    fifth_val = ''
                else:
                    fifth_val = "continuous"

                # *EXTENT RELATIVE TO NEXT TERRAIN TYPE* assign the sixth value (terrain extent relative to the following terrain)
                sixth_val = ''
                if string[-1] == "=":
                    sixth_val = "equal extent"
                elif string[-1] == "/":
                    if len(string) > 1 and string[-2] == "/":
                        sixth_val = "much greater extent"
                    else:
                        sixth_val = "greater extent"
                elif string[-1].isdigit():
                    sixth_val = string[-1]

                # add the values to the new list
                new_list.append([first_val, second_val, third_val, fourth_val, fifth_val, sixth_val, ''])
            
            # DEBUGGING PRINT UPDATES
                print(new_list)
            # print(new_list[0])
            # print(new_list[0][0][:2])

            # Loop over each list in new_list and replace coded characters with descriptive words in dictionaries
            
            for i in range(len(new_list)):
                
                # SURFICIAL MATERIAL CODE INTERPRETATION
                # Replace the first value with the associated value in the surficial_material_terms dictionary
                first_val = ''
                if len(new_list[i][0]) > 2 and new_list[i][0][:2] in bedrock_R_subclass_terms:
                    first_val += bedrock_R_subclass_terms[new_list[i][0][:2]] + ' '
            
                # Remove any non-uppercase letters from new_list[i][0]
                upper_case_letters = [char for char in new_list[i][0] if char.isupper()]

                # Count the number of uppercase letters
                num_upper_case_letters = len(upper_case_letters)

                if num_upper_case_letters == 1:
                    # Get the single uppercase letter
                    single_letter = upper_case_letters[0]

                    # Check if the surficial_material_terms dictionary has a value for that letter
                    if single_letter in surficial_material_terms:
                        # Add the associated value to new_first_val
                        first_val += surficial_material_terms[single_letter]
                    else:
                        # if the code is not found in dictionary, make note of this
                        new_list[i][6] += upper_case_letters + ': undefined surficial material code; '

                elif num_upper_case_letters == 2:
                    # Get the two uppercase letters
                    two_letters = ''.join(upper_case_letters)

                    # Check if the surficial_material_terms dictionary has a value for those two letters taken together
                    if two_letters in surficial_material_terms:
                        # Add the associated value to new_first_val
                        first_val += surficial_material_terms[two_letters]
                    else:
                        # if the code is not found in dictionary, make note of this
                        new_list[i][6] = new_list[i][6] + two_letters + ': undefined surficial material code; '
                elif num_upper_case_letters == 0:
                    new_list[i][6] = 'blank surficial material code; '
                elif num_upper_case_letters > 2:
                    new_list[i][6] = ''.join(upper_case_letters) + ': undefined surficial material code; '

                new_list[i][0] = first_val

                # if there is no terrain material identified, it cannot be continuous, so set blank
                if first_val == '':
                    new_list[i][4] = ''
                
                # SURFACE EXPRESSION CODE INTERPRETATION
                # first update str to remove any code items not in surface expression dictionary and made note
                code_not_found = []
                new_str = ""
                for c in new_list[i][1]:
                    if c not in surface_expression_terms:
                        code_not_found.append(c)
                    else:
                        new_str += c

                if len(code_not_found) > 0:
                    undefined_str = ' '.join([str(elem) for elem in code_not_found])
                    new_list[i][6] += undefined_str + ': undefined surface expression codes; '
                new_list[i][1] = new_str
                
                # Replace the second value with the associated value in the surface_expression_terms dictionary for each character
                new_list[i][1] = ' '.join([surface_expression_terms[c] if c in surface_expression_terms else c for c in new_list[i][1]])

                # TEXTURE CODE INTERPRETATION
                # first update str to remove any code items not in texture dictionary and made note
                code_not_found = []
                new_str = ""
                for c in new_list[i][2]:
                    if c not in textural_terms:
                        code_not_found.append(c)
                    else:
                        new_str += c

                if len(code_not_found) > 0:
                    undefined_str = ' '.join([str(elem) for elem in code_not_found])
                    new_list[i][6] += undefined_str + ': undefined surface expression codes; '
                new_list[i][2] = new_str
                
                # Replace the third value in each list with the associated value in the textural_terms dictionary for each character
                new_list[i][2] = ' '.join([textural_terms[c] if c in textural_terms else c for c in new_list[i][2]])

                # GEOMORPHOLOGICAL PROCESSES CODE INTERPRATATION
                # Replace 4th value w the associated value in the geomorphological_process_terms dictionary
                # Initialize new_geomorph to empty string
                new_geomorph = ''
                undefined_str = ''
                undefined_geomorph_process_terms = ''
                for char in new_list[i][3]:
                    if char.isupper() and char not in geomorphological_process_terms:
                        undefined_geomorph_process_terms += char + ' '  
                new_list[i][3] = ''.join([char for char in new_list[i][3] if char.upper() in geomorphological_process_terms])

                if undefined_geomorph_process_terms:
                    new_list[i][6] += undefined_geomorph_process_terms[:-1] + ': undefined geomorphological process terms; '

                # GEOMORPH SUBCLASS INTERPRETATIONS
                # Loop through each character in new_list[i][3]
                for char in new_list[i][3]:
                    # If character is uppercase, add the associated term from geomorphological_process_terms
                    if char.isupper():
                        new_geomorph += geomorphological_process_terms.get(char, char+'*') + ' '
                    # If character is lowercase and follows an 'F', add associated term from slow_mass_movement_F_subclass_terms
                    elif char.islower() and char.isalpha() and new_list[i][3][new_list[i][3].index(char)-1] == 'F':
                        new_geomorph += slow_mass_movement_F_subclass_terms.get(char, char+'*') + ' '
                        if slow_mass_movement_F_subclass_terms.get(char, 1) == 1:
                            new_list[i][6] += char + ': undefined geomorphological subclass modifier for F(slow mass movements)'                                # If character is lowercase and follows an 'R', add associated term from rapid_mass_movement_R_subclass_terms
                    elif char.islower() and char.isalpha() and new_list[i][3][new_list[i][3].index(char)-1] == 'R':
                        new_geomorph += rapid_mass_movement_R_subclass_terms.get(char, char+'*') + ' '
                    # If character is lowercase and follows an 'A', add associated term from snow_avalanches_A_subclass_terms
                    elif char.islower() and char.isalpha() and new_list[i][3][new_list[i][3].index(char)-1] == 'A':
                        new_geomorph += snow_avalanches_A_subclass_terms.get(char, char+'*') + ' '
                    # If character is lowercase and follows a 'B', 'I', 'J', or 'M', add associated term from fluvial_B_I_J_M_subclass_terms
                    elif char.islower() and char.isalpha() and new_list[i][3][new_list[i][3].index(char)-1] in ['B', 'I', 'J', 'M']:
                        new_geomorph += fluvial_B_I_J_M_subclass_terms.get(char, char+'*') + ' '
                    # If character is lowercase and follows a 'X' or 'Z', add associated term from permafrost_X_Z_subclass_terms
                    elif char.islower() and char.isalpha() and new_list[i][3][new_list[i][3].index(char)-1] in ['X', 'Z']:
                        new_geomorph += permafrost_X_Z_subclass_terms.get(char, char+'*') + ' '

                #update list with english geomorph terms     
                new_list[i][3] = new_geomorph

                # check the potential error string and remove the training two characters if there potential errors (string clean-up before returning)
                if new_list[i][6][-2:] == ', ' or new_list[i][6][-2:] == '; ':
                    new_list[i][6] = new_list[i][6][:-2]
            print(new_list)
            
            #return as normal if there is no record of unparsed terms in new_list[i][6]
            if new_list[i][6] == '':
                return(new_list)
            else: # goes here if there were unparsed items, treated differently whether it is in strict mode or not
                raise ValueError(new_list[i][6])

        except ValueError as e:
            print('Exception Raised from unparsed terms from input: ', e)
            if strictmode == 0:
                return(new_list)


    def __len__(self):
        return len(self.parsed)
    
    def __getitem__(self, key):
        return(self.parsed[key])
    
    def __str__(self):
        return ' / '.join([' '.join([y for y in x if y]) for x in self.parsed])

    def __int__(self):
        return(len(self.parsed))
    
    def max(self):
        return self.parsed[0]
    
    def min(self):
        return self.parsed[-1]

    def json(self):
        outjson = {self.instr :[]}
        for group in self.parsed:
            groupdict = dict(type = group[0],
                             something_else =group[1] if group[1] else None,
                             and_furthermore = group[2] if group[2] else None,
                             etc = group[3] if group[3] else None,
                             also = group[4] if group[4] else None,
                             lastly = group[5] if group[5] else None)
            outjson[self.instr].append(groupdict)
        return outjson                    
    
if __name__ == '__main__':

    # create a variable called terrain_code and set its value to "/Msa=Mw-V/Rsa"
    #terrain_code = "/Msa=Mw-V/Rsa"
    #print(len(terrain_code))
    #print(terrain_code)
    #returned_list = BCTCSparse(terrain_code)
    #print(returned_list)
    terrain = Terrain('/Msa=Mw-V/Rsa')
    print(terrain.instr)
    print(terrain.parsed)
    print(len(terrain))
    print(terrain[1])
    print(str(terrain))
    print(terrain.min())
    print(terrain.max())
    print(terrain.json())
    print(int(terrain))
