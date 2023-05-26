# BC Terrain Classification System string parser (for the 1997 BCTCS System)

The BC Terrain Classification System is a scheme designed for the classification of 
surficial materials, landforms and geomorphological processes of a mappable area.

This script takes as input a single string of alphanumeric characters which represent
the characteristics of terrain encoded by the classification system and returns a list
(or lists) containging plain english language descriptions of the terrain.

With these utilities you can:

* Get the English-language description of a BCTCS code
* Get a list of properties of a BCTCS code (i.e., its surface material, surface expression,
texture, Geomorphological proccesses, extent)
* Get those same properties above, but in a dictionary format.
* If the code is composite (i.e., contains more than one terrain type) you can get the
amount of terrain types in the code, or first type, or last type.



## Quick install

`pip install bctcs_terrain_parser`

## Documentation and API reference

User-friendly documentation is available at <https://>. This includes complete descriptions of all console utilities and a complete API reference.

## Source code

The primary repository for this software is at <https://github.com/peatrc/bc_terrain_parser>.