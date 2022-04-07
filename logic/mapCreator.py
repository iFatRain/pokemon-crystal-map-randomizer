# Use this like this in command line:
# $ python mapping.py <file_name> <map_name> <location_name>
import re
import sys

# put arguments into variables
fileName = str(sys.argv[1])
mapGroup = str(sys.argv[2])
specificMap = str(sys.argv[3])

# filter out the warp names


warp_event_found = False
warps = []

with open(fileName) as f:
    line = f.readline()
    while line:
        # read line until you find "def_warp_events". then convert each line into warp point, until you find empty line
        line = f.readline()
        if (line == "\n"):
            warp_event_found = False

        if (warp_event_found):
            # format this line and push to warps list
            line_list = line.split(", ")
            warps.append(line_list[2] + "_" + line_list[3].rstrip("\n"))

        if (line == "\tdef_warp_events\n"):
            warp_event_found = True

# close input file
f.close()

# create the code string
# proper_map_name = "_".join(re.findall('[A-Z][^A-Z]*', fileName.split(".")[0]))
if any(char.isdigit() for char in fileName):
    map_name = re.split('(B*[0-9]F)', fileName.split(".")[0])
    proper_map_name = '_'.join(re.findall('[A-Z][^A-Z]*', map_name[0])) + '_' + map_name[1]

else:
    proper_map_name = '_'.join(re.findall('[A-Z][^A-Z]*', fileName.split(".")[0]))

imports = ("from enum import IntEnum, Enum\n" +
           "from class_definitions import WarpInstruction, getHex\n" +
           "from map_data.map_constants import MapGroup, " + mapGroup)

header = ("\nmapGroup = MapGroup." + mapGroup.upper() + "\n" +
          "specificMap = " + mapGroup.lower().title() + "." + proper_map_name.upper() + "\n\n")

enum = ("class " + proper_map_name.upper() + "(IntEnum):\n" +
        "\tdef __str__(self):\n" +
        "\t\treturn str(self.value)\n\n")

enum_list = ""
i = 1
for warp in warps:
    enum_list += "\t" + warp + " = " + str(i) + "\n"
    i += 1
enum_list += "\n\n"

hex_enum = "class " + proper_map_name + "_Warp_Points(Enum): \n\n"

hex_enum_list = ""
for warp in warps:
    hex_enum_list += "\t" + (proper_map_name.upper() + "_TO_" + warp + "_WP = WarpInstruction( \n" +
                             "\t\tgetHex(" + proper_map_name.upper() + "." + warp + "), \n" +
                             "\t\tgetHex(mapGroup),\n" +
                             "\t\tgetHex(specificMap)\n" +
                             "\t\t) \n\n")

# combine all in one string
result = imports + header + enum + enum_list + hex_enum + hex_enum_list

# get same output file name as input file
output_file = fileName.split(".")[0] + "_Map" + ".py"

# print to file
with open(output_file, "w") as text_file:
    text_file.write(result)




