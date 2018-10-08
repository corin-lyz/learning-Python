#测试dict
d = {'A':42,'Boba':89,'conda':67,'dannis':4353}
print(d['A'])
#d.insert('dannis')
d['dannis'] = 82
print(d['dannis'])

#-*-测试dict.get()以及pop()函数
print(d.get('A'))
print(d.get('B'))
d.pop('Boba')
print(d)

#测试set
s = set([1,2,1,2,3,5,3,4])
print(s)
s.add(8)
print(s)
s.remove(3)
print(s)
s2 = set([1,2,3,6,7,8,9])
print(s&s2)
print(s|s2)
