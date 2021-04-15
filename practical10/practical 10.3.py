def score(name,codes,poster,test):
    final=codes*0.4+poster*0.3+test*0.3#calculate the score
    return name,final
a,b=score('Xiao Ming',100,90,90)#put name into a, put score into b
print(a,b)