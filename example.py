'''
Example of using BCTS in a script
'''

import csv
import bctcs

with open('ChilliwackTerrainCodes.csv', 'r',
          encoding='UTF-8', newline='') as cod:
    reader = csv.DictReader(cod)
    data = []
    for row in reader:
        parsedata = dict(fid = row['fid'],
                        tcode = row['terrain'],
                         terrain = bctcs.Terrain(row['terrain']))
        data.append(parsedata)

# Filter for 3+ multiple types only, get string plus ignore moraines
multi = [(x['fid'], x['tcode'], str(x['terrain'])) for x in data if len(x['terrain']) > 2 and 'Morain' not in str(x['terrain'])] 

print(multi)
