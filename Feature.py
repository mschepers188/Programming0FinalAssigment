class Feature:
    FeatureList = []

    def feature_index_handler(self, file):
        import re
        feature_begin = 0
        feature_end = 0

        with open(file, 'r') as gbfile:
            line_number = 0
            for line in gbfile:
                line_number += 1  # Keeps track of line number for every line
                if "FEATURES" in line:
                    # print(line, line_number)
                    feature_begin = line_number + 1  # The features start the line after the header has been found.
                elif 'ORIGIN' in line:
                    # print(line, line_number)
                    feature_end = line_number - 1  # Line containing the origin, the features end one line before.
                    break
                else:
                    pass
        return (feature_begin, feature_end)

    # feature_index_handler('Testfile.gp')

    def location_handler(self, feature_list):
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
        # return feature_list_edited

        # import LocationConverter

        with open("final_file.txt", "w") as final_file:
            for i in feature_list_edited:
                if '..' in i and '/' not in i:
                    index_i = feature_list_edited.index(i) + 1
                    feature_name, location = i.split('$', 1)
                    qualifier = re.sub("\$", ' ', feature_list_edited[index_i])
                    location = re.sub("\.\.", ':', location)
                    if 'join' in location:
                        location = re.sub('join\(|\)', "", location)  # Replaces 1 or more empty spaces by $
                        # Run Locationconverter normally
                    elif 'complement' in location:
                        location = re.sub('complement\(|\)', "", location)  # Replaces 1 or more empty spaces by $
                        # Run Locationconverter with reverse complement
                    else:
                        pass
                    ## Call function that transforms b into actual sequence
                    # b = b.blablabla
                    final_file.write('>' + feature_name + ' ' + qualifier + "\n" + location + "\n" * 2)
                    # print('>' + feature_name + ' ' + feature_list_edited[index_i] + "\n" + location + "\n"*2)

    def feature_handler(self, file):
        # Grabs the lines where the features are located and add them to a list.
        feature_list = []
        index_organism = []
        import re

        # 'feature_index_handler' returns the beginning and end of the features
        begin_end_feature = self.feature_index_handler(file)
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
        self.FeatureList = feature_list
        self.location_handler(self.FeatureList)

        # 'location_handler' checks for locations that span more then 1 line and unites them.

classy = Feature()
# print(classy.feature_handler('Testfile.gp'))
print(classy.feature_handler('CFTR_DNA.gb'))