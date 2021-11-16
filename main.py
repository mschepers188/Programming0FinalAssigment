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
#         # Should I maybe add this to the output file? Printing kills the whole process, so should I avoid that as well?
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
# origin_handler('CFTR_DNA.gb')
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
# definition_handler('CFTR_DNA.gb')