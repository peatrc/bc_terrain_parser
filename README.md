# BC Terrain Classification System String Parser

The BC Terrain Classification System is a scheme designed for the classification of 
surficial materials, landforms and geomorphological processes of a mappable area.
The standards for this system are outlined in great detail in the [Terrain Classification System
for British Columbia v.2 (1997)](https://www2.gov.bc.ca/assets/gov/environment/natural-resource-stewardship/nr-laws-policy/risc/terclass_system_1997.pdf)

This script takes as input a single string of alphanumeric characters which represent
the characteristics of terrain encoded by the classification system, and returns english
language descriptions of the terrain.

With this module:

* Get the English-language description of a BCTCS code
* Get a list of properties of a BCTCS code (i.e., its surface material, surface expression,
texture, Geomorphological proccesses, extent)
* Get those same properties above, but in a dictionary format.
* If the code is composite (i.e., contains more than one terrain type delineated by '/') you 
can get the quantity of terrain types in the code, first type, last type, or specify the n-th type.



## Quick install

`pip install bctcs_terrain_parser` (not yet implemented)

## Documentation and API reference

User-friendly documentation of all methods and examples are available at <https://peatrc.github.io/bc_terrain_parser/>. 

## Source code

The primary repository for this software is at <https://github.com/peatrc/bc_terrain_parser>.
