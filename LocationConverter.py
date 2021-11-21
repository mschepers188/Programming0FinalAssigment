def location_converter(locations, origin):

    splitLocs = locations.split(",")
    # print(splitLocs)
    tmp_sequence = []
    for i in splitLocs:
        #print(i)
        if ':' in i:
            # print(i)
            begin, end = i.split(':')
            begin = int(begin)-1 # Python indexing starts with 0, whereas DNA counting with 1.
            end = int(end) # Last item is non-inclusive
            # print(begin, end)
            # print(origin[begin:end])
            tmp_sequence += origin[begin:end]
        else:
            base_number = int(i) - 1
            tmp_sequence += origin[base_number]
    tmp_sequence = ''.join(tmp_sequence)

    return(tmp_sequence)

# location_converter(locations, origin)

# locations = '1:5,21:30,58'
# origin = 'aacctccaaaaatgattccatctgatataggattaagaaaaatattttccgaaatctc'

def location_converter_upper_rev(locations, origin):

    from NucleotideInverter import basechanger

    splitLocs = locations.split(",")
    # print(splitLocs)
    origin_tmp = origin
    for i in splitLocs:
        if ':' in i:
            begin, end = i.split(':')
            begin = int(begin)-1 # Python indexing starts with 0, whereas DNA counting with 1.
            end = int(end) # Last item is non-inclusive
            reverse_compl_seq = basechanger(origin[begin:end], 'rev_compl')
            # print(reverse_compl_seq)
            origin_tmp = origin_tmp[:begin] + reverse_compl_seq.upper() + origin_tmp[end:]
        else:
            base_number = int(i) - 1
            reverse_compl_seq = basechanger(origin[base_number], 'rev_compl')
            origin_tmp = origin_tmp[:base_number-1] + reverse_compl_seq.upper() + origin_tmp[base_number+1:]
    #print(origin_tmp)
    return origin_tmp

# location_converter_upper_rev(locations, origin)

def location_converter_upper(locations, origin):
    splitLocs = locations.split(",")
    origin_len = len(origin)
    origin_tmp = origin
    for i in splitLocs:
        if ':' in i:
            begin, end = i.split(':')
            begin = int(begin)-1 # Python indexing starts with 0, whereas DNA counting with 1.
            end = int(end) # Last item is non-inclusive
            origin_tmp = origin_tmp[:begin] + origin_tmp[begin:end].upper() + origin_tmp[end:]
        else:
            base_number = int(i) - 1
            origin_tmp = origin_tmp[:base_number-1] + origin_tmp[base_number].upper() + origin_tmp[base_number+1:]
    # print(origin_tmp)
    return origin_tmp

# location_converter_upper(locations, origin)