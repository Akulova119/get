def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
n= int(input())
print (dec2bin(n))