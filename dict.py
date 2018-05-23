# -*- coding: utf-8 -*-
import json
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

# print wordArr
# for item in expArr:
#     print item.encode('utf-8')

retArr=[]
for item in range(0,506):
    tempArr=[]
    tempExp=""
    for j in range(0,len(expArr[item])):
        tempExp=tempExp+expArr[item][j].encode('utf-8')
    tempArr.append("firefly forest")
    tempArr.append(wordArr[item])
    tempArr.append(tempExp)
    tempArr.append(0)
    tempArr.append(0)
    tempArr.append(0.0002)
    retArr.append(tempArr)

f=open('import.txt','w')
f.write('"user_name","word","interpret","likes","hates","score"\n')
for item in range(0,506):
    tempExp=""
    for j in range(0,len(expArr[item])):
        tempExp=tempExp+expArr[item][j].encode('utf-8')
    f.write('"firefly forest","')
    f.write(wordArr[item])
    f.write('","')
    f.write(tempExp)
    f.write('",')
    f.write('0,')
    f.write('0,')
    f.write('0.0002\n')