import numpy
ejemplo = [1,3,2,'abc']
print(ejemplo)
ejemplo.append(4)
print(ejemplo)
ejem1 =[5,8,9,6,7]
ejemplo.extend(ejem1)
print(ejemplo)
print(ejemplo.count())
print(ejemplo.index(1))
ejemplo.index(0,0)
print(ejemplo)
ejemplo.pop(0)
print(ejemplo)
print(ejemplo.reverse())
ejemplo.sort()
print(ejemplo)