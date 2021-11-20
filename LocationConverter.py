def location_converter(locations, origin):

    splitLocs = locations.split(",")
    # print(splitLocs)
    tmp_sequence = []
    for i in splitLocs:
        begin, end = i.split(':')
        # begin, end = i.split('..')
        begin = int(begin)-1 # Python indexing starts with 0, whereas DNA counting with 1.
        end = int(end) # Last item is non-inclusive
        # print(begin, end)
        # print(origin[begin:end])
        tmp_sequence.append(origin[begin:end])
    tmp_sequence = ''.join(tmp_sequence)
    # print(tmp_sequence)

    return(tmp_sequence)

def location_converter_upper_rev(locations, origin):

    from NucleotideInverter import basechanger

    splitLocs = locations.split(",")
    # print(splitLocs)
    origin_tmp = origin
    for i in splitLocs:
        begin, end = i.split(':')
        begin = int(begin)-1 # Python indexing starts with 0, whereas DNA counting with 1.
        end = int(end) # Last item is non-inclusive
        # print(begin, end)
        original_seq = origin[begin:end]
        # print(original_seq)
        reverse_compl_seq = basechanger(origin[begin:end], 'rev_compl')
        # print(reverse_compl_seq)
        origin_tmp = origin_tmp.replace(original_seq, reverse_compl_seq.upper())
        # print(origin_tmp)
    return origin_tmp

# location_converter_upper_rev(locations, origin)
# locations = '1:10,21:30,31:50'
# origin = 'aacctttccaaaaatgattccatctgatataggattaagaaaaatattttccgaaatctc'

def location_converter_upper(locations, origin):
    # print(locations)
    splitLocs = locations.split(",")
    # print(splitLocs)
    origin_tmp = origin
    for i in splitLocs:
        begin, end = i.split(':')
        begin = int(begin)-1 # Python indexing starts with 0, whereas DNA counting with 1.
        end = int(end) # Last item is non-inclusive
        # print(begin, end)
        original_seq = origin[begin:end]
        origin_tmp = origin_tmp.replace(original_seq, original_seq.upper())
        # print(origin_tmp)
    return origin_tmp

# location_converter_upper(locations, origin)