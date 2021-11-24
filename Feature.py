# Import of necessary modules
import re
from LocationConverter import *
from NucleotideInverter import basechanger


class Feature:
    """
    Feature can take multiple parameters: "self, file, feature_list, origin, definition and output_format".
    These are used by the different methods to extract the features from the file and create the desired output file.
    """
    # Creates a variable to hold the feature list in self.
    FeatureList = []

    def feature_index_handler(self, file):
        """
        'feature_index_handler' takes 'self' and 'file' as parameters. The entered file should be a genebank
        type file with a DNA, mRNA or protein sequence.
        The file is read line by line and the location of the features is indexed, this output is used by
        feature_handler to locate the lines where the features are present.
        """

        feature_begin = 0
        feature_end = 0

        with open(file, 'r') as gbfile:
            line_number = 0
            for line in gbfile:  # Reads file line by line
                line_number += 1  # Keeps track of line number
                if "FEATURES" in line:
                    feature_begin = line_number + 1  # The features start the line after the header has been found.
                elif 'ORIGIN' in line:
                    feature_end = line_number - 1  # Line containing the origin, the features end one line before.
                    break
                else:
                    pass
        # Returns the line numbers of the features so feature_handler can select those lines from the file.
        return feature_begin, feature_end

    def location_handler_separated(self, feature_list, origin, definition):
        """
        'location_handler_separated' takes feature_list, origin and definition as parameters.
        The feature_list which contains all the DNA coordinates is used to extract these selections from
        the origin. Finally, the output is added together with the definition, feature name, qualifier to create the
        output file.
        """
        location_tmp_parts = []  # Variable to hold parts of locations
        feature_list_edited = []  # Feature list to hold corrected locations

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
        # return feature_list_edited

        with open("final_file.txt", "w") as final_file:
            final_file.write(definition + "\n" * 2)  # Writes the definition to file
            for i in feature_list_edited:
                if '..' in i and '/' not in i or i[-1].isdigit() and '/' not in i:
                    index_i = feature_list_edited.index(i) + 1
                    feature_name, location = i.split('$', 1)
                    qualifier = re.sub(r"\$", ' ', feature_list_edited[index_i])
                    location = re.sub(r"\.\.", ':', location)
                    location = re.sub(r'[<>]', "", location)
                    if 'join' in location:
                        location = re.sub(r'join\(|\)', "", location)  # Replaces 1 or more empty spaces by nothing
                        if 'complement' in location:
                            location = re.sub(r'complement|\(|\)', "", location)
                            # Replaces 1 or more empty spaces by nothing
                            location = location_converter(location, origin)
                            location = basechanger(location, 'rev_compl')
                            # Run location converter and then nucleotide inverter
                        else:
                            location = location_converter(location, origin)
                    elif 'complement' in location:
                        location = re.sub(r'complement\(|\)', "", location)
                        # Replaces 1 or more empty spaces by nothing
                        location = location_converter(location, origin)
                        location = basechanger(location, 'rev_compl')
                    elif 'order' in location:
                        location = re.sub(r'order\(|\)', "", location)
                        location = location_converter(location, origin)
                    else:
                        location = location_converter(location, origin)
                    # Splits the origin into chunks of 60
                    location = '\n'.join(re.findall('.{1,%i}' % 60, location))
                    # Writes feature name, qualifier and origin to file.
                    final_file.write('>' + feature_name + ' ' + qualifier + "\n" + location + "\n" * 2)

    def location_handler_uppercased(self, feature_list, origin, definition):
        """
        'location_handler_uppercased' takes feature_list, origin and definition as parameters.
        The feature_list which contains all the DNA coordinates is used to extract these selections from
        the origin. The selections are then made into uppercase. Finally, the output is added together with
        the definition, feature name, qualifier and part of the origin to create the output file.
        """
        location_tmp_parts = []  # Variable to hold parts of locations
        feature_list_edited = []  # Feature list to hold corrected locations
        # Selects locations that span more then 1 line and unites them
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
            final_file.write(definition + "\n" * 2)  # Writes the definition to file
            for i in feature_list_edited:
                origin_tmp = origin
                if '..' in i and '/' not in i or i[-1].isdigit() and '/' not in i:
                    index_i = feature_list_edited.index(i) + 1
                    # The string with '..' and without '/' contains the feature name and the coordenates
                    feature_name, location = i.split('$', 1)
                    # The next line will always contain the qualifier
                    qualifier = re.sub(r"\$", ' ', feature_list_edited[index_i])
                    location = re.sub(r"\.\.", ':', location)
                    location = re.sub(r'[<>]', "", location)  # < or > do not matter for these purposes
                    if 'join' in location:
                        location = re.sub(r'join\(|\)', "", location)  # Replaces join() by nothing
                        if 'complement' in location:
                            location = re.sub(r'complement|\(|\)', "", location)  # Replaces complement() by nothing
                            origin_tmp = location_converter_upper_rev(location, origin_tmp)
                            # Run location converter and then nucleotide inverter
                        else:
                            origin_tmp = location_converter_upper(location, origin_tmp)
                    elif 'complement' in location:
                        location = re.sub(r'complement|\(|\)', "", location)  # Replaces complement() by nothing
                        origin_tmp = location_converter_upper_rev(location, origin_tmp)
                    elif 'order' in location:
                        location = re.sub(r'order\(|\)', "", location)  # Replaces order() by nothing
                        origin_tmp = location_converter_upper(location, origin_tmp)
                    else:
                        origin_tmp = location_converter_upper(location, origin_tmp)

                    # With uppercased view, origin ends with the last feature, thus this is determined:
                    location = re.sub(':', ',', location)
                    splitlocs = location.split(",")
                    seq_end = int(splitlocs[-1])
                    origin_tmp = origin_tmp[0:seq_end]
                    # Splits the origin into chunks of 60
                    origin_tmp = '\n'.join(re.findall('.{1,%i}' % 60, origin_tmp))
                    # Writes feature name, qualifier and origin to file.
                    final_file.write('>' + feature_name + ' ' + qualifier + "\n" + origin_tmp + "\n" * 2)

    def feature_handler(self, file, origin, definition, output_format):
        """
        'feature_handler' takes file, origin, definition and output_format as parameters.
        By using the feature_index_handler() it determines the location of the features and extracts these from the
        input file. Depending on the desired output format, this method uses either 'location_handler_separated' or
        'location_handler_uppercased'. Both will output a multi-fasta like file, whereas the latter outputs the selected
        sequence regions in uppercase.
        'feature_handler' has no return statement as it only outputs a a .txt file.
        """
        # Grabs the lines where the features are located and adds them to a list.
        feature_list = []

        # 'feature_index_handler' returns the beginning and end of the features
        begin_end_feature = self.feature_index_handler(file)
        feature_begin, feature_end = begin_end_feature[0], begin_end_feature[1]

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

        self.FeatureList = feature_list
        # 'location_handler' checks for locations that span more then 1 line and unites them. Afterwards the lines
        # are 'cleaned up' and finally the output file containing the definition, feature name, qualifier
        # and origin are written to the output file in the 'separated' or 'uppercased' output type.
        if output_format == 'separated':
            self.location_handler_separated(self.FeatureList, origin, definition)
        elif output_format == 'uppercased':
            self.location_handler_uppercased(self.FeatureList, origin, definition)
