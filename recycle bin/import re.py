import re
# Create a variable called terrain_code and set its value to "/Msa=Mw-V/Rsa"
terrain_code = "/Msa=Mw-V/Rsa"

# Split the terrain_code string before every occurrence of "/" and "=" that does not occur as the first character.
# The regular expression pattern matches "/" or "=" not followed by the start of the string "^" or another "/" or "=".
# The split method returns a list of substrings.
terrain_code_split = re.split("(?<!^)[/=]", terrain_code)