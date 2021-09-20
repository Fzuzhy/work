key=['auto','break','case','char','const','continue','default','do','double','else','enum','extern','float','for','goto','if',
'int','long','register','return','short','signed','sizeof','static',
'struct','switch','typedef','union','unsigned','void','volatile','while']
num=0
snum=0
cnum=[]
ienum=0
ifstack=[]
ieienum=0
anno=0

def keyword(f):
    global num
    global snum
    global ienum
    global ieienum
    global anno
#    for line in f:
 #       print(line)
    for line in f:
        l=len(line)
        i = 0
        while True:
            if(i>=l-1):
                break
            #print('i',i)
            if(anno==1 and line[i]!='*'):
                continue
            if(anno==1 and line[i]=='*'):
                if(line[i+1]=='\\'):
                    anno=0
                continue
            if(line[i]>'z' or line[i]<'a'):
                if(line[i]=='\''):
                    j=i
                    while j < l - 1:
                        if (line[j] =='\''):
                            break
                        j+=1
                elif(line[i]=='\"'):
                    j = i
                    while j < l - 1:
                        if (line[j] == '\"'):
                            break
                        j += 1
                elif(line[i]=='\\'):
                    if(line[i+1]=='\\'):
                        break
                    elif(line[i+1]=='*'):
                        anno=1
                else:
                    i+=1
                continue
            j=i
            while j<l-1:
                #print('j',j)
                if(line[j]>='a' and line[j]<='z' and (line[j+1]<'a' or line[j+1]>'z')):
                    break
                j+=1
                #print(line[j])
            for k in key:
                if(k==line[i:j+1]):
                    #print(k)
                    num+=1
                    if(k=='switch'):
                        snum+=1
                    if(k=='case'):
                        if(len(cnum)!=snum):
                            cnum.append(1)
                        else:
                            cnum[snum-1]+=1
                    if(k=='if' and line[i-2]!='e'):
                        ifstack.append('if')
                    if(k=='else'):
                        if(line[j+2]!='i'):
                            if(ifstack[-1]=='if'):
                                ienum += 1
                            else:
                                while (ifstack[-1] != 'if'):
                                    ifstack.pop()
                                ieienum+=1
                            ifstack.pop()
                        else:
                            ifstack.append('ei')
                    break
            i=j+1

flist=[]
name=input()
level=int(input())
f=open(name,encoding='utf-8')
#f=f.lower()
for line in f:
    line=line.replace('\n'," ")
    flist.append(line)
#for line in flist:
#    print(line)
keyword(flist)
if(level>=1):
    print("total num:",num)
if(level>=2):
    print("switch num:",snum)
    print("case num:",end='')
    for i in range(snum):
        if(i!=snum-1):
            print(cnum[i],end=' ')
        else:
            print(cnum[i])
if(level>=3):
    print("if-else num:",ienum)
if(level>=4):
    print("if-elseif-else num:",ieienum)
#C:/software/test.c