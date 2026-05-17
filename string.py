#evezetme
'''a=input("daxil et")
yeni=""
for i in a:
    if i=="a":
        i="b"
    elif i=="A":
        i="B"
    yeni+=i
print(yeni)'''
#addim
'''a="123456789"
print(a[::2])
print(a[::-1])
print(a[3:])#3den sonra
print(a[:6])#6-a qeder
print(a[2:7])#2den 7e qeder
print(a[-2:-7])'''
#split
'''def my_split(string,ayirici):
    list1=[]
    word=""
    for i in range(len(string)):
        if string[i]!=ayirici:
            word+=string[i]
        elif word!="":
            list1+=[word]
            word=""
    if word!="":
        list1+=[word]
    return list1
string=input("ad ata adi soyad daxil et:")
list1=my_split(string," ")
print(list1)
print(list1[3]," ",list1[0][0],".",list1[1][0],".",sep="")'''
#lab6
#1
'''
a="gunel yatdi"
b=input()
if b in a:
    print("simvol var")
else:
    print("simvol yoxdur")'''
#2
'''str1="aabbbAAABBccCCC"
str2=""
for i in str1:
    if i=="a":
        i="b"
    elif i=="b":
        i="a"
    elif i=="A":
        i="B"
    elif i=="B":
        i="A"
    str2+=i
print(str2)'''
#3
'''def my_split(a,ayirici):
    word=""
    list1=[]
    for i in range(len(a)):
        if a[i]!=" ":
            word+=a[i]
        elif word!="":
            list1+=[word]
            word=""
    if word!="":
        list1+=[word]
    return list1
a=input("daxil et")
list1=my_split(a," ")
print(list1)
say=0
for i in list1:
    if i!=1000:
     say+=1
print(say)'''
#4
def lenn(a):
    say=0
    for i in a:
        if i!=1000:
         say+=1
    return say
    
def my_split(a,ayirici):
    word=""
    list1=[]
    for i in range(len(a)):
        if a[i]!=" ":
            word+=a[i]
        elif word!="":
            list1+=[word]
            word=""
    if word!="":
        list1+=[word]
    return list1
a=input("daxil et")
list1=my_split(a," ")
print(list1)
maxi=0
for i in range(len(a)):
    if lenn(a[i])>maxi:
        maxi=lenn(a[i])
print(maxi)
    


            
            




