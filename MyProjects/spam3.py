spam=['a', 'b', 'c', 'd', 'e', 'f']

#print(spam[int('3'*2)/11])

print(spam[:2])

print(spam.index('c'))


spam.remove('c')
print(spam)


spam.insert(2, 'j')
print(spam)