DNASeq = 'atccgggtcaactttagtccgttgaacatgcttcttgaaaacctagttctcttaaaataa'

def basechanger(Seq):
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

    print(DNASeq_compl)
    print(DNASeq_rev_compl)

basechanger(DNASeq)