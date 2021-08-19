def to_rna(dna_strand):
    dna = 'GCTA'
    rna = 'CGAU'
    table = dna_strand.maketrans(dna, rna)
    return dna_strand.translate(table)