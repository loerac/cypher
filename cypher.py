import argparse
import sys
import os.path

# Function to encrypt taking a string as a parameter.
def enc(phrase):
    temp=''
    j=0
    
    # Removing all the new lines.
    phrase=''.join(phrase.split('\n'))

    # Moving the second half and moving it in front with the first half.
    # Ex: 123abc -> c1b2a3
    for i in range(len(phrase)):
        if i%2==0:
            temp+=phrase[len(phrase)-j-1]
            j+=1
        else:
            temp+=phrase[j-1]
    phrase=''

    # Finding the middle character.
    # If the string length is even, it'll go down one character.
    # If the string length is odd, it'll just take the middle character.
    mid=(int(len(temp)/2)-1) if len(temp)%2 ==0 else int(len(temp)/2)
    j=0

    # Doing the same shifting of character as before,
    # but instead of starting at the first character,
    # go from the middle character down to the first.
    # Ex: 123abc -> 3c2b1a
    for i in range(0,len(temp)):
        if i%2==0:
            phrase+=temp[mid]
            j+=1
            mid-=1
        else:
            phrase+=temp[len(temp)-j]
    return phrase 

# Function to decrypt taking a string as a parameter
def dec(phrase):
    temp=''
    # Removing all the new lines in the string.
    temp=''.join(phrase.split('\n'))
    phrase=''
    
    # Setting the last index number from the length of the string.
    # If the string length is even, grab the second to last character.
    # If the string length is odd, grab the last character.
    s=(len(temp)-2) if len(temp)%2==0 else (len(temp)-1)

    # Going from the end to the beginning of the string
    # every second character starting from what index [s] is
    # After reaching the beginning, switch the index [s]
    # to either be the last or second to last character.
    # If the string length is even, start at the second to last character.
    # If the string length is odd, start at the last character.
    # Ex: 123abc -> b31ca2
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
    # Start at index 1 and go to the end of the string ever second character.
    # After reaching the end of the string,
    # go from the end to the beginning of the
    # starting at the last or second to last character.
    # If the string length is even, start at the second to last character
    # If the string length is odd, start at the last character
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

    # For the string lenghts that are odd at the end of the loop
    if len(phrase)%2!=0:
	temp+=phrase[s]
    phrase=''
    c=0
    
    # A temporary way to add back the new lines.
    # If the sentence ends and there is no space, add a new line.
    for i in range(len(temp)-1):
        if (temp[c]=='.' or temp[c]=='!' or temp[c]=='?') and temp[c+1].isalpha():
	    phrase+=temp[c]+'\n'*2
	else:
            phrase+=temp[c]
	c+=1
    phrase+=temp[c]
    return phrase

# Reading the arguements given for a file: to encrypt or decrypt the file.
p=argparse.ArgumentParser(description='Encrypt/decrypt a file')
p.add_argument('filename')
p.add_argument('-e','--encrypt',dest='action',action='store_const',const=enc,help='Encrypt message')
p.add_argument('-d','--decrypt',dest='action',action='store_const',const=dec,help='Decrypt message')
a=p.parse_args()

if sys.argv[0]==a.filename:
    print('\n\tError: cannot run this file\n')
else:
    # Opening the file that was given for reading.
    if os.path.isfile(a.filename):
        with open(a.filename,'rt') as f:
            phrase=f.read().upper()

            # Depending on the arguement, the content of the-
            # file with either be encrypted or decrtyped.
            phrase=a.action(phrase.upper())

            print('\n'+str(phrase)+'\n')

        # Writing the content of the phrase back into the file.
        with open(a.filename,'wt') as f:
            f.write(phrase)
    else:
        print('\n\tError: file not found\n')
