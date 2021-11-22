from GenbankParser import *
from Feature import *
from pathlib import Path
import sys
import os.path


def main(file, output_format):
    # Output format can be 'separated' or 'uppercased'

    if file.lower().endswith('.gp'):
        pass
    elif file.lower().endswith('.gb'):
        pass
    else:
        return "Incorrect file format"
        # Return ends the function so the task won't be performed on an incorrect file type

    if os.path.isfile(file):
        path_object = Path(file)
        file_name = path_object.stem
        new_filename = f"{file_name}_features.txt"

        gbankvar1 = GenebankParser()
        definition = gbankvar1.definition_handler(file)  # Returns definition
        origin = gbankvar1.origin_handler(file)  # Returns origin
        # Determine if protein or DNA/RNA, you might have to substitute it to get a DNA origin
        gbankvar2 = Feature()
        gbankvar2.feature_handler(file, origin, definition, output_format)
        os.rename('final_file.txt', new_filename)
    else:
        return "File not found or incorrect path"


if __name__ == "__main__":
    # To accept user input from terminal, the sys.argv package is used
    file = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 else 'separated'
    main(file, output_format)
