# def origin_handler(file):
#     # Creating null variables for loop
#     index_origin_begin = 0
#     index_origin_end = 0
#     line_number = 0
#     # Importing regex to remove all non-alphabet characters from origin
#     import re # Add to class, make it global inside the class
#
#     # Opens and identifies the location of the origin
#     try:
#         with open(file, 'r') as gbfile:
#             for line in gbfile:  # Opens lines in the text one by one
#                 line_number += 1  # Keeping count of the line number for later indexing
#                 line = line.rstrip()  # Removing any trailing characters
#                 # Following loop selects all the lines containing the origin
#                 if "ORIGIN" in line:
#                     index_origin_begin = line_number + 1  # Finds line number just before origin and adds 1.
#                 elif "//" in line:
#                     index_origin_end = line_number - 1  # Finds line number right after origin and subtracts 1.
#     except(FileNotFoundError, IOError):
#         return "File not found or incorrect file path"
#         # Should I maybe add this to the output file?
#         # Printing kills the whole process, so should I avoid that as well?
#
#     # Uses the line numbers from above code to select origin and then removes all non-alphabet characters
#     with open(file, 'r') as gbfile:
#         output_sequence = open("output_sequence.txt", "w")  # Creates or overwrites existing file for sequence output
#         line_number = 0
#         for line in gbfile:
#             line_number += 1
#             line = line.rstrip()  # Removing any trailing characters
#             if index_origin_begin <= line_number <= index_origin_end:
#                 regex_string = re.compile('[^a-zA-Z]')
#                 line = re.sub(regex_string, "", line)
#                 with open("output_sequence.txt", "a") as output_file:
#                     output_file.write(line + "\n")
#         output_sequence.close()
#
# origin_handler('Testfile.gp')
#
# def definition_handler(file):
#     import re  # Add to class, make it global inside the class
#     output_definition = open("output_definition.txt", "w") # Creates or overwrites existing file for definition output
#     with open(file, 'r') as gbfile:
#         for line in gbfile:
#             if 'DEFINITION' in line:
#                 line = line.rstrip()  # Removing any trailing characters
#                 regex_string = re.compile('DEFINITION\s{2}')
#                 line = re.sub(regex_string, "", line)
#                 with open("output_definition.txt", "a") as output_file:
#                     output_definition.write(line + "\n")
#             else:
#                 pass
#     output_definition.close()
#
# definition_handler('Testfile.gp')

def feature_handler(file):
    import re
    feature_begin = 0
    feature_end = 0

    with open(file, 'r') as gbfile:
        line_number = 0
        for line in gbfile:
            if "FEATURES" in line:
                line_number += 1
                feature_begin = line_number
            elif 'ORIGIN' in line:
                feature_end = line_number - 1
                break
            else:
                line_number += 1

    # regex_string = re.compile('DEFINITION\s{2}')
    # line = re.sub(regex_string, "", line)

    line_number = 0
    feature_list = []
    # index_organism = []

    with open(file, 'r') as gbfile:

        for line in gbfile:
            if line_number < feature_begin:
                line_number += 1
                pass
            elif feature_begin <= line_number <= feature_end:
                line_number += 1
                line = line.strip()
                line = re.sub(' +', "$", line)  # Replaces 1 or more empty spaces by $
                feature_list.append(line)  # Appends line to feature_list

    # for i in feature_list:
    #     if "/organism=" in i:
    #         index_organism = feature_list.index(i)
    #     else:
    #         pass

    location_tmp_parts = []  # Variable to hold parts of locations
    feature_list_edited = []  # Feature list to hold corrected locations

    #  Following statement checks for locations that span more then 1 line
    #  and makes them into a single element in the list.
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

    # print(feature_list_edited)

    feature_list_final = []

    with open("final_file.txt", "w") as final_file:
        for i in feature_list_edited:
            if '..' in i and '/' not in i:
                index_i = feature_list_edited.index(i) + 1
                # print(index_i)
                feature_name, location = i.split('$', 1)
                ## Call function that transforms b into actual sequence
                # b = b.blablabla
                # final_file.write('>' + feature_name + ' ' + feature_list_edited[index_i] + "\n" + location + "\n"*2)
                qualifier = re.sub("\$", ' ', feature_list_edited[index_i])
                location = re.sub("\.\.", ':', location)
                print(location)
                # print('>' + feature_name + ' ' + qualifier + "\n" + location + "\n"*2)
                break
    with open("final_file.txt", "r") as final_file:
        for line in final_file:
            print(line)

    sequence_string = []
    with open('output_sequence.txt', 'r') as sequence_str:
        for line in sequence_str:
            line = line.strip()
            print(line)
            sequence_string += line
            sequence_string = ''.join(sequence_string)
    print(sequence_string)

feature_handler('Testfile.gp')

# for i in feature_list_edited: