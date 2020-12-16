#!/usr/bin/python3
''' Used to create the id attributes based on the given input'''
a = input("String: ").split()
print('id = "',end="")
for i in range(len(a)):
    if(i<len(a)-1):
        print(a[i],end="_")
    else:
        print(a[i]+'"')
