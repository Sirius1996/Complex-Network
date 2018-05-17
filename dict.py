# -*- coding: utf-8 -*-
wordArr=[]
expArr=[]
with open("dict.txt") as inFile:
    eLine=inFile.readlines()
    word=""
    exp=""
    for line in eLine:
        if line!='\n':
            tempStr=''+line
            for i in tempStr.decode('utf-8'):
                tempI=i.encode('utf-8')
                if tempI.isalpha():
                    word=word+tempI
                elif tempI>='0' and tempI<='9':
                    word=word+tempI
                elif tempI=='.' or tempI==' ' or tempI=='-' or tempI==',' or tempI=='(' or tempI==')' or tempI=='（' or tempI=='）':
                    word=word+tempI
                elif tempI=='/' or tempI=='\n':
                    pass
                else:
                    exp=exp+tempI


            wordArr.append(word)
            expArr.append(exp.decode('utf-8'))
            word=""
            exp=""

print wordArr
for item in expArr:
    print item.encode('utf-8')