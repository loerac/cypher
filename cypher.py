import argparse

def enc(phrase):
    temp=''
    j=0
    phrase=phrase.split('\n')
    for i in range(0,len(phrase)):
        temp+=phrase[i]
    phrase=temp
    temp=''
    for i in range(len(phrase)):
        if i%2==0:
            temp+=phrase[len(phrase)-j-1]
            j+=1
        else:
            temp+=phrase[j-1]
    phrase=''
    mid=(int(len(temp)/2)-1) if len(temp)%2 ==0 else int(len(temp)/2)
    j=0
    for i in range(0,len(temp)):
        if i%2==0:
            phrase+=temp[mid]
            j+=1
            mid-=1
        else:
            phrase+=temp[len(temp)-j]
    return phrase 

def dec(phrase):
    temp=''
    for i in range(len(phrase)):
	if phrase[i]!='\n':
	    temp+=phrase[i]
    phrase=''
    s=(len(temp)-2) if len(temp)%2==0 else (len(temp)-1)
    for i in range(len(temp)):
        if i<(len(temp)/2 -1):
	    phrase+=temp[s]
	    s-=2
        elif s<=0:
	    phrase+=temp[s]
	    s=(len(temp)-1) if len(temp)%2==0 else (len(temp)-2)
	else:
	    phrase+=temp[s]
	    s-=2
    temp=''
    s=1
    b=True
    for i in range(len(phrase)-1):
	if s<(len(phrase)-1) and b:
	    temp+=phrase[s]
	    s+=2
	    if s>=(len(phrase)-1):
        	    if len(phrase)%2==0:
	        	temp+=phrase[s]
        	    s=len(phrase)-2 if len(phrase)%2==0 else len(phrase)-1
	            b=False
	else:
	    temp+=phrase[s]
	    s-=2
    if len(phrase)%2!=0:
	temp+=phrase[s]
    phrase=''
    c=0
    for i in range(len(temp)-1):
        if (temp[c]=='.' or temp[c]=='!' or temp[c]=='?') and temp[c+1].isalpha():
	    phrase+=temp[c]+'\n'*2
	else:
            phrase+=temp[c]
	c+=1
    phrase+=temp[c]
    return phrase

p=argparse.ArgumentParser(description='Encrypt/decrypt a file')
p.add_argument('filename')
p.add_argument('-e','--encrypt',dest='action',action='store_const',const=enc,help='Encrypt message')
p.add_argument('-d','--decrypt',dest='action',action='store_const',const=dec,help='Decrypt message')
a=p.parse_args()
with open(a.filename,'rt') as f:phrase=f.read().upper()
phrase=a.action(phrase.upper())
phrase='\n'+str(phrase)+'\n'
print(phrase)
with open(a.filename,'wt') as f:f.write(phrase)
