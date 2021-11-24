# Import of necessary modules
import re


class GenebankParser:
    """
    GenbankParser uses 2 parameters, self and file, which are used by the methods definition_handler
    and origin handler.
    definition_handler takes the file and returns the definition from the file as a string.
    origin_handler takes the file and returns the origin from the file as a string.
    """
    # Creates empty lists to add definition and origin
    definition = []
    origin = []

    def definition_handler(self, file):
        """
        'definition_handler' takes 'self' and 'file' as parameters. The entered file should be a genebank type file with
        DNA, mRNA or protein sequence.
        The file is read line by line and indexed, the line with the definition is then stripped, cleaned and returned.
        'definition_handler' returns the definition from the input file as a single string
        """

        # Temporary variables for following loop
        tmp_definition = []
        line_found = False

        # Opens the file line by line, indexes the line(s) containing the Definition.
        with open(file, 'r') as gbfile:
            for line in gbfile:  # Opens lines in the text one by one
                line = line.rstrip()
                if 'DEFINITION' in line:  # Finds the first line containing the definition
                    tmp_definition = [line]
                    line_found = True
                    if line.endswith('.'):  # If the line ends with '.', that should be the end of the definition.
                        break
                    else:
                        pass
                elif line_found is True and not line.endswith('.'):  # If definition has been found, appends line.
                    tmp_definition.append(line)
                elif line_found is True and line.endswith('.'):
                    # If definition has been found and line ends with a '.' end of definition has been reached.
                    tmp_definition.append(line)
                    line_found = False  # Set to false so program won't append any more lines.
                else:
                    pass

        tmp_definition = ''.join(tmp_definition)
        # Substitute DEFINITION and empty spaces by nothing using regex
        regex_str_one = re.compile(r'DEFINITION\s{2,}')
        tmp_definition = re.sub(regex_str_one, "", tmp_definition)
        regex_str_two = re.compile(r'\s{2,}')
        tmp_definition = re.sub(regex_str_two, " ", tmp_definition)
        # Assigns the temporary file holding the definition to self.definition.
        self.definition = tmp_definition
        # Returns self.definition so it can be caught in a new variable outside of this class.
        return self.definition

    def origin_handler(self, file):
        """
        'origin_handler' takes 'self' and 'file' as parameters. The entered file should be a genebank type file with
        DNA, mRNA or protein sequence.
        The file is read line by line and indexed, the lines with the origin are then stripped, cleaned and returned.
        'origin_handler' returns the origin from the input file as a single string.
        """

        # Creating null variables for loop
        index_origin_begin = 0
        index_origin_end = 0
        line_number = 0

        # Opens and identifies the location of the origin, returning begin line and end line.
        try:
            with open(file, 'r') as gbfile:
                for line in gbfile:  # Opens lines in the text one by one.
                    line_number += 1  # Keeping count of the line number for later indexing
                    line = line.rstrip()  # Removing any trailing characters
                    # Following loop selects all the lines containing the origin
                    if "ORIGIN" in line:
                        index_origin_begin = line_number + 1  # Finds line number just before origin and adds 1.
                    elif "//" in line:
                        index_origin_end = line_number - 1  # Finds line number right after origin and subtracts 1.
        except(FileNotFoundError, IOError):
            return "File not found or incorrect file path"

        # Uses the line numbers from above code to select origin and then removes all non-alphabet characters
        dna_list = []
        with open(file, 'r') as gbfile:
            line_number = 0
            for line in gbfile:
                line_number += 1
                line = line.rstrip()  # Removing any trailing characters
                # If line number is in between origin begin line and origin line,
                # line is 'cleaned' and appended to dna_list.
                if index_origin_begin <= line_number <= index_origin_end:
                    regex_string = re.compile('[^a-zA-Z]')
                    line = re.sub(regex_string, "", line)
                    dna_list.append(line)
            dna_list = ''.join(dna_list)  # Turns dna_list into a single string for easier indexing
        # Assigns the temporary file holding the dna string to self.origin.
        self.origin = dna_list
        # Returns self.definition so it can be caught in a new variable outside of this class.
        return self.origin
