def origin_handler(file):
    # Creating null variables for loop
    index_origin_begin = 0
    index_origin_end = 0
    line_number = 0
    # Importing regex to remove all non-alphabet characters from origin
    import re # Add to class, make it global inside the class

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
        # Should I maybe add this to the output file?
        # Printing kills the whole process, so should I avoid that as well?

    # Uses the line numbers from above code to select origin and then removes all non-alphabet characters
    dna_list = []
    with open(file, 'r') as gbfile:
        output_sequence = open("output_sequence.txt", "w")  # Creates or overwrites existing file for sequence output
        line_number = 0
        for line in gbfile:
            line_number += 1
            line = line.rstrip()  # Removing any trailing characters
            if index_origin_begin <= line_number <= index_origin_end:
                regex_string = re.compile('[^a-zA-Z]')
                line = re.sub(regex_string, "", line)
                # print(line)
                dna_list.append(line)
                with open("output_sequence.txt", "a") as output_file:
                    output_file.write(line + "\n")
        output_sequence.close()
    # print(dna_list)
origin_handler('Testfile.gp')

def definition_handler(file):
    import re  # Add to class, make it global inside the class
    tmp_definition = []
    line_found = False

    with open(file, 'r') as gbfile:
        for line in gbfile:
            line = line.rstrip()
            if 'DEFINITION' in line: # Finds the first line containing the definition
                tmp_definition = [line]
                line_found = True
            elif line_found == True and not line.endswith('.'): # If definition has been found, appends line.
                tmp_definition.append(line)
            elif line_found == True and line.endswith('.'):
                # If definition has been found and line ends with a '.' end of definition has been reached.
                tmp_definition.append(line)
                line_found = False # Set to false so program won't append any more lines.
            else:
                pass

    tmp_definition = ''.join(tmp_definition)
    # print(tmp_definition)
    # Substitute DEFINITION and empty spaces by nothing
    regex_str_one = re.compile('DEFINITION\s{2,}')
    tmp_definition = re.sub(regex_str_one, "", tmp_definition)
    regex_str_two = re.compile('\s{2,}')
    tmp_definition = re.sub(regex_str_two, " ", tmp_definition)

    return(tmp_definition)

# definition_handler('Testfile.gp')

def feature_index_handler(file):
    import re
    feature_begin = 0
    feature_end = 0

    with open(file, 'r') as gbfile:
        line_number = 0
        for line in gbfile:
            line_number += 1 # Keeps track of line number for every line
            if "FEATURES" in line:
                # print(line, line_number)
                feature_begin = line_number + 1 # The features start the line after the header has been found.
            elif 'ORIGIN' in line:
                # print(line, line_number)
                feature_end = line_number - 1 # Line containing the origin, the features end one line before.
                break
            else:
                pass
    return(feature_begin, feature_end)

# feature_index_handler('Testfile.gp')

def location_handler(feature_list):
    location_tmp_parts = []  # Variable to hold parts of locations
    feature_list_edited = []  # Feature list to hold corrected locations
    import re

    for i in feature_list:
        if i.endswith(','):
            location_tmp_parts.append(i)
        elif i.endswith(')'):
            location_tmp_parts.append(i)
            # Joins the tmp locations into 1 and resets previous one if present.
            location_tmp_compl = ''.join(location_tmp_parts)
            feature_list_edited.append(location_tmp_compl)
            location_tmp_parts = []  # Resets the tmp location holder
        else:
            feature_list_edited.append(i)

    with open("final_file.txt", "w") as final_file:
        for i in feature_list_edited:
            if '..' in i and '/' not in i:
                index_i = feature_list_edited.index(i) + 1
                # print(index_i)
                feature_name, location = i.split('$', 1)
                qualifier = re.sub("\$", ' ', feature_list_edited[index_i])
                location = re.sub("\.\.", ':', location)
                if 'join' in location:
                    location = re.sub('join\(|\)', "", location)  # Replaces 1 or more empty spaces by $
                    # print(location)
                elif 'complement' in location:
                    location = re.sub('complement\(|\)', "", location)  # Replaces 1 or more empty spaces by $
                    # print(location)
                else:
                    # print(location)
                    pass
                # print(qualifier)
                # print(location)
                ## Call function that transforms b into actual sequence
                # b = b.blablabla
                final_file.write('>' + feature_name + ' ' + feature_list_edited[index_i] + "\n" + location + "\n"*2)
                # print('>' + feature_name + ' ' + feature_list_edited[index_i] + "\n" + location + "\n"*2)

def feature_handler(file):
    feature_list = []
    index_organism = []
    import re

    begin_end_feature = feature_index_handler(file) # Returns the beginning and end of the features
    feature_begin, feature_end = begin_end_feature[0], begin_end_feature[1]
    # print(feature_begin, feature_end) # Checking whether features have properly been indexed.

    with open(file, 'r') as gbfile:
        line_number = 0
        for line in gbfile:
            line_number += 1
            if line_number < feature_begin:
                pass
            elif feature_begin <= line_number <= feature_end:
                line = line.strip()
                line = re.sub(' +', "$", line)  # Replaces 1 or more empty spaces by $
                feature_list.append(line)  # Appends line to feature_list
    feature_list = location_handler(feature_list) #  Checks for locations that span more then 1 line and unites them.

    # print(feature_list)

feature_handler('Testfile.gp')

#
# # feature_handler('CFTR_DNA.gb')
#
#     sequence_string = []
#     with open('output_sequence.txt', 'r') as sequence_str:
#         for line in sequence_str:
#             line = line.strip()
#             # print(line)
#             sequence_string += line
#             sequence_string = ''.join(sequence_string)
#             begin, end = location.split(':', 1)
#             begin = int(begin) - 1 # Python indexing starts at zero, so -1
#             end = int(end) # Python indexing does not include the last item, thus -1 not necessary
#     print(begin, end)
#     print(sequence_string)
#     print(sequence_string[begin:end])
#
# feature_handler('Testfile.gp')
#
# # for i in feature_list_edited: