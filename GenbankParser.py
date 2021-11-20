class GenebankParser:
    definition = []
    origin = []

    def definition_handler(self, file):
        import re  # Add to class, make it global inside the class
        tmp_definition = []
        line_found = False

        with open(file, 'r') as gbfile:
            for line in gbfile:
                line = line.rstrip()
                if 'DEFINITION' in line:  # Finds the first line containing the definition
                    tmp_definition = [line]
                    line_found = True
                    if line.endswith('.'):
                        break
                    else:
                        pass
                elif line_found is True and not line.endswith('.'):  # If definition has been found, appends line.
                    tmp_definition.append(line)
                    print(line)
                elif line_found is True and line.endswith('.'):
                    # If definition has been found and line ends with a '.' end of definition has been reached.
                    tmp_definition.append(line)
                    line_found = False  # Set to false so program won't append any more lines.
                else:
                    pass

        tmp_definition = ''.join(tmp_definition)
        # print(tmp_definition)
        # Substitute DEFINITION and empty spaces by nothing
        regex_str_one = re.compile('DEFINITION\s{2,}')
        tmp_definition = re.sub(regex_str_one, "", tmp_definition)
        regex_str_two = re.compile('\s{2,}')
        tmp_definition = re.sub(regex_str_two, " ", tmp_definition)

        self.definition = tmp_definition

        return (self.definition)

    # definition = filetest

    # definition_handler('Testfile.gp')

    def origin_handler(self, file):
        # Creating null variables for loop
        index_origin_begin = 0
        index_origin_end = 0
        line_number = 0
        # Importing regex to remove all non-alphabet characters from origin
        import re  # Add to class, make it global inside the class

        # Opens and identifies the location of the origin
        try:
            with open(file, 'r') as gbfile:
                for line in gbfile:  # Opens lines in the text one by one
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
                if index_origin_begin <= line_number <= index_origin_end:
                    regex_string = re.compile('[^a-zA-Z]')
                    line = re.sub(regex_string, "", line)
                    dna_list.append(line)
            dna_list = ''.join(dna_list)

        self.origin = dna_list
        return self.origin

# if __name__ == "__main__":
#     main()

# filetest = GenebankParser()
# # Returns definition
# print(filetest.definition_handler('CFTR_DNA.gb'))
# # Returns origin
# filetest = GenebankParser()
# print(filetest.origin_handler('CFTR_DNA.gb'))
