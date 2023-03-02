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

terrain_codes = []

with open("ChilliwackTerrainCodes.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        terrain_codes.append(row["terrain"])

print(terrain_codes)

# Dictionary for Textural Terms
textural_terms = {
    'a': 'blocks',
    'b': 'boulders',
    'k': 'cobble',
    'p': 'pebbles',
    's': 'sand',
    'z': 'silt',
    'c': 'clay',
    'd': 'mixed Fragments',
    'g': 'gravel',
    'x': 'angular fragments',
    'r': 'rubble',
    'm': 'mud',
    'y': 'shells',
    'e': 'fibric',
    'u': 'mesic',
    'h': 'humic',
}

# Dictionary for Surficial Material Terms //**** Must work on Active/Inactive Qualifiers
surficial_material_terms = {
    'A': 'anthropogenic(A)',
    'C': 'colluvium(A)',
    'D': 'weathered bedrock (in situ)(A)',
    'E': 'eolian(I)',
    'F': 'fluvial(I)',
    'FG': 'glaciofluvial(I)',
    'I': 'ice(A)',
    'L': 'lacustrine(I)',
    'LG': 'glaciolacustrine(I)',
    'M': 'morainal(I)',
    'N': 'not mapped(-)',
    'O': 'organic(A)',
    'R': 'bedrock(-)',
    'U': 'undifferentiated(-)',
    'V': 'volcanic(I)',
    'W': 'marine(I)',
    'WG': 'glaciomarine(I)',
}

# Dictionary for Surface Expression Terms
surface_expression_terms = {
    'a': 'moderate slope',
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
    'A': 'snow avalanches(A)',
    'B': 'braiding channel(A)',
    'C': 'cryoturbation(A)',
    'D': 'deflation(A)',
    'E': 'channeled by meltwater(I)',
    'F': 'slow mass movements(A)',
    'H': 'kettled(I)',
    'I': 'irregularly sinuous channel(A)',
    'J': 'anastomising channel(A)',
    'K': 'karst(A)',
    'L': 'abundant surface seepage(A)',
    'M': 'meandering channel(A)',
    'N': 'nivation(A)',
    'P': 'piping(A)',
    'R': 'rapid mass movements(A)',
    'S': 'solifluction(A)',
    'U': 'inundation(A)',
    'V': 'gully erosion(A)',
    'W': 'washing(A)',
    'X': 'permafrost process(A)',
    'Z': 'general periglacial process(A)',
}

# Dictionary for Subclass of (-F)Geomorphological Process Slow Mass Movement Terms
slow_mass_movement_F_subclass_terms = {
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
    'd': 'ephemeral tributary-fed backchannels',
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
    'bx': 'clastic, breccia',
    'pk': 'precipitates, crystalline, calcareous',
    'pu': 'precipitates, crystalline, non-calcareous',
    'tv': 'precipitates, crystalline, travertine',
    'ls': 'precipitates, crystalline, limestone',
    'do': 'precipitates, crystalline, dolomite',
    'gy': 'precipitates, crystalline, gypsum',
    'li': 'precipitates, crystalline, limonite',
    'ba': 'precipitates, crystalline, barite',
    'ok': 'organic, calcareous',
    'oc': 'organic, carbonaceous',
    'ma': 'organic, cacareous, marl',
    'lg': 'organic, carbonaceous, lignite',
    'co': 'organic, carbonaceous, coal',
    'ia': 'intrusive, acid(felsic)',
    'ii': 'intrusive, intermediate',
    'ib': 'intrusive, basic(mafic)',
    'sy': 'intrusive, syenite',    
    'gr': 'intrusive, granite',
    'qm': 'intrusive, quartz monzonite',
    'gd': 'intrusive, granodiorite',
    'qd': 'intrusive, quartz diorite',
    'di': 'intrusive, diorite',
    'qg': 'intrusive, quartz gabbro',
    'gb': 'intrusive, gabbro',
    'py': 'intrusive, pyroxenite',
    'pd': 'intrusive, peridotite',
    'du': 'intrusive, dunite',
    'ea': 'extrusive, acid(felsic)',
    'ei': 'extrusive, intermediate',
    'eb': 'extrusive, basic(mafic)',
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

#---------------------------------------------------------
# PARSING THE FIRST 3 CHARACTERS FOR THE TERRAIN CODE 
#---------------------------------------------------------
#Loop through the terrain_codes array (pulled from the csv file above)
for i, code in enumerate(terrain_codes):
    # Remove all symbols "=" or "/" and all characters that come after those symbols
    code = code.split("=")[0].split("/")[0]
    # Parse the string into 4 parts
    parts = []
    for part in code.split("-"):
        first_group = ""
        second_group = ""
        for char in part:
            if char.islower():
                first_group += char
            elif char.isupper():
                if first_group == "":
                    first_group = part[:part.index(char)]
                second_group += char
        parts.append((first_group, second_group))
    # Check the first group of lower case letters and print the terrain code if any of the characters match
    matches = ""
    for char in parts[0][0][:3]:
        if char in "abkpszcdgrmyeu":
            matches += char
    if matches:
        print(f"{i}: {'-'.join([p[0]+p[1] for p in parts])}", end=" ")
        for match in matches:
            print(textural_terms[match], end=" ")
        print()
