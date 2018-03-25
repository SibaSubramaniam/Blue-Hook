lines=[]
substr="credited"
with open ('text.txt','rt') as file:
    for line in file:
        line.rstrip('\n')
        if line.lower().find(substr)!=-1:
            lines.append(line)
        ls=str(lines)
        #print(ls)
        lss=ls.rsplit('BNK')
        print(lss)
        
            
        
        
        
       
"""with open ('Downloads/ip.txt','wt') as ipfile:
    ipfile.write(ls)
    lss=ls.rsplit('BNK')
lsstr=str(lss)
idx=lsstr.find('credited')
print (idx)
subs=lsstr[:idx+10]
print (subs)
for i,n in enumerate(ls):
            print(i)
            print(n)
        for line1 in ls:
            line1.rstrip('\n')
            print(line1)
            
            if line1.lower().find(substr)!=-1:
                linesfinal.append(line1)"""
