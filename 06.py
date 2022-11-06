'''
 Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')


'''
a=input("Sample data: ")
b=input("Sample data: ")
c=input("Sample data: ")
d=input("Sample data: ")

# print(list[a,b,c,d])
# print(tuple(a,b,c,d))

e=[a,b,c,d]
# f=tuple{a,b,c,d}
# f=tuple(list[e])
f=(a,b,c,d)
print(e)
print(tuple(f))






