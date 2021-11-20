from GenbankParser import *
from Feature import *
# file = 'CFTR_DNA.gb'

# With init check whether the file is valid and whether is actually contains DNA

def main_func(file, output_format ='uppercased'):
    filetest = GenebankParser()
    definition = filetest.definition_handler(file) # Returns definition
    origin = filetest.origin_handler(file)  # Returns origin
    molecule = ''
    # print(definition) # print(origin)
    filetesttwo = Feature()
    filetesttwo.feature_handler(file, origin, output_format)

main_func('CFTR_DNA.gb')

# class genbanktool:
#     Filetype = ''
#
#     # Add try exept later
#
#     def __init__(self, file):
#         try:
#             if file.lower().endswith('.gp'):
#                 self.Filetype = 'gp'
#             elif file.lower().endswith('.gb'):
#                 self.Filetype = 'gb'
#         except:
#             return "Incorrect file format"
#
#         # Check extension
#         import GenbankParser
#         import Feature
#
#     # def parser(self):
#
# test = genbanktool('CFTR_DNA.g')
# print(test)