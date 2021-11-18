locations = '1:60,61:120,121:180,181:240'
DNA = []
with open('output_sequence.txt', 'r') as origin:
    for line in origin:
        line = line.rstrip()
        DNA.append(line)
    DNA = ''.join(DNA)
    print(DNA)

# print(DNA[265-1:402])

# print(DNA)

def location_converter(locations):
    splitLocs = locations.split(",")
    for i in splitLocs:
        begin, end = i.split(':')
        begin = int(begin)-1 # Python indexing starts with 0, whereas DNA counting with 1.
        end = int(end) # Last item is non-inclusive
        print(begin, end)
        print(DNA[begin:end])
        print(len(DNA[begin:end]))

location_converter(locations)