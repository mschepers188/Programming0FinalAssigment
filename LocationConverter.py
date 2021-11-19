def location_converter(locations):

    DNA = [] # Create local variable to hold DNA sequence
    with open('output_sequence.txt', 'r') as origin: # Load the file with origin and create variable
        for line in origin:
            line = line.rstrip()
            DNA.append(line)
        DNA = ''.join(DNA) # Turn list into single string

    # Get
    splitLocs = locations.split(",")
    tmp_sequence = []
    for i in splitLocs:
        # begin, end = i.split(':')
        begin, end = i.split('..')
        begin = int(begin)-1 # Python indexing starts with 0, whereas DNA counting with 1.
        end = int(end) # Last item is non-inclusive
        # print(begin, end)
        tmp_sequence.append(DNA[begin:end])
    tmp_sequence = ''.join(tmp_sequence)
    return(tmp_sequence)

location_converter(locations)