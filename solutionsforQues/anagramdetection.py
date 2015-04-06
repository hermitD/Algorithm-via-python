# -*- coding: utf-8 -*- 

'''
one string is an anagram of another if the second is simply a rearrangement of the first. 
For example, 'heart' and 'earth' are anagrams. The strings 'python' and 'typhon' are anagrams as well. 
For the sake of simplicity, we will assume that the two strings in question are of equal length and that they are made up of symbols 
from the set of 26 lowercase alphabetic characters. Our goal is to write a boolean function that will take two strings and 
return whether they are anagrams.
'''



def ad1(s1,s2):
    #simplely Checking Off for every data
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

def ad2(s1,s2):
    #sort and check
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

def ad3(s1,s2):
    # brute force
    #...
    
def ad4(s1,s2):
    #Count and Compare
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK    


def main():
    
    pass




if __name__ == '__main__':
    main()