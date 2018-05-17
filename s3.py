# s1 = "送奸文"
#
# if 'aa' not in s1:
#     print ('ok')
# else:
#     print ('error')
#
# print (type(bool('True')))
#
# # if
#
# n = 123
# m = 'shizhengwen'
# #print (n.upper())
# a = n.bit_length()
# print (n*3)
# print (a)
# #print (len(n * 3 + 'a')).bit_length()
#
# a = True
# s1 = 'alex'
#
# print (int('011', base=16))
#
# a = 260
# print (a.bit_length())
#
# b = 'alex'
# c = b.center(25, '*')
# print (c, len(c))
# print (b.encode('GBK'))
#
# d = 'I am {name}, age {age}'
# print ('length =', len(d))
# e = d.format(name = 'alex', age = 19)
# print (e)

s = "sdifadkfTTdf t\tfdaf\tdasdf"
v = s.expandtabs(20)
print (v)
print (v.capitalize())
print (v.upper())
print (v.isalpha())

#join
c = 'thisdfa'
v = '_'
print (v.join(c))