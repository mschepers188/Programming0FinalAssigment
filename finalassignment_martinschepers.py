# Import of necessary modules
from GenbankParser import *
from Feature import *
from pathlib import Path
import sys
import os.path


def main(file, output_format):
    """
    This program functions as a Genebank feature extractor and is compatible with DNA, mRNA and protein files.
    The output format can be 'separated' or 'uppercased', not entering the second argument (sys.argv[2]) results
    in the default 'separated'. By utilizing the two classes 'GenebankParser' and 'Feature' the defitinition, origin
    and features are extracted from the file and delivered back to the user as .txt file.
    """

    # Checks if the file extension is correct
    # Returns "Incorrect file format" and ends the function, so the task won't be performed on an incorrect file type
    if file.lower().endswith('.gp'):
        pass
    elif file.lower().endswith('.gb'):
        pass
    else:
        return "Incorrect file format"

    if output_format == 'separated' or 'uppercased':
        pass
    else:
        return "Incorrect output file requested"

    # Checks if the file exists at the appointed path and creates a variable to hold the file name
    if os.path.isfile(file):
        path_object = Path(file)
        file_name = path_object.stem
        new_filename = f"{file_name}_features.txt"

        # creates instances of GenebankParser and calls different methods to catch the definition and origin
        gbankvar1 = GenebankParser()
        definition = gbankvar1.definition_handler(file)  # Returns definition
        origin = gbankvar1.origin_handler(file)  # Returns origin
        # creates instances of Feature and calls a methods which creates the output file.
        gbankvar2 = Feature()
        gbankvar2.feature_handler(file, origin, definition, output_format)
        os.rename('final_file.txt', new_filename)
    else:
        return FileNotFoundError


if __name__ == "__main__":
    # To accept user input from terminal, the sys.argv package is used
    file = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 else 'separated'
    main(file, output_format)
