def location_converter(locations, origin):

    splitlocs = locations.split(",")
    tmp_sequence = []
    for i in splitlocs:
        if ':' in i:
            begin, end = i.split(':')
            begin = int(begin)-1  # Python indexing starts with 0, whereas DNA counting with 1.
            end = int(end)  # Last item is non-inclusive
            tmp_sequence += origin[begin:end]
        else:
            base_number = int(i) - 1
            tmp_sequence += origin[base_number]
    tmp_sequence = ''.join(tmp_sequence)

    return tmp_sequence


def location_converter_upper_rev(locations, origin):

    from NucleotideInverter import basechanger

    splitlocs = locations.split(",")
    origin_tmp = origin
    for i in splitlocs:
        if ':' in i:
            begin, end = i.split(':')
            begin = int(begin)-1  # Python indexing starts with 0, whereas DNA counting with 1.
            end = int(end)  # Last item is non-inclusive
            reverse_compl_seq = basechanger(origin[begin:end], 'rev_compl')
            origin_tmp = origin_tmp[:begin] + reverse_compl_seq.upper() + origin_tmp[end:]
        else:
            base_number = int(i) - 1
            reverse_compl_seq = basechanger(origin[base_number], 'rev_compl')
            origin_tmp = origin_tmp[:base_number-1] + reverse_compl_seq.upper() + origin_tmp[base_number+1:]
    return origin_tmp


def location_converter_upper(locations, origin):
    splitlocs = locations.split(",")
    origin_tmp = origin
    for i in splitlocs:
        if ':' in i:
            begin, end = i.split(':')
            begin = int(begin)-1  # Python indexing starts with 0, whereas DNA counting with 1.
            end = int(end)  # Last item is non-inclusive
            origin_tmp = origin_tmp[:begin] + origin_tmp[begin:end].upper() + origin_tmp[end:]
        else:
            base_number = int(i) - 1
            origin_tmp = origin_tmp[:base_number-1] + origin_tmp[base_number].upper() + origin_tmp[base_number+1:]
    return origin_tmp
