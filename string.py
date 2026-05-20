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


    


            
            




