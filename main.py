from GenbankParser import *
from Feature import *
import os.path
from pathlib import Path

def main(file, output_format ='separated'):
    Filetype = ''
    # Output format can be 'separated' or 'uppercased'

    if file.lower().endswith('.gp'):
        Filetype = 'gp'
    elif file.lower().endswith('.gb'):
        Filetype = 'gb'
    else:
        return "Incorrect file format"
        # Return ends the function so the task won't be performed on an incorrect file type

    if os.path.isfile(file):
        path_object = Path(file)
        # print(path_object.parent)
        file_name = path_object.stem
        file_extention = path_object.suffix
        new_filename = f"{file_name}_features.txt"

        gbankvar1 = GenebankParser()
        definition = gbankvar1.definition_handler(file) # Returns definition
        origin = gbankvar1.origin_handler(file)  # Returns origin
        # Determine if protein or DNA/RNA, you might have to substitute it to get a DNA origin
        gbankvar2 = Feature()
        gbankvar2.feature_handler(file, origin, definition, output_format)
        os.rename('final_file.txt', new_filename)
    else:
        return "File not found or incorrect path"

main('CFTR_protein.gp', 'uppercased')