import xml.dom.minidom
from xml.dom.minidom import parse 
import sys
sys.setrecursionlimit(500000)#Increase the number of iterations available
DOM= xml.dom.minidom.parse('go_obo.xml')#input the xml file
collection=DOM.documentElement
terms=collection.getElementsByTagName('term')
dictionary={}
counter=[]
for term in terms:#a dictionary that contains all immediate childnodes
    id=term.getElementsByTagName('id')
    dictionary[id[0].firstChild.data]=[]
for term in terms:
    id=term.getElementsByTagName('id')
    is_as=term.getElementsByTagName('is_a')
    for is_a in is_as:
        dictionary[is_a.firstChild.data].append(id[0].firstChild.data)#add all childnodes
def count(a):
    for term in terms:#check every term
        if a in term.getElementsByTagName('defstr')[0].firstChild.data:#if 'a' exist in defstr, we thought we find what we need
            ids=term.getElementsByTagName('id')[0].firstChild.data#get the id information
            if dictionary[ids] !=[]:
                counter=dictionary[ids]
                n=count2(counter)
    print('the childnode number of '+a+' is '+str(n))
    return n
def count2(counter):
    for i in range(len(counter)):
        if counter[i] not in listf:
            listf.append(counter[i])#put the childnodes into listf
            count2(dictionary[counter[i]])#put the 'grandchildnodes' into listf
    return len(listf)
listf=[]#listf is used to store the childnodes 
count('DNA')
listf=[]#each time the function is exexuted, clear listf
count('RNA')
listf=[]
count('protein')
listf=[]
count('lipid')