text='Hello,Python!'
t1=text.strip()
print(t1)
t2=t1.replace('!', '?')
print(t2)
t3=t2.upper()
print(t3)
rt=t3.strip().lower().replace('?','!')
try:
    assert rt == 'hello,python!'
    print('Yes')
except AssertionError:
    print('No')

