#Tuple
B2a=(23,24,26,27,28,29,30,31,32, 33, 35, 36, 37,)
B2b=(39,40,41,42,43,44,)
print(B2a)
print(B2b)

#Cocatination
b=B2a+B2b
print(b)

#Length of Tuple
print(len(b))

#Type of Tuple
print(type(b))

#Slicing operation
print(b[3:7])
print(b[7:])
print(b[:7])

#Mesbership operation
print(42 in b)

#Repeatation
print((b)*10)

#Minimum value and maximum value from the tuple
print(min(b))
print(max(b))

#Converting Tuple into list
print(list(b))

#Converting list into tuple
print(tuple(b))