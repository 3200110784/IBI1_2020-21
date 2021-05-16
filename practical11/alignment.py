import re
SOD2_human=open('SOD2_human.fa')
SOD2_mouse=open('SOD2_mouse.fa')
RandomSeq=open('RandomSeq.fa')
blosum62=open('BLOSUM62.txt')
seq1=''
seq2=''
seq3=''
def read_protein(seq,seqn):#put protein in seq
    for line in seq:
        if re.search !='>':
            seqn=line
    return seqn
seq1=read_protein(SOD2_human,seq1)
seq2=read_protein(SOD2_mouse,seq2)
seq3=read_protein(RandomSeq,seq3)
string=''
list=[]
for string in blosum62:
    list.append(string[1:].split())
def compare(s1,s2,list):
    index={'A':'1','R':'2','N':'3','D':'4','C':'5','Q':'6','E':'7','G':'8','H':'9','I':'10','L':'11','K':'12','M':'13','F':'14','P':'15','S':'16','T':'17','W':'18','Y':'19','V':'20','B':'21','Z':'22','X':'23','*':'24'}
    edit_distance=0
    j=0
    for i in range (len(s1)):
        if	s1[i]!=s2[i]:
            j=j+1
            b=list[int(index[s1[i]])]
            edit_distance = edit_distance+int(b[int(index[s2[i]])])
    print(j/len(s1))
    print(edit_distance)
compare(seq1,seq2,list)
compare(seq1,seq3,list)
compare(seq2,seq3,list)

