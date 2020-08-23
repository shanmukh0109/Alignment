import copy
s1=list(input('enter seq 1'))
s2=list(input('enter seq 2'))
if len(s1)<len(s2):
    s2,s1=s1,s2
gapscore=int(input('eneter gap score'))
matchscore=int(input('enter match score'))
mismatchscore=int(input('enter mismatch score'))
l1=[0]
l=[]
for i in range(1,len(s1)+1):
    l1.append(l1[i-1]+gapscore)
for i in range(1,len(s2)+1):
    l.append([l1[i]])
l=[l1]+l
for i in range(len(s2)):
    for j in range(len(s1)):
        if s1[j]==s2[i]:
            l[i+1].append(1)
        else:
            l[i+1].append(0)
g=[]
o=copy.deepcopy(l)
for i in range(1,len(l)):
    for j in range(1,len(l[i])):
        if l[i][j]==1:
            b1=(o[i-1][j-1])+matchscore
            b2=(o[i-1][j])+gapscore
            b3=(o[i][j-1])+gapscore
            re=[b1,b2,b3]
            s=""
            if re[0]==max(re):
                s+="D"
            if re[1]==max(re):
                s+="U"
            if re[2]==max(re):
                s+="L"
            g.append(s)
            l[i][j]=[max(re),s]
            o[i][j]=max(re)
        else:
            b1=(o[i-1][j-1])+mismatchscore
            b2=(o[i-1][j])+gapscore
            b3=(o[i][j-1])+gapscore
            re=[b1,b2,b3]
            s=""
            if re[0]==max(re):
                s+="D"
            if re[1]==max(re):
                s+="U"
            if re[2]==max(re):
                s+="L"
            g.append(s)
            l[i][j]=[max(re),s]
            o[i][j]=max(re)
print('after applying needleman Wunsch algorithm')
print(' ',end="\t")
print('\t'+'\t'+'\t'.join(s1)+'\t')
s2=[' ']+s2
for i in range(len(l)):
    print(s2[i],end="\t\t")
    for j in range(len(l[i])):
        print(l[i][j],end="\t")
    print()
