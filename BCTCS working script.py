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
#from BCTCSparse import BCTCSparse
import BCTCS


try:
    terrain_code = []

    with open('ChilliwackTerrainCodes.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            terrain_code.append(row[1])

    # hardcode a string to parse as the last entry
    terrain_code.append('spRks//zCb-Fe')
    terrain_code.append('oNTA')
    terrain_code.append('NT-FqYAY')
    terrain_code.append('wowGIBBErish/112rz-APEz$!@')



    returned_list = []

    for i in range(1, len(terrain_code)):
        print(terrain_code[i])
        returned_list.append(BCTCS.Terrain(terrain_code[i],0).parsed)
        #returned_list[i-1].append(terrain_code[i])
        print('Output List for input string = ', terrain_code[i], '\n', returned_list[i-1])
    #BCTCS()
    
    #returned_list = []
    #returned_list = BCTCSparse(terrain_code[1])
    print(returned_list[0], terrain_code[1])
    """ 
    # print last entry of returned list for debugging purposes
    N = 2 #len(returned_list[-1])
    L = len(returned_list)
    for i in range(N):
        for j in range(7):
            print(returned_list[L-1][i][j]) """
    #print('Type of terrain_code:', type(terrain_code))
except ValueError as e:
    print('Exception Raised from unparsed terms from input: ', e)

print(BCTCS.Terrain(''))
print(BCTCS.Terrain('').parsed)
print(BCTCS.Terrain('zFG').parsed)
            
#`help(BCTCS)