def basechanger(seq, output_type):
    """
    Takes 2 parameters, a DNA sequence (seq) and output type ("compl" or "rev_compl" which respectively give
    the complement DNA or the reverse complement DNA').
    """
    dna_seq_compl = []

    for i in seq:
        if i == 'a'.casefold():
            dna_seq_compl.append('t')
        elif i == 't'.casefold():
            dna_seq_compl.append('a')
        elif i == 'g'.casefold():
            dna_seq_compl.append('c')
        elif i == 'c'.casefold():
            dna_seq_compl.append('g')

    dna_seq_compl = ''.join(dna_seq_compl)
    dna_seq_rev_compl = dna_seq_compl[::-1]

    if output_type == 'compl':
        return dna_seq_compl
    elif output_type == 'rev_compl':
        return dna_seq_rev_compl
    else:
        return 'incorrect input, please enter: "compl" or "rev_compl"'
