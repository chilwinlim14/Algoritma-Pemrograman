def reverse(x):
    str = ''
    for i in x:
       str = i + str
    return str

x = input('Masukkan sesuatu: ')

print('String original: ',end = '')
print(x)
print('String Reverse: ',end = '')
print(reverse(x)) 