def tuple(tup):
    # new_tuple=()
    new_tuple=tup[::2]+()
    return new_tuple
tup=(1,2,3,5,6,7,5,8,4)
new_tuple=tuple(tup)
print(new_tuple)