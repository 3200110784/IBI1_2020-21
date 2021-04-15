
def corresponding_DNA(DNA):
    DNA=DNA.upper()#cover the sequnce to uppercase
    cDNA = ''
    i=0
    while i <= len(DNA)-1:#corresponding
        if DNA[i]=='A':
            cDNA='T'+cDNA
            i=i+1
        elif DNA[i]=='T':
            cDNA='A'+cDNA
            i=i+1
        elif DNA[i]=='C':
            cDNA='G'+cDNA
            i=i+1
        elif DNA[i]=='G':
            cDNA='C'+cDNA
            i=i+1
    return cDNA
print(corresponding_DNA('ATcg'))