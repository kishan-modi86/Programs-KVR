b=input('enter a word')
print('forward direction')
for ch in b:
    print(ch)
print('------------2----------')
for i in range(0,len(b)):
    print(b[i])
print('------------3----------')
for i in range(-len(b),0):
    print(b[i])
print('backward direction')
for ch in b[::-1]:
    print(ch)
print('--------2----------')
for i in range(-1,-len(b)-1,-1):
    print(b[i])
print('--------3------------')
for i in range(len(b)-1,-1,-1):
    print(b[i])