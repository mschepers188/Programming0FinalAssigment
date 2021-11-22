import re
from LocationConverter import *
from NucleotideInverter import basechanger


class Feature:
    FeatureList = []

    def feature_index_handler(self, file):

        feature_begin = 0
        feature_end = 0

        with open(file, 'r') as gbfile:
            line_number = 0
            for line in gbfile:
                line_number += 1  # Keeps track of line number for every line
                if "FEATURES" in line:
                    feature_begin = line_number + 1  # The features start the line after the header has been found.
                elif 'ORIGIN' in line:
                    feature_end = line_number - 1  # Line containing the origin, the features end one line before.
                    break
                else:
                    pass
        return feature_begin, feature_end

    def location_handler_separated(self, feature_list, origin, definition):
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
            final_file.write(definition + "\n" * 2)
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

                    location = '\n'.join(re.findall('.{1,%i}' % 60, location))
                    final_file.write('>' + feature_name + ' ' + qualifier + "\n" + location + "\n" * 2)

    def location_handler_uppercased(self, feature_list, origin, definition):
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
            final_file.write(definition + "\n" * 2)
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
                        location = re.sub(r'order\(|\)', "", location)
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
                    final_file.write('>' + feature_name + ' ' + qualifier + "\n" + origin_tmp + "\n" * 2)

    def feature_handler(self, file, origin, definition, output_format):
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
        # 'location_handler' checks for locations that span more then 1 line and unites them.
        if output_format == 'separated':
            self.location_handler_separated(self.FeatureList, origin, definition)
        elif output_format == 'uppercased':
            self.location_handler_uppercased(self.FeatureList, origin, definition)
