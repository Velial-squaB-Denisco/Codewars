"""Дополните функцию/метод (в зависимости от языка), чтобы они возвращали true/True,
если их аргументом является массив с той же структурой вложенности и той же длиной вложенных массивов, что и первый массив.

Например:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )"""

def same_structure_as(original, other):

    if isinstance(original, list) != isinstance(other, list):
        return False

    if not isinstance(original, list):
        return True

    if len(original) != len(other):
        return False
    
    for o, e in zip(original, other):
        if not same_structure_as(o, e):
            return False
    return True

print(same_structure_as([1,[1,1]],[2,[2,2]]))