fname=input('enter the file name:')
genes=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
import re
import os

os.chdir('D:\课件\第二学期\IBI\practical\上交\8')
output=open(fname)
a=0
c=''
find=False
genetic_code= {'ATA':'J', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'B', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Z',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'O', 'TAG':'U',
    'TGC':'C', 'TGT':'C', 'TGA':'X', 'TGG':'W',}#genetic code
for line in genes: #search every line
    if re.search('^>',line):
        find= False #stop adding bases
        if "unknown function" in line:
            find=True #start adding bases
            if a!=0:#to output this name of unknown genes and the gene before this gene
                output.write('\n')
                output.write(str(a/3))
                output.write('\n')
                pr=''#protein
                for i in range (0,len(c),3):
                    pr=pr+genetic_code[c[i:i+3]]#add amino acid to protein            
                output.write(pr)
                output.write('\n')
                output.write('\nname:'+'\n'+re.search(r'gene:(\w+)',line).group(1))
                a=0#initialize
                c=''
            elif a==0:#output the name of first unknown genes
                output.write('name:'+  re.search(r'gene:(\w+)', line).group(1))
    elif find ==True: #adding bases
        a=a+len(line)-1
        b=a#to calculate last unknown gene
        c=c+line.rstrip()
        d=c
output.write('\n')
output.write(str(b/3))
output.write('\n')
pr=''#protein
for i in range (0,len(d),3):
    pr=pr+genetic_code[d[i:i+3]]#add amino acid to protein
output.write(pr)
output.close()
genes.close()
