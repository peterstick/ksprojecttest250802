x = [1, 2, 3, 4, 5] # list

print("slicing=========")
print(x[2:5])  #[end_index+1]]
print("apend=======")
x.append(7)
print(x)
print("insert=============")
x.insert(1, 9)
print(x)
print("remove=========")
x.remove(1)
print(x)
print("9->6=========")
x[0] = 6
print(x)
print("x")

print("배열의 길이====")
len(x)

print("배열의 마지막 인덱스")
print(len(x)-1)


x = {'a':100, 'b': 200} #dictionary, key:value
print(x)
print(x['a'])
print(x['b'])

print("dictionary 에제=======")
x['c'] = 10
print(x)
print(x['c'])
#print(x['d'])

del x['a'] #딕셔너리에서 특정 기값 지우기
print(x)


print(x.keys())
print(x.values())
print(x.items())

print(x.clear()) #딕셔너리 지우기
print(x)