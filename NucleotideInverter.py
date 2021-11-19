DNASeq = 'gattcgctaaatcatccatc'

def basechanger(Seq, output):
    DNASeq_compl = []
    DNASeq_rev_compl = []

    for i in Seq:
        if i == 'a'.casefold():
            DNASeq_compl.append('t')
        elif i == 't'.casefold():
            DNASeq_compl.append('a')
        elif i == 'g'.casefold():
            DNASeq_compl.append('c')
        elif i == 'c'.casefold():
            DNASeq_compl.append('g')

    DNASeq_compl = ''.join(DNASeq_compl)
    DNASeq_rev_compl = DNASeq_compl[::-1]

    if output == 'compl':
        return(DNASeq_compl)
    elif output == 'rev_compl':
        return(DNASeq_rev_compl)
    else:
        return('incorrect input, please enter: "Compl" or "rev_compl"')

basechanger(DNASeq, 're_compl')